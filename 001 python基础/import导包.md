```
if __name == '__main':
	func1()
这个类似于C语言中的main一样，是一个函数的入口。
一个.py文件就构成一个module
python写的各个module都可以包含这样一个入口，在本moudle执行的时候，__name__就是__main__,在被导入的时候__name__就是module的名称。
所以这行代码可一保证我们的测试代码只在本module生效，而在被导入时并不执行
```

- __name__在模块中是代表module名，在类中代表类名，在方法中代表方法名

```
import导入的模块会保留自己的命名空间，这就是我们为什么需要使用模块名来访问它的函数或属性(`module.function`)
from module import xx 则要从另一个模块中将指定的函数和属性导入到自己的命名空间，所以我们可以直接访问它们(function)而不需要引用它们所来源的模块的原因
```

- python是按`LEGB` 原则来查找函数、变量等
  - L -Local 函数内的命名空间
  - E - Enclosing function locals 外部嵌套函数的命名空间
  - G -Global 全局变量,哈桑农户定义所在模块(文件)的命名空间
  - B -Builtin 内建模块
- 内建模块

```
当使用内建模块中函数或其他功能时，可以直接使用，不用添加内建模块的名字

但是，如果想要向内建模块添加一些功能，以便在任何函数中都能直接使用而不需要import ,这时，就要导入内建模块，在内建模块的命名空间(即__dict__字典属性)中添加该功能
builtin 是内建模块
builtins 是对内建模块的一个引用

说明在__main__中执行__builtin__就是__builtins__，它的type是一个module
说明在导入的情况下执行__builtins__是__builtin__.__dict__，他是一个字典

```

