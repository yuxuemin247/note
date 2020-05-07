##### 一、pyinstaller介绍

PyInstaller 将 [Python](http://c.biancheng.net/python/) 程序生成可直接运行的程序，这个程序就可以被分发到对应的 Windows 或 Mac OS X 平台上运行 。PyInstaller工具是跨平台的，它既可以在 Windows平台上使用，也可以在 Mac OS X 平台上运行。在不同的平台上使用 PyInstaller 工具的方法是一样的，它们支持的选项也是一样的。 

##### 二、pyinstaller使用

- 安装

  ```
  pip install pyinstaller
  ```

   强烈建议使用 pip 在线安装的方式来安装 PyInstaller 模块，不要使用离线包的方式来安装，因为 PyInstaller 模块还依赖其他模块，pip 在安装 PyInstaller 模块时会先安装它的依赖模块。

- 语法： pyinstaller  选项  Python  源文件 

  ```
  #下面先创建一个 app 目录，在该目录下创建一个 app.py 文件，文件中包含如下代码：
  
      from say_hello import *
      def main():
          print('程序开始执行')
      # 增加调用main()函数
      if __name__ == '__main__':
          main()
  
  #接下来使用命令行工具进入到此 app 目录下,cmd执行如下命令：
  pyinstaller -F app.py
  #当生成完成后，将会在此 app 目录下看到多了一个 dist 目录，并在该目录下看到有一个 app.exe 文件，这就是使用 PyInstaller 工具生成的 EXE 程序。
  #由于该程序没有图形用户界面，因此如果通过双击来运行该程序，则只能看到程序窗口一闪就消失了，这样将无法看到该程序的输出结果。
  ```

- | -h，--help                  | 查看该模块的帮助信息                                         |
  | --------------------------- | ------------------------------------------------------------ |
  | -F，-onefile                | 产生单个的可执行文件                                         |
  | -D，--onedir                | 产生一个目录（包含多个文件）作为可执行程序                   |
  | -a，--ascii                 | 不包含 Unicode 字符集支持                                    |
  | -d，--debug                 | 产生 debug 版本的可执行文件                                  |
  | -w，--windowed，--noconsolc | 指定程序运行时不显示命令行窗口（仅对 Windows 有效）          |
  | -c，--nowindowed，--console | 指定使用命令行窗口运行程序（仅对 Windows 有效）              |
  | -o DIR，--out=DIR           | 指定 spec 文件的生成目录。如果没有指定，则默认使用当前目录来生成 spec 文件 |
  | -p DIR，--path=DIR          | 设置 Python 导入模块的路径（和设置 PYTHONPATH 环境变量的作用相似）。也可使用路径分隔符（Windows 使用分号，[Linux](http://c.biancheng.net/linux_tutorial/) 使用冒号）来分隔多个路径 |
  | -n NAME，--name=NAME        | 指定项目（产生的 spec）名字。如果省略该选项，那么第一个脚本的主文件名将作为 spec 的名字 |