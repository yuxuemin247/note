#!/usr/bin/python3
# coding: utf-8

import requests
from urllib.parse import quote


class ESStorage:
    """
    ElasticSearch REST api 封装操作的方法
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def create_index(self, name, shards=5, replicas=1):
        url = self.base_url + f'/{name}'
        data = {
            "settings": {
                "number_of_shards": shards,
                "number_of_replicas": replicas
            }
        }
        resp = requests.put(url, json=data)
        return resp.status_code == 200

    def delete_index(self, name):
        url = self.base_url + f'/{name}'
        resp = requests.delete(url)
        return resp.status_code == 200

    def add_doc(self, _index, _type, **kwargs):
        url = self.base_url + f'/{_index}/{_type}'
        if 'id' in kwargs:
            url += f'/{kwargs["id"]}'
            kwargs.pop('id')  # 删除数据文档中的id

        resp = requests.post(url, json=kwargs)
        return resp.status_code == 200, resp.json()

    def update_doc(self, _index, _type, _doc_id, **kwargs):
        url = self.base_url + f'/{_index}/{_type}/{_doc_id}'
        resp = requests.put(url, json=kwargs)
        return resp.status_code == 200

    def del_doc(self, _index, _type, _doc_id):
        url = self.base_url + f'/{_index}/{_type}/{_doc_id}'
        resp = requests.delete(url)
        return resp.status_code == 200

    def get_doc(self, _index, _type, _doc_id):
        url = self.base_url + f'/{_index}/{_type}/{_doc_id}'
        resp = requests.get(url)
        return resp.json()

    def search(self, kw):
        url = self.base_url + f'/_search/?q={quote(kw)}'
        resp = requests.get(url)
        return resp.json()


if __name__ == '__main__':
    es = ESStorage('http://47.105.137.19')
    # ret = es.get_doc('zzindex', 'user', '2')
    # print(ret)
    #
    # ret = es.search('西安')
    # print(ret)

    # print(es.create_index('biquge'))
    data = {
        'title': '牧神记',
        'author': '宅猪',
        'last_time': '2019-12-15 11:16:37',
        'last_chapter': '宅猪新书，《临渊行》已经上传',
        'summary': '大墟的祖训说，天黑，别出门。大墟残老村的老弱病残们从江边捡到了一个婴儿，取名秦牧，含辛茹苦将他养大。'
                   ' 这一天夜幕降临，黑暗笼罩大墟，秦牧走出了家门……做个春风中荡漾的反派吧！ 瞎子对他说。秦牧的反派之路，正在崛起！'
    }
    # ret = es.add_doc('biquge', 'rank', **data)
    # print(ret)
    # print(es.get_doc('biquge', 'rank', 'AXHyGTAj5dXdNBG_GXV_'))

    flag, ret = es.add_doc('biquge', 'chapters', book_id='AXHyGTAj5dXdNBG_GXV_', chapter_no=2, title="正文卷 第二章 四灵血",
                           content="""
     司婆婆拉着他兴冲冲的往村里走，笑道：“别看了，快点过来，今天是你的大日子！村长，马爷，都出来！”

    村里燃起了篝火，村长又被人用担架抬了出来，沉声道：“四灵都找到了？”

    “都找到了。”

    独臂的马爷拖来了一条几丈长的大蛇，碧青色，也还活着，泛着腥气，只是被马爷单手捏住七寸，动弹不得。
    """)

    print(flag, ret['_id'], ret)

    # print(es.del_doc('biquge', 'chapters','AXHyHfy15dXdNBG_GXWB'))
