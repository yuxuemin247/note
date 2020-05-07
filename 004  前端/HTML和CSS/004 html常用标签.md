# html常用标签

#### 1、无语义标签

```html
<div></div>
<span></span>
```

#### 2、常用语义标签

```html
<hn></hn> 几级标题 
<p></p> 段落
<pre></pre> 原文本
<br/> 换行
<hr/> 分割线
```

#### 3、文本标签

```html
<i></i> 斜体字
<em></em> 斜体字，表示强调
<b></b> 粗体字
<strong></strong> 粗体字，表示强调(语气更强) 
<del></del> 删除的文本
<ins></ins> 插入的文本
<sub></sub> 下标字
<sup></sup> 上标字
<ruby>
	拼音<rt>pinyin</rt>ying
</ruby> 中文注音，h5新增
```

#### 4、a标签

```html
<a href="https://www.baidu.com">前往百度</a>
<a href="./index.html">前往主页</a>
相对路径 :以当前文件作为参考，.代表当前路径，..代表上一级目录
```

- 常用属性

  title  --链接说明,悬浮会显示说明

  target  --目标位置  target属性规定在何处打开链接文档

```
target值描述
_blank在新窗口中打开被链接文档。
_self默认。在相同的框架中打开被链接文档。
_parent在父框架集中打开被链接文档。_top在整个窗口中打开被链接文档。
framename在指定的框架名中打开被链接文档。
```

- 其他用法

  前端移动页面中

  ```
  <a href="tel:10086">10086</a>
  ```

  - `mailto`邮件给...
  - tel 电话给...
  - `sms` 信息给...

- a标签的reset操作

  ```html
  a {
      color: #333;
      text-decoration: none;   标准文本显示(去掉默认的下划线)  blink 定义闪烁的文本
      cursor: pointer | wait | move  鼠标样式 pointer小手 wait转圈
  }
  ```

- 锚点

  ```html
  <a href="#tag">前往锚点</a> <a name="tag" des="锚点"></a>
  <a href="#tag">前往锚点</a> <i id="tag" des="锚点"></i>
  ```

#### 5、`img`标签

```html
<img src="https://image/icon.gif" alt="网不好，图片未加载出来" title="这是一张图片">
<img src="./icon.gif">
```

#### 6、list操作

- 有序列表

  ```
  <ol>
  	<li></li>
  	<li></li>
  <ol>
  ```

- 无序列表

  ```
  <ul>
  	<li></li>
  	<li><li>
  </ul>
  ```

- list的reset操作

  ```
  ol,ul {
   margin:0;
   padding:0;
   list-style:none;
  }
  ```

#### 6、其他标签

```html
<section></section> 块
<small></small> 小号字体
```

#### 标签的分类

##### 1、单|双标签

- 单标签：单标签在自身标签标识结束，主要应用为功能性标签
- 双标签：双标签有成对的结束标识，主要应用场景为内容性标签

##### 2、行|块标签

- 行标签：又名内联标签，内联标签自身不具备宽高，通常同行显示
- 块标签：又名块级标签，块标签拥有自身宽高，通常独自占据一行

##### 3、单一|组合标签

- 单一标签：单独出现，出现具体的功能或展示具体的内容
- 组合标签：配合使用，才能产生相应的内容和效果

div section article的区别
一个比一个更具有语义