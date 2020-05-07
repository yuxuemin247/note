# Bootstrap

## 一、简介

```
Bootstrap是美国Twitter公司的设计师Mark Otto和Jacob Thornton合作基于HTML、CSS、JavaScript 开发的简洁、直观、强悍的前端开发框架，使得 Web 开发更加快捷。
```

## 二、安装

#### 1、本地链接

[官网下载](https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip)

#### 2、CDN

```html
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

## 三、布局容器

- 固定宽度：.container
- 流式布局：.container-fluid

## 四、响应式布局

- 超小屏幕：大于 576px
- 小屏幕：大于等于 768px
- 中等屏幕：大于等于 992px
- 大屏幕：大于等于 1200px

```
通过在Sass中写了源CSS，所有的媒体查询通过Sass mixins都是可用的,SASS的Mixins可以一次性定义功能模块，让你在任何地方调用，并且可以无限制的重用）
```

## 五、删格系统

#### 1、概念

```
将父级可用宽度(content)均分为12等份
```

#### 2、列比

-  总共有[五个栅格等级](https://code.z01.com/v4/layout/grid.html#responsive-breakpoints)，每个响应式分界点隔出一个等级：特小`.col`、小`.col-sm-*`、中`.col-md-*`、大`.col-lg-*`、特大（大、特大也可以称为宽、超宽）`.col-xl-*`。
-   栅格断点的媒体查询基于宽度的最小值，意味着它们应用到某一等级以及这一等级之上的所有（如`.col-sm-4`的的定义可以在小型、中型、宽、超宽设备上呈现，但不适用于能在超小型`.col-sx`上呈现） 

###### v-hint：只设置小屏列比会影响大屏列比；只设置大屏列比小屏时会撑满屏幕

#### 3、行

```html
<div class="row"></div>
...
<div class="row no-gutters "></div>
<!-- no-gutters,使页面不会额外宽出30px-->
```

#### 4、列偏移

- 超小屏幕：.col-xs-offset-*
- 小屏幕：.col-sm-offset-*
- 中等屏幕：.col-md-offset-*
- 大屏幕：.col-lg-offset-*

## 六、辅助类

#### 1、 情境背景色

```html
<p class="bg-primary">...</p>
<p class="bg-success">...</p>
<p class="bg-info">...</p>
<p class="bg-warning">...</p>
<p class="bg-danger">...</p>
```

#### 2、快速浮动

```html
<div class="pull-left">...</div>
<div class="pull-right">...</div>
```

#### 3、快速清浮动

```html
<div class="clearfix">...</div>
```

#### 4、显隐

```html
<div class="show">...</div>
<div class="hidden">...</div>
```

## 七、字体图标

```html
<i class="glyphicon glyphicon-*"></i>
```

## 八、组件

```
API
```

