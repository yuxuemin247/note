[TOC]

# Django缓存机制

## 缓存介绍

```python
在动态网站中，用户所有的请求，服务器都会去数据库中进行相应的增、删、查、改、渲染模板，执行业务逻辑，最后生成用户看到的页面。
当一个网站的用户访问量很大的时候，每一次的的后台操作，都会消耗很多的服务端资源，所以必须使用缓存来减轻后端服务器的压力。
缓存是将一些常用的数据保存内存或者memcache中，在一定的时间内有人来访问这些数据时，则不再去执行数据库及渲染等操作，而是直接从内存或memcache的缓存中去取得数据，然后返回给用户。
```

3种粒度：

```python
1. 全站缓存
2. 单页面缓存
3. 页面中局部缓存
```

## 6种缓存方式

```python
1. 开发调试缓存
2. 内存缓存
3. 文件缓存
4. 数据库缓存
5. Memcache缓存(使用python-memcached模块)
6. Memcache缓存(使用pylibmc模块)
经常使用的有文件缓存和Mencache缓存
```

## Django中缓存的使用

缓存到文件配置(6种之一)

```python
# settings中配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 指定缓存使用的引擎
        'LOCATION': '/var/tmp/django_cache',  # 指定缓存的路径
        'TIMEOUT': 300,  # 缓存超时时间(默认为300秒,None表示永不过期)
        'OPTIONS': {
            'MAX_ENTRIES': 300,  # 最大缓存记录的数量（默认300）
            'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
        }
    }
}
```

### 单页面缓存

```python
# 视图层
from django.views.decorators.cache import cache_page
# 代表缓存5s
@cache_page(5)
def cache_test(request):
    print('走视图函数')
    ctime=time.time()
    return render(request,'index.html',locals())
```

### 页面局部缓存

```python
{ % load cache %}
# 传两个参数:第一个参数是超时时间，第二个参数是key值,唯一的标志#
{ % cache 5 'ttt' %}
    当前时间是：{{ ctime }}
{ % endcache %}

-缓存存储的数据格式
unique_snowflake = {
    'index': asdfafasfasf,
    'test': aerafdgerytwrega,
    'ttt': saefasfaefqwe,
    'yyy': asdfasfdsad,
}
```

### 全站缓存

```
# 在settings中配置两个中间件
'django.middleware.cache.UpdateCacheMiddleware'
..........
'django.middleware.cache.FetchFromCacheMiddleware'

# 配置缓存时间
CACHE_MIDDLEWARE_SECONDS=10
```

