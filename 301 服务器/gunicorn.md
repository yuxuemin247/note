- 安装

  pip install gunicorn

- 启动

  gunicorn run:app

- 配置参数

  ```
  gunicorn -w 2 -b 0.0.0.0:8000 run:app
  ```

  其中`-b 或 --bind` 指定项目启动绑定域名和端口，`-w 或 --workers` 指定启动几个进程

  ```
  gunicorn -b localhost:8000 -w 4 --threads 4 --max-requests 0 --timeout 30 wsgi:app  #国网项目
  ```

  