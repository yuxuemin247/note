- cmd命令修改全局pip源

  ```
  pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
  ```

- pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple   

  -i   换源安装

- tesseract 光学识别 谷歌验证码识别的开山鼻祖,需要大量训练

  sudo python3 -m pip install -r  requirements.txt

- 安装包时报错:

  ```
   #include "Python.h"
                          ^
      compilation terminated.
      error: command 'gcc' failed with exit status 1
      在写Python代码的时候，需要用到psutil模块，需要安装。在安装psutil模块的时候出现的问题，重新安装了gcc等各种我能想到的，不过还是不行。网上说是其实安装一个对应的devel环境就可以了。 举个例子，这是我安装报错的信息：#include "Python.h"       ^compilation terminated.error: command 'gcc' failed with exit status 1其实只要看include缺什么就行了，我缺的时Python.h，所以就安装以下python的devel环境就好yum install python-devel其他同类问题同理，对应下载相应的devel环境。
  sudo python3 pip install django==2.0.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```
  
- python源码安装包

  ```
  1. 下载源码zip包
  2. 解压zip包(解压位置无限制)
  3. 进入要安装的虚拟环境(workon 虚拟环境名)
  4. 进入zip解压包中,执行python setup.py install
  ```

