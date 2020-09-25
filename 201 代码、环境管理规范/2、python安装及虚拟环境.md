#### 1、python 安装

- linux

  1. 安装底层依赖库

     ```shell
     yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libdb4-devel libpcap-devel xz-devel libffi-devel
     ```

  2. 下载python源代码

     ```shell
     wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz
     ```

  3. 验证下载文件

     ```shell
     md5sum Python-3.7.6.tar.xz
     ```

  4. 解压缩和解归档

     ```shell
     xz -d Python-3.7.6.tar.xz
     tar -xvf Python-3.7.6.tar
     ```

  5. 执行安装前的配置(生成Makefile文件)

     ```shell
     cd Python-3.7.6
     ./configure --prefix=/root/env --enable-optimizations
     ```

     Configure脚本配置工具，它是autoconf的工具的基本应用。

     --prefix=/root/env    指定文件安装的位置

     --enable-optimizations 是优化选项(LTO，PGO 等)加上这个 flag 编译后，性能有 10% 左右的优化
     
  6. 构建和安装

     ```shell
     make && make install 
     ```

  7. 使用和pip

     ```
     /root/env/bin/python3 t1.py
     /root/env/bin/pip3 install xx
     ```

  8. 配置 PATH环境变量(用户或系统环境变量)并激活(非必要)

     ```
     vim ~/.bash_profile
     vim /etc/profile
     ```

     ```
     ... 此处省略上面的代码...
     
     export PATH=$PATH:/usr/local/python37/bin
     
     ... 此处省略下面的代码...
     ```

     ```
     source ~/.bash_profile
     source /etc/profile
     ```

  9. 注册软链接(非必要)

     ```
     ln -s  /root/env/bin/python3 /usr/bin/python3
     ```

     ln -s 源文件 目标文件

     ```
     python3 --version
     python  --version #测试Python环境是否更新成功（安装Python3一定不能破坏原来的Python2）。
     ```

  说明：如果需要清除之前的安装，就删除对应的文件和文件夹即可

#### 2、virtualenv使用

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

#### 3、Virtualenvwrapper使用

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

  