

# HTML5/CSS3基础

## 1. HTML

### 1.1 什么是HTML

* HTML是用来制作网页的标记语言 
* HTML是Hypertext Markup Language的英文缩写,即超文本标记语言 
* HTML语言是一种标记语言,不需要编译,直接由浏览器执行 
* HTML文件是一个文本文件,包含了一些HTML元素,标签等
* HTML文件必须使用.html或.htm为文件名后缀 
* HTML是大小写不敏感的,HTML与html是一样的 
* HTML是由W3C的维护的 
* HTML 是通向 WEB 技术世界的钥匙。

### 1.2 发展历史

* HTML是从2.0版本开始的，实际上没有1.0的官方规范,在1993年6月作为互联网工程工作小组（IETF）工作草案发布（并非标准）
  HTML 2.0——1995年11月作为RFC 1866发布，在RFC 2854于2000年6月发布之后被宣布已经过时
* HTML 3.2——1997年1月14日，W3C推荐标准
* HTML 4.0——1997年12月18日，W3C推荐标准
* HTML 4.01（微小改进）——1999年12月24日，W3C推荐标准
* HTML 5——2014年10月28日，W3C推荐标准

### 1.3 HTML5的由来

* HTML5草案的前身名为 Web Applications 1.0，于2004年被WHATWG提出，于2007年被W3C接纳，并成立了新的 HTML 工作团队。
* HTML 5 的第一份正式草案已于2008年1月22日公布。HTML5 仍处于完善之中。然而，大部分现代浏览器已经具备了某些 HTML5 支持。
* 2012年12月17日，万维网联盟（W3C）正式宣布凝结了大量网络工作者心血的HTML5规范已经正式定稿。根据W3C的发言稿称：“HTML5是开放的Web网络平台的奠基石。”
* 2013年5月6日， HTML 5.1正式草案公布。该规范定义了第五次重大版本，第一次要修订万维网的核心语言：超文本标记语言（HTML）。在这个版本中，新功能不断推出，以帮助Web应用程序的作者，努力提高新元素互操作性。
* 2014年10月29日，万维网联盟宣布，经过接近8年的艰苦努力，该标准规范终于制定完成。

### 1.4 HTML5的优点

* 1、提高可用性和改进用户的友好体验；
* 2、有几个新的标签，这将有助于开发人员定义重要的内容；
* 3、可以给站点带来更多的多媒体元素\(视频和音频\)；
* 4、可以很好的替代FLASH和Silverlight；
* 5、当涉及到网站的抓取和索引的时候，对于SEO很友好；
* 6、将被大量应用于移动应用程序和游戏；
* 7、可移植性好。

### 1.5 HTML5的兼容性

* Internet Explorer 9 以及 以上版本
* chrome、Safari、opera、Firefox和各种以wekkit为内核的国产浏览器

### 附：相关组织

#### IETF\(The Internet Engineering Task Force\)

国际互联网工程任务组（The Internet Engineering Task Force，简称 IETF）  
互联网工程任务组，成立于1985年底，是全球互联网最具权威的技术标准化组织，主要任务是负责互联网相关技术规范的研发和制定，当前绝大多数国际互联网技术标准出自IETF。

#### W3C\(World Wide Web Consortium\)

万维网联盟\(World Wide Web Consortium\)  
万维网联盟创建于1994年，是Web技术领域最具权威和影响力的国际中立性技术标准机构。到目前为止，W3C已发布了200多项影响深远的Web技术标准及实施指南，如广为业界采用的超文本标记语言（标准通用标记语言下的一个应用）、可扩展标记语言（标准通用标记语言下的一个子集）以及帮助残障人士有效获得Web内容的信息无障碍指南（WCAG）等，有效促进了Web技术的互相兼容，对互联网技术的发展和应用起到了基础性和根本性的支撑作用。

### WHATWG\(Web Hypertext Application Technology Working Group\)

网页超文本应用技术工作小组是一个以推动网络HTML 5 标准为目的而成立的组织。  
在2004年，由Opera、Mozilla基金会和苹果这些浏览器厂商组成。

## 2 HTML基本语法

### 2.1 HTML标签

* 标签是HTML中最基本单位,也是最重要组成部分
* 通常要用两个角括号括起来:`<`和`>`
* 标签都是闭合的（两种形式：成对与不成对） 
* 双标签（成对）: `<标签名>内容</标签名>` 如：`<table></table>` 即分起始和结束
* 单标签（不成对）: `<标签名 />`;  如： `<br/>`、`<hr/>`
* 标签是大小写无关的,`<body>`;跟`<BODY>`表示意思是一样的，标准推荐使用小写，这样符合XHTML标准。
* 对于HTML标签来讲，最重要的是语义

### 2.2 HTML标签属性

* HTML属性一般都出现在HTML的开始标签中, 是HTML标签的一部分。
* 标签可以有属性,它包含了额外的信息.属性的值一定要在双引号中。
* 标签可以拥有多个属性。
* 属性由属性名和值成对出现。
* 语法格式如下：
  ```html
  <标签名 属性名1="属性值" 属性名2="属性值" ... 属性名N="属性值">
    <!– 输出内容…  -->
  </标签名>
  ```

### 2.3 HTML代码格式

任何回车或空格在源代码中都是不起作用，  
所以在编写HTML代码时，都可以使用回车或者空格进行代码排版，  
这样可以使代码清晰，也便于团队合作。必须保持严格的缩进规则，以`Tab`键为准。

### 2.4 HTML 注释

```html
<!-- 注释内容 -->
<!--
    这里全是注释
    都是注释
-->
```

### 2.5 HTML 实体 \(特殊字符\)

|  | 描述 | 实体名称 | 实体编号 |
| :--- | :--- | :--- | :--- |
|  | 空格 |  | &\#160; |
| &lt; | 小于号 | &lt; | &\#60; |
| &gt; | 大于号 | &gt; | &\#62; |
| & | 和号 | & | &\#38; |
| " | 引号 | " | &\#34; |
| ' | 撇号 | ' \(IE不支持\) | &\#39; |
| ￠ | 分（cent） | ¢ | &\#162; |
| £ | 镑（pound） | £ | &\#163; |
| ¥ | 元（yen） | ¥ | &\#165; |
| € | 欧元（euro） | € | &\#8364; |
| § | 小节 | § | &\#167; |
| © | 版权（copyright） | © | &\#169; |
| ® | 注册商标 | ® | &\#174; |
| ™ | 商标 | ™ | &\#8482; |
| × | 乘号 | × | &\#215; |
| ÷ | 除号 | ÷ | &\#247; |

## 3 HTML常用标签

### 3.1 文档声明

你可使用此声明在 Internet Explorer 6 及以后版本中切换为严格的标准兼容模式。

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!DOCTYPE html>
```

### 3.2 HTML主体结构标签

* `<html></html>` 此元素可告知浏览器其自身是一个 HTML 文档。
* `<head></head>` 用于定义文档的头部，它是所有头部元素的容器。`<head>` 中的元素可以引用脚本、指示浏览器在哪里找到样式表、提供元信息等等。
* `<body></doby>` 定义文档的主体    

### 3.3 HEAD头部标签

* `<title></title>`  定义文档标题
* `<base />`  标签为页面上的所有链接规定默认地址或默认目标
* `<meta />`  元素可提供有关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。`<meta>` 标签永远位于 head 元素内部。
  ```html
  <meta charset="utf-8">
  ```
* `<link></link>` 标签定义文档与外部资源的关系。

  ```html
  <link rel="stylesheet" type="text/css"  href="style.css"></link>
  <link rel="shortcut icon" type="images/x-icon" href="http://www.baidu.com/favicon.ico">
  ```

* `<style></style>`  签用于为 HTML 文档定义样式信息。

* `<script></script>`  标签用于定义客户端脚本，比如 JavaScript。script 元素既可以包含脚本语句，也可以通过 src 属性指向外部脚本文件。

  ```html
  <script type="text/javascript" src="script.js"></script>
  <script>
    alert('OK')
  </script>
  ```

### 3.4 meta元信息

* content  定义与 http-equiv 或 name 属性相关的元信息
* name 把content属性关联到一个名称

  ```
  author

  description

  keywords

  generator

  revised

  robots

  others
  ```

* http-equiv  把 content 属性关联到 HTTP 头部。

  ```
  content-type
  expires
  refresh
  set-cookie
  ```

* charset  字符集编码

```html
编码字符集
<meta charset="utf-8">  HTML5 支持 HTML5向下兼容
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> HTML 4支持

网页关键字：
<meta name="keywords" content="8-12个以英文逗号隔开的单词/词语">

网页描述信息
<meta name="description" content="80字以内的一段话，与网站内容相关">


<!--下面的内容，只需要了解。 自己看看-->
所有搜索引擎，抓取这个页面、爬行链接、禁止快照：  
<meta name="robots" content="index,follow,noarchive">
  all：文件将被检索，且页面上的链接可以被查询；
  none：文件将不被检索，且页面上的链接不可以被查询；
  index：文件将被检索；
  follow：页面上的链接可以被查询；
  noindex：文件将不被检索，但页面上的链接可以被查询；
  nofollow：文件将被检索，但页面上的链接不可以被查询；
  noarchive：文件将被检索，但禁止保存快照；

网页作者：
<meta name="author" content="obama">

网页网页生成工具 
<meta name="generator" content="Sublime Text3">

定义页面最新版本 
<meta name="revised" content="David, 2008/8/8/" />

网页版权信息：
<meta name="copyright" content="2009-2014©版权所有">

网页刷新信息：
<meta http-equiv="refresh" content="10;url=http://www.baidu.com">  10秒后跳转到百度页面
```

### 3.5 格式排版标签

* `<br/>`    换行标签，完成文字的紧凑显示。可以使用连续多个`<br/>`标签来换行
* `<hr/>`    水平分割线标签，用于段落与段落之间的分割
* `<p></p>`段落标签,里面可以加入文字,列表,表格等，可以&lt;p&gt;&lt;/p&gt;或&lt;p /&gt;使用
* `<pre></pre>`按原文显示标签，可以把原文件中的空格,回车,换行,tab键表现出来
* `<hn></hn>`    标题字标签，n为1-6，定义六级标题，而且会自动换行插入一个空行
* `<div></div>` 没有任何语义的标签

### 3.6 文本标签

* `<em></em>` 表示强调，通常为斜体字 
* `<strong></strong>` 表示强调\(语气更强\)，通常为粗体字 
* `<del></del>`  标签定义文档中已删除的文本。
* `<ins></ins>` 标签定义已经被插入文档中的文本
* `<sub></sub>`    文字下标字体标签
* `<sup></sup>`    文字上标字体标签
* `<mark></mark>`  **H5新增** 标签定义带有记号的文本 请在需要突出显示文本时使用,如搜索引擎搜索页面
* `<ruby></ruby>`  **H5新增** 标签定义 ruby 注释（中文注音或字符） 在东亚使用，显示的是东亚字符的发音。
* `<rt></rt>`  **H5新增** 标签定义字符（中文注音或字符）的解释或发音

```html
<!--一下文本标签  作为了解-->
<cite>    用于引证、举例、(标签定义作品（比如书籍、歌曲、电影、电视节目、绘画、雕塑等等）的标题)通常为斜体字
<dfn> 定义一个定义项目
<code> 定义计算机代码文本
<samp> 定义样式文本 标签并不经常使用。只有在要从正常的上下文中将某些短字符序列提取出来，对它们加以强调的极少情况下，才使用这个标签。
<kbd> 定义键盘文本。它表示文本是从键盘上键入的。它经常用在与计算机相关的文档或手册中。
<abbr> 定义缩写 配合title属性  (IE6以上)
<bdo>  来覆盖默认的文本方向 dir属性 值: lrt  rtl
<var> 定义变量。您可以将此标签与 <pre> 及 <code> 标签配合使用。
<small> 标签定义小型文本（和旁注）
<b>    粗体字标签 根据 HTML 5 的规范，<b> 标签应该做为最后的选择，只有在没有其他标记比较合适时才使用它。
<i>    斜体字标签 标签被用来表示科技术语、其他语种的成语俗语、想法、宇宙飞船的名字等等。
<u>    下划线字体标签 标签定义与常规文本风格不同的文本，像拼写错误的单词或者汉语中的专有名词。 请尽量避免使用 <u> 为文本加下划线，用户会把它混淆为一个超链接。
<q>  签定义一个短的引用。浏览器经常会在这种引用的周围插入引号。(小段文字)
<blockquote> 标签定义摘自另一个源的块引用。浏览器通常会对 <blockquote> 元素进行缩进。(大段文字) (块状元素)
<address>  定义地址 通常为斜体 (注意非通讯地址)  块状元素
<font>       H5已删除 字体标签，可以通过标签的属性指定文字的大小、颜色及字体等信息
<tt>       H5已删除 打字机文字
<big>       H5已删除 大型字体标签
<strike>   H5已删除 添加删除线
<acronym>  H5已删除 首字母缩写 请使用<abbr>代替
<bdi>      H5新增 标签允许您设置一段文本，使其脱离其父元素的文本方向设置。(经测试,各大浏览器都不起作用)
<mark>     H5新增 标签定义带有记号的文本 请在需要突出显示文本时使用,如搜索引擎搜索页面
<meter>    H5新增 定义预定义范围的度量
<progress> H5新增 标签标示任务的进度（进程）
<time>     H5新增 定义时间和日期 
<wbr>        H5新增    规定在文本中的何处适合添加换行符。Word Break Opportunity
```

## 4 CSS基础语法

### 4.1 使用方法

* 写在标签内的style属性中

  ```html
  <p style="color:red;"</p>
  ```

  写在&lt;style&gt; 元素中

  ```html
  <style>
      p {
          color:red
      }
  </style>
  ```

* 外部导入

  ```html
  <link rel="stylesheet" type="text/css" href="./style.css">
  ```

### 4.2 CSS格式组成

* 选择器     负责圈定范围，要修改的元素集合
     声明    由属性名和属性值组成，中间用冒号连接\(属性名:属性值\)，用于设定具体样式
* CSS由选择器和一或多个声明组成，多个声明之间用分号
  ```css
  选择器{
    属性名:属性值;
    属性名:属性值;
  }
  ```

### 4.3 CSS注释

```css
/*注释内容*/
```

### 4.4 CSS基本长度单位

* em 倍数 默认字体大小的倍数
* px：pixel，像素，屏幕上显示的最小单位，用于网页设计，直观方便；%
* 百分比
* pt：point，是一个标准的长度单位，1pt＝1/72英寸，用于印刷业，非常简单易用；
* cm 厘米
* mm 毫米

### 4.5 CSS基本颜色单位

* colorName 颜色名方式    red,green,blue...

  RGB十进制数字表示颜色

  ```
   数字（1-255） rgb(255,0,0)
   百分比(1-100) rgb(100%,0,0)
  ```

* RGB十六进制表示

  ```
   #rrggbb
   #rgb  简写
  ```

## 5 CSS选择器\(基础\)

* HTML元素选择器

  ```css
   div {

   }
  ```

* ID选择器

  ```css
   #idName {

   }
  ```

* CLASS选择器

  ```css
   .className {

   }
  ```

* 全局选择器

  ```css
   * {

   }
  ```

* 组合: 后代元素

  ```css
   选择器 选择器 {

   }
   .nav li {}
   #box div {}
   div .list {}
   .container li {}
  ```

* 组合：子元素

  ```css
   选择器>选择器 {

   }
   .nav>li {}
   #box>div {}
   div>.list {}
   .container>li {}
  ```

* 组合：群组选择器

  ```css
   选择器,选择器，选择器 {

   }

   body,ul,li,p,figure,table,.item,.list-item {

   }
  ```

* 组合：多选择器

  ```css
   div.item {

   }
   .item.list-item {

   }
   div#container {

   }
  ```

## 6 选择器优先级

```
计算 选择符 中ID的数量(=a)                    
计算 选择符 中 类选择器 属性选择器 伪类选择器 的数量(=b)    
计算选择符 中 标签选择器 伪对象选择器的数量 (=c)        
忽略全局选择器                            
a的权重100  b的权重10   c的权重1    相加
```

## 7 CSS常用属性和值

### 7.1 字体属性

* font

  ```css
  font:字体风格[字体加粗]<字体大小>[/行高]<字体族科>
  ```

* font-family    字体族科   宋体\|微软雅黑

  ```css
  font-family:"Arial","Helvetica",sans-serif;
  ```

* font-size            字体大小

* font-style       字体风格  normal \| italic \| oblique \(斜体\)

* font-weight    字体加粗  normal \| bold \| lighter

* font-variant    字体变形 normal \| small-caps

### 7.2 文字颜色

* color 设置文字颜色

### 7.3 文本属性

* letter-spacing    字母间隔  值为长度，可以是负值

* word-spacing    词的间距\(通过空格识别\)

* text-decoration    文字修饰

  ```
  underline
  overline
  line-through
  none(默认)
  ```

* text-align    横向排列 left \| right \| center

* vertical-align    垂直对其方式

  ```
  baseline： 将支持valign特性的对象的内容与基线对齐 
  sub： 垂直对齐文本的下标 
  super： 垂直对齐文本的上标 
  top： 将支持valign特性的对象的内容与对象顶端对齐 
  text-top： 将支持valign特性的对象的文本与对象顶端对齐 
  middle： 将支持valign特性的对象的内容与对象中部对齐 
  bottom： 将支持valign特性的对象的文本与对象底端对齐 
  text-bottom： 将支持valign特性的对象的文本与对象顶端对齐 
  <percentage>： 用百分比指定由基线算起的偏移量。可以为负值。基线对于百分数来说就是0%。 
  <length>： 用长度值指定由基线算起的偏移量。可以为负值。基线对于数值来说为0。（CSS2）
  ```

* text-indent    文本缩进  2em\(2个字\)   50px

* line-height    设置行间距离 不允许使用负值

* word-break 规定自动换行的处理方法

  ```
  normal        使用浏览器默认的换行规则。
  break-all    允许在单词内换行。
  keep-all    只能在半角空格或连字符处换行。
  ```

* word-wrap 允许长单词或URL地址换行到下一行

  ```
  normal        只在允许的断字点换行（浏览器保持默认处理）。
  break-word    在长单词或 URL 地址内部进行换行。
  ```

* overflow-wrap  **CSS3**中把word-wrap 改名为 overflow-wrap

* white-space

  ```
  normal：     默认处理方式。
  pre：        用等宽字体显示预先格式化的文本，不合并文字间的空白距离，当文字超出边界时不换行。可查阅pre对象
  nowrap：     强制在同一行内显示所有文本，合并文本间的多余空白，直到文本结束或者遭遇br对象。
  pre-wrap：   用等宽字体显示预先格式化的文本，不合并文字间的空白距离，当文字碰到边界时发生换行。
  pre-line：   保持文本的换行，不保留文字间的空白距离，当文字碰到边界时发生换行。
  ```

