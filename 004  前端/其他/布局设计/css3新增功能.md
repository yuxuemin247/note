# CSS3新增功能

## 1 CSS3选择器详解

### 1.1 基础选择器

* 通配选择器`*`
* 元素选择器`E`
* ID选择器`#id`
* CLASS选择器`.class`
* 群组选择器`select1,selectN`



### 1.2 层次选择器

* 后代选择器  `E F`
* 子选择器  `E>F`
* 相邻兄弟选择器  `E+F`
* 通用兄弟选择器  `E~F`



### 1.3 属性选择器

* `E[attr]`  选择具有att属性的E元素。 
* `E[attr="val"]`  选择具有att属性且属性值等于val的E元素。 
* `E[attr~="val"]`  选择具有att属性且属性值为一用空格分隔的字词列表，其中一个等于val的E元素（包含只有一个值且该值等于val的情况）。 
* `E[attr^="val"] ` 选择具有att属性且属性值为以val开头的字符串的E元素。
* `E[attr$="val"] `选择具有att属性且属性值为以val结尾的字符串的E元素。 
* `E[attr*="val"]` 选择具有att属性且属性值为包含val的字符串的E元素。 
* `E[attr|="val"]` 选择具有att属性且属性值为以val开头并用连接符"-"分隔的字符串的E元素，如果属性值仅为val，也将被选择。



### 1.4 伪类选择器

#### 动态伪类选择器

* `E:link`

		设置超链接a在未被访问前的样式。 
	注意，a:hover 必须位于 a:link 和 a:visited 之后，a:active 必须位于 a:hover 之后

* `E:visited`

		设置超链接a在其链接地址已被访问过时的样式。 

* `E:hover`

		设置元素在其鼠标悬停时的样式。 

* `E:active`

		设置元素在被用户激活（在鼠标点击与释放之间发生的事件）时的样式。

* `E:focus`

		设置对象在成为输入焦点（该对象的onfocus事件发生）时的样式。

#### 目标伪类选择器

* `E:target`

		匹配相关URL指向的E元素。 

#### 语言伪类选择器

* `E:lang(fr)`

		匹配使用特殊语言的E元素

#### UI元素伪类选择器

* `E:checked`

		匹配用户界面上处于选中状态的元素E。(用于input type为radio与checkbox时) 

* `E:enabled`

		匹配用户界面上处于可用状态的表单元素

* `E:disabled`

		匹配用户界面上处于禁用状态的表单元素

#### 结构伪类选择器

* `E:root`

		匹配E元素在文档的根元素。在HTML中，根元素永远是HTML 

* `E:first-child`

		匹配父元素的第一个子元素E。 

* `E:last-child`

		匹配父元素的最后一个子元素E。 

* `E:only-child`

		匹配父元素仅有的一个子元素E。

* `E:nth-child(n)`

		匹配父元素的第n个子元素E，假设该子元素不是E，则选择符无效。

* `E:nth-last-child(n)`

		匹配父元素的倒数第n个子元素E，假设该子元素不是E，则选择符无效。

* `E:first-of-type`

		匹配同类型中的第一个同级兄弟元素E

* `E:last-of-type`

		匹配同类型中的最后一个同级兄弟元素E

* `E:only-of-type`

		匹配同类型中的唯一的一个同级兄弟元素E

* `E:nth-of-type(n)`

		匹配同类型中的第n个同级兄弟元素E

* `E:nth-last-of-type(n)`

		匹配同类型中的倒数第n个同级兄弟元素E

* `E:empty`

		匹配没有任何子元素（包括text节点）的元素E

#### 否定伪类选择器

* `E:not(s)`

		匹配不含有s选择符的元素E



### 1.5 伪元素选择器

* `E:first-letter/E::first-letter`

		设置对象内的第一个字符的样式。 

* `E:first-line/E::first-line` 

		设置对象内的第一行的样式。

* `E:before/E::before` 

		设置在对象前（依据对象树的逻辑结构）发生的内容。用来和content属性一起使用

* `E:after/E::after`

		设置在对象后（依据对象树的逻辑结构）发生的内容。用来和content属性一起使用

* `E::placeholder` 

		设置对象文字占位符的样式。 

* `E::selection` 

		设置对象被选择时的样式。 





## 2 CSS3 基本功能

### 2.1 CSS3新增长度单位

* rem  **相对于根元素(即html元素)font-size计算值的倍数**
* vm  **视口被均分为100单位的vw**
* vh  **视口被均分为100单位的vh**
* vmax **相对于视口的宽度或高度中较大的那个。其中最大的那个被均分为100单位的vmax**
* vmin **相对于视口的宽度或高度中较小的那个。其中最小的那个被均分为100单位的vmin**

### 2.2 CSS3新增颜色单位

* RGBA(R,G,B,A)    A：Alpha透明度。取值0~1之间。

* HSL(H,S,L)   

  > H:  Hue(色调)。0(或360)表示红色，120表示绿色，240表示蓝色，也可取其他数值来指定颜色。取值为：0 - 360
  >
  > S：Saturation(饱和度)。取值为：0.0% - 100.0%
  >
  > L：Lightness(亮度)。取值为：0.0% - 100.0%

* HSLA(H,S,L,A)

### 2.3 CSS3渐变(了解)

#### 线性渐变

**语法**

```
<linear-gradient> = linear-gradient([ [ <angle> | to <side-or-corner> ] ,]? <color-stop>[, <color-stop>]+)

<side-or-corner> = [left | right] || [top | bottom]

<color-stop> = <color> [ <length> | <percentage> ]?
```

**取值**

```
<angle>：用角度值指定渐变的方向（或角度）。
	to left： 设置渐变为从右到左。相当于: 270deg
	to right：设置渐变从左到右。相当于: 90deg
	to top：  设置渐变从下到上。相当于: 0deg
	to bottom： 设置渐变从上到下。相当于: 180deg。这是默认值，等同于留空不写。
<color-stop> 用于指定渐变的起止颜色：
	<color>：  指定颜色。
	<length>： 用长度值指定起止色位置。不允许负值
	<percentage>： 用百分比指定起止色位置。
```

**示例**

```css
linear-gradient(#fff, #333);
linear-gradient(to bottom, #fff, #333);
linear-gradient(to top, #333, #fff);
linear-gradient(180deg, #fff, #333);
linear-gradient(to bottom, #fff 0%, #333 100%);
```

#### 径向渐变

**语法**

```
<radial-gradient> = radial-gradient([ [ <shape> || <size> ] [ at <position> ]? , | at <position>, ]?<color-stop>[ , <color-stop> ]+)

<position> = [ <length>① | <percentage>① | left | center① | right ]? [ <length>② | <percentage>② | top | center② | bottom ]?

<shape> = circle | ellipse

<size> = <extent-keyword> | [ <circle-size> || <ellipse-size> ]

<extent-keyword> = closest-side | closest-corner | farthest-side | farthest-corner

<circle-size> = <length>

<ellipse-size> = [ <length> | <percentage> ]{2}

<shape-size> = <length> | <percentage>

<color-stop> = <color> [ <length> | <percentage> ]?
```

**取值**

```
<position> 确定圆心的位置。如果提供2个参数，第一个表示横坐标，第二个表示纵坐标；如果只提供一个，第二值默认为50%，即center
	<percentage>①：用百分比指定径向渐变圆心的横坐标值。可以为负值。
	<length>①：用长度值指定径向渐变圆心的横坐标值。可以为负值。
	left：设置左边为径向渐变圆心的横坐标值。
	center①：设置中间为径向渐变圆心的横坐标值。
	right：设置右边为径向渐变圆心的横坐标值。
	<percentage>②：用百分比指定径向渐变圆心的纵坐标值。可以为负值。
	<length>②：用长度值指定径向渐变圆心的纵坐标值。可以为负值。
	top：设置顶部为径向渐变圆心的纵坐标值。
	center②：设置中间为径向渐变圆心的纵坐标值。
	bottom：设置底部为径向渐变圆心的纵坐标值。

<shape> 确定圆的类型
	circle：指定圆形的径向渐变
	ellipse：指定椭圆形的径向渐变。

<extent-keyword> circle | ellipse 都接受该值作为 size
	closest-side：指定径向渐变的半径长度为从圆心到离圆心最近的边
	closest-corner：指定径向渐变的半径长度为从圆心到离圆心最近的角
	farthest-side：指定径向渐变的半径长度为从圆心到离圆心最远的边
	farthest-corner：指定径向渐变的半径长度为从圆心到离圆心最远的角

<circle-size> circle 接受该值作为 size
	<length>：用长度值指定正圆径向渐变的半径长度。不允许负值。

<ellipse-size> ellipse 接受该值作为 size
	<length>：用长度值指定椭圆径向渐变的横向或纵向半径长度。不允许负值。
	<percentage>：用百分比指定椭圆径向渐变的横向或纵向半径长度。不允许负值。

<color-stop> 用于指定渐变的起止颜色：
	<color>：指定颜色。
	<length>：用长度值指定起止色位置。不允许负值
	<percentage>：用百分比指定起止色位置。不允许负值
```

**示例**

```css
radial-gradient(circle, #f00, #ff0, #080);
radial-gradient(circle at center, #f00, #ff0, #080);
radial-gradient(circle at 50%, #f00, #ff0, #080);
radial-gradient(circle farthest-corner, #f00, #ff0, #080);
```



## 3 CSS3 新增基本属性

### 3.1 布局相关属性

* box-sizing	定义盒子模型的尺寸解析方式
  ```
  >content-box(默认)	
  >border-box		
  ```
* resize	否允许用户缩放，调节元素尺寸大小
  ```
  none： 不允许用户调整元素大小。 (默认)
  both： 用户可以调节元素的宽度和高度。 
  horizontal： 用户可以调节元素的宽度 	
  vertical： 用户可以调节元素的高度。 	
  ```
* display	盒子是否以及如何显示
  ```
  > none： 隐藏对象。与visibility属性的hidden值不同，其不为被隐藏的对象保留其物理空间 
  > inline： 指定对象为内联元素。 
  > block： 指定对象为块元素。 
  > list-item： 指定对象为列表项目。 
  > inline-block： 指定对象为内联块元素。（CSS2） 
  > table： 指定对象作为块元素级的表格。类同于html标签<table>（CSS2） 
  > inline-table： 指定对象作为内联元素级的表格。类同于html标签<table>（CSS2） 
  > table-caption： 指定对象作为表格标题。类同于html标签<caption>（CSS2） 
  > table-cell： 指定对象作为表格单元格。类同于html标签<td>（CSS2） 
  > table-row： 指定对象作为表格行。类同于html标签<tr>（CSS2） 
  > table-row-group： 指定对象作为表格行组。类同于html标签<tbody>（CSS2） 
  > table-column： 指定对象作为表格列。类同于html标签<col>（CSS2） 
  > table-column-group： 指定对象作为表格列组显示。类同于html标签<colgroup>（CSS2） 
  > table-header-group： 指定对象作为表格标题组。类同于html标签<thead>（CSS2） 
  > table-footer-group： 指定对象作为表格脚注组。类同于html标签<tfoot>（CSS2）
  > run-in： 根据上下文决定对象是内联对象还是块级对象。（CSS3） 
  > box： 将对象作为弹性伸缩盒显示。（伸缩盒最老版本）（CSS3） 
  > inline-box： 将对象作为内联块级弹性伸缩盒显示。（伸缩盒最老版本）（CSS3） 
  > flexbox： 将对象作为弹性伸缩盒显示。（伸缩盒过渡版本）（CSS3） 
  > inline-flexbox： 将对象作为内联块级弹性伸缩盒显示。（伸缩盒过渡版本）（CSS3） 
  > flex： 将对象作为弹性伸缩盒显示。（伸缩盒最新版本）（CSS3） 
  > inline-flex： 将对象作为内联块级弹性伸缩盒显示。（伸缩盒最新版本）（CSS3） 
  ```
	​		

### 3.2 外轮廓

- outline	给元素周围绘制一条轮廓线

  ```css
  <' outline-width '> || <' outline-style '> || <' outline-color '>
  ```

- outline-width  外廓线宽度

  > <length>： 用长度值来定义轮廓的厚度。不允许负值 
  > medium： 定义默认宽度的轮廓。 
  > thin： 定义比默认宽度细的轮廓。 
  > thick： 定义比默认宽度粗的轮廓。 	

- outline-style	外廓线风格

  > none： 无轮廓。与任何指定的 <' outline-width '> 值无关 
  > dotted： 点状轮廓。 
  > dashed： 虚线轮廓。 
  > solid： 实线轮廓 
  > double： 双线轮廓。两条单线与其间隔的和等于指定的 <' outline-width '> 值 
  > groove： 3D凹槽轮廓。 
  > ridge： 3D凸槽轮廓。 
  > inset： 3D凹边轮廓。 
  > outset： 3D凸边轮廓。 	

- outline-color	  外廓线颜色
- outline-offset  外廓线的偏移量



### 3.3 颜色

* opacity  检索或设置对象的不透明度。  对于尚不支持opacity属性的IE浏览器可以使用IE私有的滤镜属性来实现与opacity相同的效果 





## 4 CSS3新增边框和背景属性

### 4.1 边框圆角

* border-radius			

  > 设置或检索对象使用圆角边框。提供2个参数，2个参数以“/”分隔，每个参数允许设置1~4个参数值，第1个参数表示水平半径，第2个参数表示垂直半径，如第2个参数省略，则默认等于第1个参数 
  > 水平半径：如果提供全部四个参数值，将按上左(top-left)、上右(top-right)、下右(bottom-right)、下左(bottom-left)的顺序作用于四个角。 
  > 如果只提供一个，将用于全部的于四个角。 
  > 如果提供两个，第一个用于上左(top-left)、下右(bottom-right)，第二个用于上右(top-right)、下左(bottom-left)。 
  > 如果提供三个，第一个用于上左(top-left)，第二个用于上右(top-right)、下左(bottom-left)，第三个用于下右(bottom-right)。 
  >
  > 垂直半径也遵循以上4点。 

* border-top-left-radius		设置或检索对象的左上角圆角边框

* border-top-right-radius	设置或检索对象的右上角圆角边框

* border-bottom-right-radius	设置或检索对象的右下角圆角边框

* border-bottom-left-radius	   设置或检索对象的左下角圆角边框



### 4.2 盒子阴影

* box-shadow	设置元素的阴影

  > 值: none | <shadow> [ , <shadow> ]*			
  > <shadow> = inset? && <length>{2,4} && <color>?	
  >
  > 取值：
  >
  > ​	none： 无阴影 
  > 	<length>①： 第1个长度值用来设置对象的阴影水平偏移值。可以为负值 
  > 	<length>②： 第2个长度值用来设置对象的阴影垂直偏移值。可以为负值 
  > 	<length>③： 如果提供了第3个长度值则用来设置对象的阴影模糊值。不允许负值 
  > 	<length>④： 如果提供了第4个长度值则用来设置对象的阴影外延值。可以为负值 
  > 	<color>： 设置对象的阴影的颜色。 
  > 	inset： 设置对象的阴影类型为内阴影。该值为空时，则对象的阴影类型为外阴影 

  可以设定多组效果，每组参数值以逗号分隔						

  ``` css
  test .outset {
  	box-shadow: 5px 5px rgba(0, 0, 0, .6);
  }
  .test .outset-blur {
  	box-shadow: 5px 5px 5px rgba(0, 0, 0, .6);
  }
  .test .outset-extension {
  	box-shadow: 5px 5px 5px 10px rgba(0, 0, 0, .6);
  }
  .test .inset {
  	box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, .6) inset;
  }
  .test .multiple-shadow {
  	box-shadow:
  		0 0 5px 3px rgba(255, 0, 0, .6),
  		0 0 5px 6px rgba(0, 182, 0, .6),
  		0 0 5px 10px rgba(255, 255, 0, .6);
  }	
  ```

* box-reflect   倒影  （仅webkit  了解）

  > 值: box-reflect：none | <direction> <offset>? <mask-box-image>?
  >
  > 取值：
  >
  > direction		
  > 	above： 指定倒影在对象的上边 
  > 	below： 指定倒影在对象的下边 
  > 	left： 指定倒影在对象的左边 
  > 	right： 指定倒影在对象的右边 
  > offset			
  > 	<length>： 用长度值来定义倒影与对象之间的间隔。可以为负值 
  > 	<percentage>： 用百分比来定义倒影与对象之间的间隔。可以为负值 
  > mask-box-image	
  > 	none： 无遮罩图像 
  > 	<url>： 使用绝对或相对地址指定遮罩图像。 
  > 	<linear-gradient>： 使用线性渐变创建遮罩图像。 
  > 	<radial-gradient>： 使用径向(放射性)渐变创建遮罩图像。 
  > 	<repeating-linear-gradient>： 使用重复的线性渐变创建背遮罩像。 
  > 	<repeating-radial-gradient>： 使用重复的径向(放射性)渐变创建遮罩图像。 

### 4.3 CSS3新增背景属性

```css
background: bg-image bg-position / bg-size bg-repeat bg-attachment bg-origin bg-clip bg-color
```

* background-origin  背景图片原点

  ```
  取值：
  padding-box：(默认值) 从padding区域（含padding）开始显示背景图像。 
  border-box： 从border区域（含border）开始显示背景图像。 
  content-box： 从content区域开始显示背景图像。
  ``` 

* backgroun-clip   指定对象的背景图像向外裁剪的区域。  
  ```
  取值：
  padding-box： 从padding区域（不含padding）开始向外裁剪背景。 
  border-box： (默认值)从border区域（不含border）开始向外裁剪背景。 
  content-box： 从content区域开始向外裁剪背景。 
  text： 从前景内容的形状（比如文字）作为裁剪区域向外裁剪，如此即可实现使用背景作为填充色之类的遮罩效果
  ```

* background-size  背景图像的尺寸
  ```
  <length>： 用长度值指定背景图像大小。不允许负值。 
  <percentage>： 用百分比指定背景图像大小。不允许负值。 
  auto： 背景图像的真实大小。 
  cover： 将背景图像等比缩放到完全覆盖容器，背景图像有可能超出容器。 
  contain： 将背景图像等比缩放到宽度或高度与容器的宽度或高度相等，背景图像始终被包含在容器内。 
  ```

* CSS3多背景

  ```css
  background:url(test1.jpg) no-repeat scroll 10px 20px/50px 60px content-box padding-box,
  	   	   url(test1.jpg) no-repeat scroll 10px 20px/70px 90px content-box padding-box,
  	       url(test1.jpg) no-repeat scroll 10px 20px/110px 130px content-box padding-box #aaa;
  ```

  

### 4.4 CSS3边框图片(了解)

* border-image	
  ```
  border-image：<' border-image-source '> || <' border-image-slice '> [ / <' border-image-width '> | / <' border-image-width '>? / <' border-image-outset '> ]? || <' border-image-repeat '
  
  复合属性。设置或检索对象的边框样式使用图像来填充。  
  ```

* border-image-source	设置或检索对象的边框样式使用图像路径。 值: url

* border-image-slice	设置或检索对象的边框背景图的分割方式。 值: 浮点数/百分比

* border-image-width	设置或检索对象的边框厚度。值: 长度值/百分比/浮点数

* border-image-outset   设置或检索对象的边框背景图的扩展   值: 长度值/浮点数

* border-image-repeat   设置或检索对象的边框图像的平铺方式。 
  ```
  值:
  stretch： 指定用拉伸方式来填充边框背景图。 
  repeat： 指定用平铺方式来填充边框背景图。当图片碰到边界时，如果超过则被截断。 
  round： 指定用平铺方式来填充边框背景图。图片会根据边框的尺寸动态调整图片的大小直至正好可以铺满整个边框。 
  space： 指定用平铺方式来填充边框背景图。图片会根据边框的尺寸动态调整图片的之间的间距直至正好可以铺满整个边框。 	
  ```



## 5 CSS3变换/过渡/动画

### 5.1 变换(transform)

#### 相关属性

* transform		

  > 设置或检索对象的转换。 
  >
  > 取值
  >
  > none  (默认值)无转换
  >
  > 2D Transform Functions：
  > 	matrix()： 以一个含六值的(a,b,c,d,e,f)变换矩阵的形式指定一个2D变换，相当于直接应用一个[a,b,c,d,e,f]变换矩阵 
  > 	translate()： 指定对象的2D translation（2D平移）。第一个参数对应X轴，第二个参数对应Y轴。如果第二个参数未提供，则默认值为0 
  > 	translatex()： 指定对象X轴（水平方向）的平移 
  > 	translatey()： 指定对象Y轴（垂直方向）的平移 
  > 	rotate()： 指定对象的2D rotation（2D旋转），需先有 <' transform-origin '> 属性的定义 
  > 	scale()： 指定对象的2D scale（2D缩放）。第一个参数对应X轴，第二个参数对应Y轴。如果第二个参数未提供，则默认取第一个参数的值 
  > 	scalex()： 指定对象X轴的（水平方向）缩放 
  > 	scaley()： 指定对象Y轴的（垂直方向）缩放 
  > 	skew()： 指定对象skew transformation（斜切扭曲）。第一个参数对应X轴，第二个参数对应Y轴。如果第二个参数未提供，则默认值为0 
  > 	skewx()： 指定对象X轴的（水平方向）扭曲 
  > 	skewy()： 指定对象Y轴的（垂直方向）扭曲 
  >
  > 3D Transform Functions：
  > 	matrix3d()： 以一个4x4矩阵的形式指定一个3D变换 
  > 	translate3d()： 指定对象的3D位移。第1个参数对应X轴，第2个参数对应Y轴，第3个参数对应Z轴，参数不允许省略 
  > 	translatez()： 指定对象Z轴的平移 
  > 	rotate3d()： 指定对象的3D旋转角度，其中前3个参数分别表示旋转的方向x,y,z，第4个参数表示旋转的角度，参数不允许省略 
  > 	rotatex()： 指定对象在x轴上的旋转角度 
  > 	rotatey()： 指定对象在y轴上的旋转角度 
  > 	rotatez()： 指定对象在z轴上的旋转角度 
  > 	scale3d()： 指定对象的3D缩放。第1个参数对应X轴，第2个参数对应Y轴，第3个参数对应Z轴，参数不允许省略 
  > 	scalez()： 指定对象的z轴缩放 
  > 	perspective()： 指定透视距离 	



* transform-origin	

  > 设置或检索对象以某个原点进行转换。 
  > 用法
  > 	如果提供两个值，第一个用于横坐标，第二个用于纵坐标。 
  > 	如果只提供一个，该值将用于横坐标；纵坐标将默认为50%。 
  > 	3D变形需要制定Z坐标 第三个参数值
  > 取值
  > 	left  right  center   <lenght>  <percentage>
  > 	top bottom  center   <lenght>  <percentage>	

* transform-style	

  > 指定某元素的子元素是（看起来）位于三维空间内，还是在该元素所在的平面内被扁平化。 
  > flat： (默认)指定子元素位于此元素所在平面内 
  > preserve-3d： 指定子元素定位在三维空间内 

* perspective

  > 指定观察者与「z=0」平面的距离，使具有三维位置变换的元素产生透视效果。「z>0」的三维元素比正常大，而「z<0」时则比正常小，大小程度由该属性的值决定。 
  >
  > none： 不指定透视 
  > <length>： 指定观察者距离「z=0」平面的距离，为元素及其内容应用透视变换。不允许负值 

* perspective-origin

  > 设置透视点的位置
  >
  > 用法 
  >
  > ​	该属性提供2个参数值。 
  > 	如果提供两个，第一个用于横坐标，第二个用于纵坐标。 
  > 	如果只提供一个，该值将用于横坐标；纵坐标将默认为center。 
  > 取值
  > 	left  right  center   <lenght>  <percentage>
  > 	top bottom  center   <lenght>  <percentage>	

* backface-visibility	

  > 指定元素背面面向用户时是否可见。
  > 决定一个元素背面面向用户时是否可见，需要直接在该元素上定义 <' backface-visibility '> 属性，而不能在其父元素上，因为该属性默认为不可继承。 
  > 取值
  > 	visible： (默认)指定元素背面可见，允许显示正面的镜像。 
  > 	hidden： 指定元素背面不可见 

#### 2D变换

##### 2D位移

* translate(x, y)	
* translatex()	
* translatey()	

##### 2D缩放

* scale(x, y)	
* scalex()		
* scaley()		

##### 2D旋转

* rotate(deg)	

##### 2D倾斜

* skew(x,y)	
* skewx()		
* skewy()		

##### 2D矩阵

* matrix()	

#### 3D变换

##### 3D位移	

* translate3d(x, y, z)
* translatez()

##### 3D缩放	

* scale3d()
* scalez()

##### 3D旋转	

* rotate3d(x, y, z, a)
* rotatex()
* rotatey()
* rotatex()

##### 3D矩阵

* matrix3d()

##### 多重变形

```css
-webkit-transform:translate(-50%, -50%) rotate(45deg);
-moz-transform:translate(-50%, -50%) rotate(45deg);
-ms-transform:translate(-50%, -50%) rotate(45deg);
-o-transform:translate(-50%, -50%) rotate(45deg);
transform:translate(-50%, -50%) rotate(45deg);
```



### 5.2 过渡(transition)

#### 过渡相关属性

* transition	检索或设置对象变换时的过渡。

  > 注意：
  >
  > 如果只提供一个<time>参数，则为 <' transition-duration '> 的值定义；如果提供二个<time>参数，则第一个为 <' transition-duration '> 的值定义，第二个为 <' transition-delay '> 的值定义 
  >
  > 用法
  > transition：<single-transition>[,<single-transition>]*<single-transition> = [ none | <single-transition-property> ] || <time> || <single-transition-timing-function> || <time>

* transition-property	 设置对象中的参与过渡的属性

  > 默认值为：all。默认为所有可以进行过渡的css属性。 
  > 如果提供多个属性值，以逗号进行分隔。 
  > 取值				
  > 	none： 不指定过渡的css属性 
  > 	all： 所有可以进行过渡的css属性 
  > 	<IDENT>： 指定要进行过渡的css属性 
  > 那些CSS属性可以被过渡		
  > 	颜色属性
  > 	具有长度值 百分比的属性
  > 	值是数字的属性 如 z-index  opacity  outline-offset等
  > 	变形系列属性
  > 	阴影
  > 	渐变		

* transition-duration	设置对象过渡的持续时间		

  如果提供多个属性值，以逗号进行分隔。

* transition-timing-function   设置对象中过渡的动画类型	

  > 取值				
  > ease： 平滑过渡。等同于贝塞尔曲线(0.25, 0.1, 0.25, 1.0) 
  > linear： 线性过渡。等同于贝塞尔曲线(0.0, 0.0, 1.0, 1.0) 
  > ease-in： 由慢到快。等同于贝塞尔曲线(0.42, 0, 1.0, 1.0) 
  > ease-out： 由快到慢。等同于贝塞尔曲线(0, 0, 0.58, 1.0) 
  > ease-in-out： 由慢到快再到慢。等同于贝塞尔曲线(0.42, 0, 0.58, 1.0) 
  > cubic-bezier(<number>, <number>, <number>, <number>)： 特定的贝塞尔曲线类型，4个数值需在[0, 1]区间内 http://cubic-bezier.com/
  > steps(<integer>[, [ start | end ] ]?)： 接受两个参数的步进函数。第一个参数必须为正整数，指定函数的步数。第二个参数取值可以是start或end，指定每一步的值发生变化的时间点。第二个参数是可选的，默认值为end。 

*  transition-delay	设置对象延迟过渡的时间

#### CSS3触发过渡的条件

* 伪元素触发			
* 媒体查询			 
* JavaScript触发			



### 5.3 动画

#### 关键帧

帧——就是动画中最小单位的单幅影像画面，相当于电影胶片上的每一格镜头。

#### 关键帧语法

> @keyframes <identifier> { <keyframes-blocks> }
> <keyframes-blocks>：[ [ from | to | <percentage> ]{ sRules } ][ [ , from | to | ]{ sRules } ]*

```css
@keyframes testanimations {
	from { opacity: 1; }
	to { opacity: 0; }
}

@keyframes testanimations {
	from { transform: translate(0, 0); }
	20% { transform: translate(20px, 20px); }
	40% { transform: translate(40px, 0); }
	60% { transform: translate(60px, 20); }
	80% { transform: translate(80px, 0); }
	to { transform: translate(100px, 20px); }
}

@keyframes testanimations{
	0% { transform: translate(0, 0); }
	20% { transform: translate(20px, 20px); }
	40% { transform: translate(40px, 0); }
	60% { transform: translate(60px, 20px); }
	80% { transform: translate(80px, 0); }
	100% { transform: translate(100px, 20px); }
}
```

#### 相关属性

* animation	设置对象所应用的动画特效

  > 如果提供多组属性值，以逗号进行分隔。 
  >
  > 注意：如果只提供一个<time>参数，则为 <' animation-duration '> 的值定义；如果提供二个<time>参数，则第一个为 <' animation-duration '> 的值定义，第二个为 <' animation-delay '> 的值定义 
  >
  > 用法
  > 	animation： <single-animation-name> || <time> || <single-animation-timing-function> || <time> || <single-animation-iteration-count> || <single-animation-direction> || <single-animation-fill-mode> || <single-animation-play-state>	

* animation-name	设置对象所应用的动画名称

  > 必须与规则@keyframes配合使用，因为动画名称由@keyframes定义 

* animation-duration	设置对象动画的持续时间

* animation-timing-function	 设置对象动画的过渡类型

  > ease： (默认)平滑过渡。等同于贝塞尔曲线(0.25, 0.1, 0.25, 1.0) 
  > linear： 线性过渡。等同于贝塞尔曲线(0.0, 0.0, 1.0, 1.0) 
  > ease-in： 由慢到快。等同于贝塞尔曲线(0.42, 0, 1.0, 1.0) 
  > ease-out： 由快到慢。等同于贝塞尔曲线(0, 0, 0.58, 1.0) 
  > ease-in-out： 由慢到快再到慢。等同于贝塞尔曲线(0.42, 0, 0.58, 1.0) 
  > step-start： 等同于 steps(1, start) 
  > step-end： 等同于 steps(1, end) 
  > steps(<integer>[, [ start | end ] ]?)： 接受两个参数的步进函数。第一个参数必须为正整数，指定函数的步数。第二个参数取值可以是start或end，指定每一步的值发生变化的时间点。第二个参数是可选的，默认值为end。 
  > cubic-bezier(<number>, <number>, <number>, <number>)： 特定的贝塞尔曲线类型，4个数值需在[0, 1]区间内 	

* animation-delay		指定对象动画的延迟时间

* animation-iteration-count	  指定动画的具体循环次数

  > number:动画循环次数
  > infinite： 无限循环 

* animation-direction	设置对象动画在循环中是否反向运动 

  > normal： 正常方向 (默认)
  > reverse： 反方向运行 
  > alternate： 动画先正常运行再反方向运行，并持续交替运行 
  > alternate-reverse： 动画先反运行再正方向运行，并持续交替运行 

* animation-play-state	设置对象动画的状态

  > running： 运动 (默认)
  > paused： 暂停 

* animation-fill-mode	设置对象动画时间之外的状态 

  > none		默认值。动画在动画执行之前和之后不会应用任何样式到目标元素。
  > forwards 	在动画结束后（由 animation-iteration-count 决定），动画将应用该属性值。
  > backwards	动画将应用在 animation-delay 定义期间启动动画的第一次迭代的关键帧中定义的属性值。这些都是from 				关键帧中的值（当 animation-direction 为 "normal" 或 "alternate" 时）或 to 关键帧中的值（当 animation-direction 为 "reverse" 或 "alternate-reverse" 时）。
  > both		动画遵循 forwards 和 backwards 的规则。也就是说，动画会在两个方向上扩展动画属性。

​	



## 6 CSS3嵌入WEB字体

### 6.1 什么是@font-face	 

* 可以把字体放置在服务器上,而不受制于客户端系统字体			
* 浏览器会根据指定的命令将对应的字体下载到本地缓存			
* 1998年@font-face加入到css2中, 但css2.1中又被移出,css3重新加入	
* IE兼容性极好

### 6.2 @font-face语法

#### 格式

```css
@font-face { 
	font-family: <identifier>; 
	src: <fontsrc> [<string>] [, <fontsrc> [<string>]]*; 
	[<font>];
 }																			
```

#### 相关参数	 

* identifier	字体名称						

* url		      此值指的是你自定义的字体的存放路径，可以是相对路径也可以是绝路径 

* string	 字体的格式，主要用来帮助浏览器识别, format(fontType) 		

  > truetype		.ttf	
  > 	Firefox3.5+ Chrome 4+ Safari 3+ Opear10+ IOS Mobile Safari 4.2+ IE9+
  > opentype	.otf	
  > 	Firefox3.5+ Chrome 4+ Safari 3+ Opear10+ IOS Mobile Safari 4.2+
  > Web Open Font Format	.woff	
  > 	Firefox 3.5+ Chrome 6+ Safari 3.6+ Opera 11.1+ IE9+
  > embedded Open Type	.eot	
  > 	IE4+
  > svg	 .svg	
  > 	Chrome 4+ Safari 3.1 + Opera 10+ IOS Mobile Safari 3.2+	



* font	 定义字体相关样式

  > font-weight	
  > font-style	
  > font-size	
  > font-variant	
  >
  > font-stretch			

#### 兼容性处理

```css
@font-face {
	font-family: 'diyfont';
	src: url('diyfont.eot'); /* IE9兼容模式 */
	src: url('diyfont.eot?#iefix') format('embedded-opentype'), /* IE9 - */
		 url('diyfont.woff') format('woff'), /* chrome、firefox opera  safari  IE9+ 最佳格式 */
		 url('diyfont.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+ IE9+*/
		 url('diyfont.svg#fontname') format('svg'); /* iOS 4.1- */
}
```



### 6.3 字体工具

#### web字体定制

* http://www.iconfont.cn/webfont/#!/webfont/index 阿里Web字体		 
* http://www.youziku.com/ 字体库网站						 

#### web字体转换

* https://www.fontsquirrel.com/tools/webfont-generator	FontSquirrel在线工具 



### 6.4 使用字体图标

#### 使用字体图标的优势	

* 相比位图更加清晰				
* 灵活性高，更方便改变大小、颜色、风格等	
* 兼容性好，低版本IE也支持			

#### 常用的字体图标库	

* 阿里图标	 http://www.iconfont.cn/		

* Font Awesome http://fontawesome.dashgame.com/	

* Glyphicons Halfings http://glyphicons.com/			

* 字体图标制作工具	

  http://icomoon.io/app/#/select 				

  http://www.iconfont.cn/help/iconmake.html		阿里图标

​		