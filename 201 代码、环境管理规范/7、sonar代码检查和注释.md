## Pycharm接入sonarlint

### 1. sonar是什么

[SonarQube](https://www.sonarqube.org/) 是一款开源的代码质量检测工具，能够帮助你检查代码中的Bug、安全缺陷、不符合标准的代码。Sonar支持C++、Java、Python、Go、JavaScipt等多种语言，并且能够配合Jekins等工具进行持续集成、持续部署。

### 2. 从软件工程的角度看代码检测的意义

> **你总需要在一个环节上认真，这个环节越往前就越有效率，越往后你就越没效率**。要么你设计和编码认真点，不然，你就得在测试上认真点。要是你设计、编码、测试都不认真，那你就得在运维上认真，就得在处理故障上认真。你总需要在一个地方认真。
>
> ——[开发团队的效率](https://coolshell.cn/articles/11656.html)

一个完整的软件开发流程，大致可以分为这么几个阶段：设计——开发——测试——部署——交付——运维。在这 些阶段里，越靠后的阶段所付出的精力、成本越大。我们现在发现，一些比较早期开发的项目，出于种种原因，设计出的项目结构、写出的代码难以拓展，当后来需求变更、规模变大时，暴露出种种问题却难以维护。

这里暂且不对项目设计上作讨论，这个与项目背景、设计者的能力水平都有较强的关联。对于开发人员而言，sonar提供的代码规范检查、复杂度检查、测试覆盖率检查等功能，至少能帮助我们在**代码设计、开发、测试阶段**做得更细致些，降低后续工作的成本。

### 3. 如何使用

和许多产品一样，sonar也提供了社区版、企业版等产品。但对于个人开发而言，自己搭建一套sonar环境，再把代码提交进去进行检测也是一项不小的工程。我们可以借助一些插件，轻易地将sonar即成到我们的开发环境中。在这里介绍一下[SonarLint - Plugins | JetBrains](https://plugins.jetbrains.com/plugin/7973-sonarlint)这个插件，可以将sonar检测集成到Pycharm中。

#### 3.1 安装

Windows: File——Setting——Plugins——Market——搜索sonarlint——安装——重启PyCharm

Mac: Preference——Plugins——Market——搜索sonarlint——安装——重启PyCharm

#### 3.2 使用

##### 3.2.1 分析代码

成功安装后，在Pycharm的底栏会多出一个`SonarLint`的按钮，点击该按钮，会自动分析Pycharm当前打开的代码。

##### 3.2.2 查看分析详情

选中某条分析可以看到对应的**问题类型、问题描述、例子、解决方案等**。

双击某条分析可以自动**跳转**到代码位置

##### 3.2.3 Cognitive Complexity认知复杂度

SonarLint使用**认知复杂度**来度量代码的可维护性。SonarLint要求Cognitive Complexity在**15**以下。

循环、判断、嵌套，多个逻辑运算符等都会增加Cognitive Complexity。

点击分析结果的Location tab页，可以看出什么地方增加了复杂度。

像上面的代码是怎么可以达到285的认知复杂度的呢？

1. 代码太长，一个函数做了太多的事情
2. 嵌套过深。（我们可以横着来看我们的代码，如果你的代码有很多这种高低起伏的小山峰，那么很可能就是嵌套过多了。）

嵌套结构是增加认知复杂度的重要因素，过多嵌套会让我们的代码难以理解。毕竟

> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.

当SonarLint分析出我们代码Cognitive Complexity过高时，我们确实需要考虑我们的代码是否**做了太多的事**。有些判断是否能够**提前返回。**

## 注释(google风格)

#### 1、模块

首先是一行以句号, 问号或惊叹号结尾的概述(或者该文档字符串单纯只有一行).

接着是一个空行.

接着是文档字符串剩下的部分, 它应该与文档字符串的第一行的第一个引号对齐.

接着是一个空行

```
"""告警分析操作模块

包含：
1、受害者分析
2、攻击者分析
3、告警类型分析

"""
```

#### 2、函数和方法

一个函数必须要有文档字符串, 除非它满足以下条件:

1. 外部不可见
2. 非常短小
3. 简单明了

文档字符串应该包含函数做什么, 以及输入和输出的详细描述.通常, 不应该描述”怎么做”, 除非是一些复杂的算法.

文档字符串应该提供足够的信息, 当别人编写代码调用该函数时, 他不需要看一行代码, 只要看文档字符串就可以了.

对于复杂的代码, 在代码旁边加注释会比使用文档字符串更有意义.

关于函数的几个方面应该在特定的小节中进行描述记录， 这几个方面如下文所述.

每节应该以一个标题行开始. 标题行以冒号结尾. 除标题行外, 节的其他内容应被缩进4个空格.

Args:

  列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述太长超过了单行80字符（40个汉字）,使用4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar.

Returns: (或者 Yields: 用于生成器)

  描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.

Raises:

  列出与接口有关的所有异常.

```
@classmethod
def update_alarm_status(cls,field,ip,now_time，**kwargs):
    """更新告警状态
    
    Args:
        field:更新的字段
        ip:源IP
        now_time:当前时间
        **kwargs:
            is_update:是否更新数据库
            
    Returns:
        total: 更新成功的报警数目
    
    Raises:
        IOError:找不到文件时触发IO错误
    """
```

#### 3、类

类应该在其定义下有一个描述该类的文档字符串。如果你的类有公共属性(Attributes),那么文档中应该有一个属性(Attributes)段，并且应该遵守和函数相同的格式

```
Class SampleClass(object):
    """这是一个简单类
    
    longer class infomation
    longer class infomation
    
    Attributes:
        name : your name
        age  : your age 
    """
    
    def __init__(self,name,age):
        """ Inits SampleClass with blah"""
        self.name = name 
        self.age = age
        
    def public_method(self):
        """Performs Operation blah ""
```

#### 4、块注释和行注释

最需要写注释的是代码中那些技巧性的部分. 如果你在下次 [代码审查](http://en.wikipedia.org/wiki/Code_review) 的时候必须解释一下, 那么你应该现在就给它写注释. 对于复杂的操作, 应该在其操作开始前写上若干行注释. 对于不是一目了然的代码, 应在其行尾添加注释.

为了提高可读性, 注释应该至少离开代码2个空格.

另一方面, 绝不要描述代码. 假设阅读代码的人比你更懂Python, 他只是不知道你的代码要做什么.