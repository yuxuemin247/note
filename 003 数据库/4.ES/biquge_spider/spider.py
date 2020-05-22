#!/usr/bin/python3
# coding: utf-8
import asyncio
import random

import requests
from lxml import etree

from es_ import ESStorage

es = ESStorage('http://39.100.114.253/')  # ES 索引库

base_url = 'http://www.xbiquge.la'
start_url = base_url + '/paihangbang/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


class DownloadError(Exception):
    pass


async def download(url, request=requests.get):
    resp = request(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        return resp

    raise DownloadError(f'{url} 下载失败')


async def start_request():

    resp = await download(start_url)
    root = etree.HTML(resp.text)
    for a in root.xpath('//div[starts-with(@class, "box")]/ul[1]/li[position()>1 and position()<22]//a'):
        name = a.text
        book_url = a.xpath('./@href')[0]
        print(name, book_url)

        await asyncio.sleep(random.uniform(0.3, 0.5))
        await get_book(name, book_url)


async def get_book(name, book_url):
    resp = await download(book_url)
    root = etree.HTML(resp.text)
    book = {}
    book['name'] = name
    book['cover'] = root.xpath('//div[@id="fmimg"]/img/@src')
    book['author'] = root.xpath('//div[@id="info"]/p[1]/text()')[0].split('：')[-1]
    book['last_time'] = root.xpath('//div[@id="info"]/p[3]/text()')[0]
    book['last_chapter_title'] = root.xpath('//div[@id="info"]/p[last()]//text()')[-1]

    _, ret = es.add_doc('biquge', 'book', **book)

    print(_, book)

    for a in root.xpath('//div[@id="list"]//a'):
        name = a.text
        cha_url = base_url+ a.xpath('./@href')[0]

        await get_book_chapter(ret['_id'], name, cha_url)


async def get_book_chapter(book_id, chapter_title, url):
    resp = await download(url)
    # with open('a.html', 'wb') as f:
    #     f.write(resp.content)

    root = etree.HTML(resp.text)
    content = '<br>'.join(root.xpath('//div[@id="content"]/text()'))
    _, ret = es.add_doc('biquge', 'chapters', book_id=book_id, title=chapter_title, content=content)
    print(ret['_id'], f'{chapter_title}章节 添加索引成功!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 获取IO多路复用的事件模型 epoll/poll/select
    loop.run_until_complete(start_request())
    # loop.run_until_complete(get_book_chapter('', '', 'http://www.xbiquge.la/2/2029/1458171.html'))
