- 什么是缓存？为什么使用缓存？

  数据库的是 web 应⽤性能的瓶颈，为了提⾼ web 应用访问效率，尽可能减少数据库的操作，可以将经常访问的数据缓存起来，再次使⽤用时直接从缓存中获取，而不是每次都操作数据库。

- flask-cacheing
  - flask 数据缓存扩展
  - flask-cache 已经不在维护，因此使用 flask-caching 

- 安装

  - ```
    pip install flask-caching
    pip install redis
    ```

- 初始化

  - ```python
    from flask_caching import Cache
    cache = Cache()
    cache.init_app(app=app, config={'CACHE_TYPE': 'simple'})
    ```
  
- 配置

  ```
  CACHE_TYPE:设置缓存的类型
      设置都是在config中设置的
  # 下面五个参数是所有的类型共有的
  CACHE_NO_NULL_WARNING = "warning" # null类型时的警告消息
  CACHE_ARGS = [] # 在缓存类实例化过程中解包和传递的可选列表，用来配置相关后端的额外的参数
  CACHE_OPTIONS = {}  # 可选字典,在缓存类实例化期间传递，也是用来配置相关后端的额外的键值对参数
  CACHE_DEFAULT_TIMEOUT # 默认过期/超时时间，单位为秒
  CACHE_THRESHOLD # 缓存的最大条目数
  
  
  CACHE_TYPE = null # 默认的缓存类型，无缓存
  CACHE_TYPE = 'simple' # 使用本地python字典进行存储，非线程安全
  
  
  CACHE_TYPE = 'filesystem' # 使用文件系统来存储缓存的值
  CACHE_DIR = "" # 文件目录
  
  CACHE_TYPE = 'memcached' # 使用memcached服务器缓存
  CACHE_KEY_PREFIX # 设置cache_key的前缀
  CAHCE_MEMCACHED_SERVERS # 服务器地址的列表或元组
  CACHE_MEMCACHED_USERNAME # 用户名
  CACHE_MEMCACHED_PASSWORD # 密码
  
  
  CACHE_TYPE = 'redis' # 使用redis作为缓存
  CACHE_KEY_PREFIX # 设置cache_key的前缀
  CACHE_REDIS_HOST  # redis地址
  CACHE_REDIS_PORT  # redis端口
  CACHE_REDIS_PASSWORD # redis密码
  CACHE_REDIS_DB # 使用哪个数据库
  # 也可以一键配置
  CACHE_REDIS_URL 连接到Redis服务器的URL。示例 redis://user:password@localhost:6379/2
  ```
  
  

- 缓存视图函数

  ```python
  @app.route('/')
  @cache.cached(timeout=30)  # timeout 设置超时时间
  def index():
  		print('查询数据库')
      return '缓存视图函数'
  
  @app.route('/clear/')
  def index():
  		cache.clear()
      return '清除所有的缓存，操作需慎重，不推荐使用'
  ```

- 缓存普通函数（无参）

  ```python
  # 缓存普通函数时，推荐指定 key_prefix，缓存 key 的前缀
  # 否则 key 即为调⽤的视图函数所在的路由
  # 单独缓存某个函数，提供更好的复用性
  @cache.cached(timeout=50, key_prefix='get_list')
  def get_list():
      return [random.randint(0, 10) for i in range(10)]
  
  @app.route('/random/')
  def random():
  		return get_list()
  ```

- 缓存普通函数（有参）

  ```python
  @cache.memoize(timeout=50, make_name='param_func')
  def param_func(a, b):
      return a+b+random.randint(1, 50)
  
  @app.route('/cache/')
  def cache():
      param_func(1, 2)
  		return 'cache'
  
  @app.route('/delete/')
  def delete():
      cache.delete_memoized(param_func, 1, 2)
  		return 'delete'
  ```

- 缓存对象（键值对）

  ```python
  @app.route('/test')
  def test():
      cache.set('name','小明', timeout=30)
      cache.set('person', {'name':'小明', 'age':18})
      x = cache.get('name')
      print(x)
      cache.set_many([('name1','小明'),('name2','老王')])
      print(cache.get_many("name1","name2"))
      print(cache.delete("name"))
      print(cache.delete_many("name1","name2"))
      return 'test'
  ```

  

- cache 对象的主要方法

  ```
  cache.cached：装饰器，装饰无参数函数，使得该函数结果可以缓存
      参数:
      timeout:超时时间
      key_prefix：设置该函数的标志
      unless：设置是否启用缓存，如果为True，不启用缓存
      forced_update：设置缓存是否实时更新，如果为True，无论是否过期都将更新缓存
      query_string：为True时，缓存键是先将参数排序然后哈希的结果
  
  cache.memoize：装饰器，装饰有参数函数，使得该函数结果可以缓存
  		make_name：设置函数的标志，如果没有就使用装饰的函数
  		# 其他参数同cached
  
  cache.delete_memoized：删除缓存
    参数：
    func_name：缓存函数的引用
    *args：函数参数
  
  cache.clear() # 清除缓存所有的缓存，这个操作需要慎重
  cache.
  	get(key)  #获取一个键的值，如果值是json格式会自动转化成字典
  	set(key,value,timeout)  #设置一个键值，value可以是字典，会自动转化json格式的字符串
  	add(key, value, timeout=None)  #设置一个键值,如果存在就pass，注意和set的区别
  	delete(key)  #删除键
  ```
