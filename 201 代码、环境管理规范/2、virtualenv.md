#### 1、virtualenv使用

- 使用豆瓣源安装 virtualenv
  pip install -i https://pypi.douban.com/simple virtualenv

- 创建一个名叫 env 的目录（虚拟环境），该目录下包含了独立的 Python 运行程序,以及 pip副本用于安装其他的 packge

  ```python
  virtualenv env
  virtualenv -p /usr/local/bin/python3 env   #指定python解释器
  ```

- 启动虚拟环境

  ```
  cd env
  source ./bin/activatesou
  ```

- 退出

  ```
  deactivate 
  #如果想删除虚拟环境，那么直接运行rm -rf env/
  ```

#### 2、Virtualenvwrapper使用

- 安装

  ```
  pip install -i https://pypi.douban.com/simple virtualenvwrapper-win
  ```

- 创建虚拟环境

  ```
  mkvirtualenv env
  mkvirtualenv env -p C:\python27\python.exe   #指定python 版本
  ```

- 进入虚拟环境

  ```
  workon env
  ```

- 退出虚拟环境

  ```
  deactivate
  rmvirtualenv env  #删除虚拟环境
  ```

  