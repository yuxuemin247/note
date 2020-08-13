#### pip安装包

- 安装pip

  ```
  wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz
  tar -zxvf pip-1.5.5.tar.gz
  cd pip-1.5.5
  python setup.py install
  ```

- 源码安装包

  ```
  1. 下载源码zip包
  2. 解压zip包(解压位置无限制)
  3. 进入要安装的虚拟环境(workon 虚拟环境名)
  4. 进入zip解压包中,执行python setup.py install
  ```

- 离线安装包

  ```
  pip install --no-index --find-links=/your_packages/  package_name  #安装单个包
  pip install --no-index --find-links=/your_packages/ -r requirements.txt   #批量离线安装包 
  ```

- 在线安装

  ```
  pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple    #-i   换源安装
  sudo python3 -m pip install xxx 
  ```

- pip换源

  - win下 cmd命令修改全局pip源

    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

  - Linux/Unix/Mac配置目录：~/.pip/pip.conf

    私有源使用：例如天眼源:http://pypi.skyeye.corp.qihoo.net/simple

    ```
    [global]
    trusted-host=pypi.skyeye.corp.qihoo.net
    index-url=http://pypi.skyeye.corp.qihoo.net/simple
    disable-pip-version-check = true
    timeout = 120
    ```

#### 错误总结

###### 1、win安装M2Crypto

- 错误提示

  error: Microsoft Visual C++ 9.0 is required.

- 要安装的库是c语言编写的，安装vc [地址](https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)

- 查看有无win版本，pip install M2CryptoWin32

###### 2、linux安装psycopg2

- 错误提示

  pg_config executable not found

- 先安装  yum install postgresql-devel*
- 再安装   pip install psycopg2-binary 

###### 3、linux安装psutil

- 错误提示

  include "Python.h"    compilation terminated.error: command 'gcc' failed with exit status 1

- yum install python-devel



