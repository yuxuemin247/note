日志管理快速入门：

 `Django` 使用 Python 内置的 [`logging`](https://docs.python.org/3/library/logging.html#module-logging) 模块处理系统日志。关于该模块的使用，Python 文档里有更详细的讨论。

日志框架的组成元素

一份Python logging配置有下面四个部分组成：

-  Loggers 记录器

- Handlers 处理器

- 过滤器

- Formatters 格式化器

  Loggers

  logger是日志系统的入口。每个logger都是命名了的bucket,消息写入bucket以便进一步处理

  logger可以配置日志级别。日志级别描述了由该logger处理的消息的严重性。

  每一个写入logger的消息都是一条日志记录。每一条日志记录也包含日志级别,代表对应信息的严重程度。日志记录还包含有用的元数据，来描述被记录了日志的事件细节。

   当 logger 确定了一条消息需要处理之后，会把它传给 *Handler*。 

  Handler 是决定如何处理 logger 中每一条消息的引擎。它描述特定的日志行为，比如把消息输出到屏幕、文件或网络 socket。

   一个 logger 可以有多个 handler，每一个 handler 可以有不同的日志级别。这样就可以根据消息的重要性不同，来提供不同格式的输出。例如，你可以添加一个 handler 把 `ERROR` 和 `CRITICAL` 消息发到寻呼机，再添加另一个 handler 把所有的消息（包括 `ERROR` 和 `CRITICAL` 消息）保存到文件里以便日后分析。 

   在日志记录从 logger 传到 handler 的过程中，使用 Filter 来做额外的控制。  程增加额外条件。例如，可以添加一个 filter 只允许某个特定来源的 `ERROR` 消息输出。 

   Filter 还被用来在日志输出之前对日志记录做修改。例如，可以写一个 filter，当满足一定条件时，把日志记录从 `ERROR` 降到 `WARNING` 级别。 

  Refused to apply style from 'because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.。

  ```
django setting.py 文件中配置,有几个默认的日志记录器,会自动记录
  # LOGGING = {
  ```
     'version': 1,
        是否禁用已经存在的日志器
       'disable_existing_loggers': False,
       日志格式化器
       'formatters': {
           'simple': {
               'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s: %(message)s',
              'datefmt': '%Y-%m-%d %H:%M:%S',
          },
           'verbose':{
               'format': '%(levelname)s %(filename)s[line:%(lineno)d] %(message)s',
              'datefmt': '%Y-%m-%d %H:%M:%S',
          }
       },
       # 日志过滤器
       # 日志处理器
       'handlers': {
           # 输出到文件(每周切割一次)
           'file1': {
               'class': 'logging.handlers.TimedRotatingFileHandler',
               'filename': 'error.log',
               'when': 'W0',
               'backupCount': 12,
               'formatter': 'simple',
               'level': 'WARNING',
           },
           # 'syslog':{
           #     'class':'logging.handlers.SysLogHandler',
           #     'address':('log.ab.local',514),
          #     'level':'DEBUG',
           #     'formatter':'verbose',
           # },
       },
       # 日志器记录器
       'loggers': {
           'django': {
               # 需要使用的日志处理器
               'handlers': ['file1'],
               # 是否向上传播日志信息
               'propagate': True,
               # 日志级别(不一定是最终的日志级别)
               'level': 'DEBUG',
           },
           # 'customer': {
           #     'handlers': ['syslog'],
           #     'propagata': True,
           #     'level': 'DEBUG'
           # },
           'django.db.backends':{
               'handlers':['file1'],
               'propagata':True,
               'level':'DEBUG'
           },
  
       }
   }

  ```
  
  

  ```
Internal Server Error  服务器挂掉了，或者启动失败没起来。
```

####  python的logging模块

- ​	 logging.basicConfig(**kwargs) 

```
  此函数，通过创建一个带有默认 Formatter 的StreamHandler处理器并将其添加到根日志记录器中来初始化基本配置。如果根日志记录器没有定义处理器，则debug(), info(), warning(), error() and critical() 会自动调用 basicConfig() 。
  如果根日志记录器已经配置了处理器，则此函数不起作用。
  ```

  ​	示例使用(不使用配置文件)

  ```
  def initlog(tag,level="DEBUG",console=False):
      syslogHander = SysLogHandler(address=('log.ab.ink',514))
      formatter = logging.Formatter(
      tag + ': %(levelname)s %(filename)s[line:%(lineno)d] %(message)s')
      syslogHander.formatter =formatter
      handlers = [syslogHander]
      if console:
          handlers.append(logging.StreamHandler())
          logging.basicConfig(
          level=level,
          format='%(asctime)s : %(levelname)s %(filename)s[line:%(lineno)d] %(message)s',
          datefmt='%Y-%m-%d %H:%M:%S',
          handlers=handlers)
          
  if __name__ == '__main__':
      initlog(tag='customer',console=True)
      logging.info('大家好')

