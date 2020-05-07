# 浏览器对象模型BOM



## 1. 浏览器对象模型介绍

BOM(Browser Object Model) 是指浏览器对象模型，是用于描述这种对象与对象之间层次关系的模型，浏览器对象模型提供了独立于内容的、可以与浏览器窗口进行互动的对象结构。BOM由多个对象组成，其中代表浏览器窗口的Window对象是BOM的顶层对象，其他对象都是该对象的子对象。

**BOM的左右**

* 弹出新浏览器窗口的能力；
* 移动、关闭和更改浏览器窗口大小的能力；
* 可提供WEB浏览器详细信息的导航对象；
* 可提供浏览器载入页面详细信息的本地对象；
* 可提供用户屏幕分辨率详细信息的屏幕对象；
* 支持Cookies；



## 2. 各对象详解

### 3.1 window

window对象是客户端JavaScript的全局对象
是所有客户端JavaScript特性和API的主要接入点
它表示Web浏览器的一个窗口或窗体,并且用标识符window来引用它

#### window 对象属性

| 属性            | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| **document**    | 对 Document 对象的只读引用。                                 |
| **history**     | 对 History 对象的只读引用。                                  |
| **location**    | 用于窗口或框架的 Location 对象。                             |
| **navigator**   | 对 Navigator 对象的只读引用。                                |
| **screen**      | 对 Screen 对象的只读引用。                                   |
| frames          | 返回窗口中所有命名的框架。该集合是 Window 对象的数组，每个 Window 对象在窗口中含有一个框架。 |
| length          | 设置或返回窗口中的框架数量。                                 |
| parent          | 返回父窗口。                                                 |
| top             | 返回最顶层的父窗口。                                         |
| name            | 设置或返回窗口的名称。                                       |
| opener          | 返回对创建此窗口的窗口的引用。                               |
| closed          | 返回窗口是否已被关闭。                                       |
| defaultStatus   | 设置或返回窗口状态栏中的默认文本。                           |
| status          | 设置窗口状态栏的文本。                                       |
| self            | 返回对当前窗口的引用。等价于 Window 属性。                   |
| **innerHeight** | 返回窗口的文档显示区的高度。                                 |
| **innerWidth**  | 返回窗口的文档显示区的宽度。                                 |
| **outerHeight** | 返回窗口的外部高度，包含工具条与滚动条。                     |
| **outerWidth**  | 返回窗口的外部宽度，包含工具条与滚动条。                     |
| pageXOffset     | 设置或返回当前页面相对于窗口显示区左上角的 X 位置。          |
| pageYOffset     | 设置或返回当前页面相对于窗口显示区左上角的 Y 位置。          |
| screenLeft      | 返回相对于屏幕窗口的x坐标                                    |
| screenTop       | 返回相对于屏幕窗口的y坐标                                    |
| screenX         | 返回相对于屏幕窗口的x坐标                                    |
| screenY         | 返回相对于屏幕窗口的y坐标                                    |

#### window对象方法

| 方法            | 描述                                               |
| --------------- | -------------------------------------------------- |
| **alert()**         | 显示带有一段消息和一个确认按钮的警告框。           |
| **confirm()**      | 显示带有一段消息以及确认按钮和取消按钮的对话框。   |
| **prompt()**        | 显示可提示用户输入的对话框。                       |
| focus()         | 把键盘焦点给予一个窗口。                           |
| blur()          | 把键盘焦点从顶层窗口移开。                         |
| **open()**      | 打开一个新的浏览器窗口或查找一个已命名的窗口。     |
| close()         | 关闭浏览器窗口。                                   |
| print()         | 打印当前窗口的内容。                               |
| createPopup()   | 创建一个 pop-up 窗口。                             |
| **setInterval()** | 按照指定的周期（以毫秒计）来调用函数或计算表达式。 |
| **setTimeout()** | 在指定的毫秒数后调用函数或计算表达式。             |
| **clearInterval()** | 取消由 setInterval() 设置的 timeout。              |
| **clearTimeout()** | 取消由 setTimeout() 方法设置的 timeout。           |
| moveBy()        | 可相对窗口的当前坐标把它移动指定的像素。(仅IE)     |
| moveTo()        | 把窗口的左上角移动到一个指定的坐标。（仅IE）      |
| resizeBy()      | 按照指定的像素调整窗口的大小。(仅IE)               |
| resizeTo()      | 把窗口的大小调整到指定的宽度和高度。(仅IE)         |
| scrollBy()      | 按照指定的像素值来滚动内容。                     |
| scrollTo()      | 把内容滚动到指定的坐标。                           |



### 3.2 Localtion

Location 对象包含有关当前 URL 的信息。

Location 对象是 window 对象的一部分，可通过 window.Location 属性对其进行访问。



#### Location 对象属性

| 属性     | 描述                          |
| -------- | ----------------------------- |
| href     | 返回完整的URL                 |
| protocol | 返回一个URL协议               |
| host     | 返回一个URL的主机名和端口     |
| hostname | 返回URL的主机名               |
| port     | 返回一个URL服务器使用的端口号 |
| pathname | 返回的URL路径名。             |
| search   | 返回一个URL的查询部分         |
| hash     | 返回一个URL的锚部分           |


#### Location 对象方法

| 方法       | 说明                   |
| ---------- | ---------------------- |
| assign()   | 载入一个新的文档       |
| reload()   | 重新载入当前文档       |
| replace()] | 用新的文档替换当前文档 |



### 3.3 History

History 对象包含用户（在浏览器窗口中）访问过的 URL。

History 对象是 window 对象的一部分，可通过 window.history 属性对其进行访问。

#### History 对象属性

| 属性   | 说明                   |
| ------ | ---------------------- |
| length | 返回历史列表中的网址数 |

#### History 对象方法

| 方法      | 说明                              |
| --------- | --------------------------------- |
| back()    | 加载 history 列表中的前一个 URL   |
| forward() | 加载 history 列表中的下一个 URL   |
| go()      | 加载 history 列表中的某个具体页面 |



### 3.4 Navigator

#### Navigator 对象属性

| 属性          | 说明                                        |
| ------------- | ------------------------------------------- |
| appCodeName   | 返回浏览器的代码名                          |
| appName       | 返回浏览器的名称                            |
| appVersion    | 返回浏览器的平台和版本信息                  |
| cookieEnabled | 返回指明浏览器中是否启用 cookie 的布尔值    |
| platform      | 返回运行浏览器的操作系统平台                |
| **userAgent** | 返回由客户机发送服务器的user-agent 头部的值 |

#### Navigator 对象方法

| 方法           | 描述                                      |
| -------------- | ----------------------------------------- |
| javaEnabled()  | 指定是否在浏览器中启用Java                |
| taintEnabled() | 规定浏览器是否启用数据污点(data tainting) |



### 3.5 Screen

Screen 对象包含有关客户端显示屏幕的信息。

#### Screen 对象属性

| 属性        | 说明                                     |
| ----------- | ---------------------------------------- |
| availHeight | 返回屏幕的高度（不包括Windows任务栏）    |
| availWidth  | 返回屏幕的宽度（不包括Windows任务栏）    |
| colorDepth  | 返回目标设备或缓冲器上的调色板的比特深度 |
| height      | 返回屏幕的总高度                         |
| pixelDepth  | 返回屏幕的颜色分辨率（每象素的位数）     |
| width       | 返回屏幕的总宽度                         |