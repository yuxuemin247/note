# BootStrap基础

## 1 什么是BootStrap

* 由Twitter的设计师Mark Otto和Jacob Thornton合作开发，是一个CSS/HTML框架
	 简洁、直观、强悍的前端开发框架，让web开发更迅速、简单。			



## 2 BootStrap的版本

* BootStrap2
* BootStrap3
* BootStrap4



## 3 BootStrap 下载

* [用于生产环境的Bootstrap](href="https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip")
* [Bootstrap Less 源码](https://github.com/twbs/bootstrap/archive/v3.3.7.zip)
	 [Bootstrap Sass 源码](https://github.com/twbs/bootstrap-sass/archive/v3.3.7.tar.gz)		

	​		

## 4 CDN服务

```html
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- 可选的Bootstrap主题文件（一般不用引入） -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
```



## 5 目录结构

**生产环境版**

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   └── bootstrap-theme.min.css
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    ├── glyphicons-halflings-regular.woff
    └── glyphicons-halflings-regular.woff2
```

 这是 Bootstrap 最基础的形式：直接拖入即用的编译文件，几乎能在所有Web项目中使用。
其中`bootstrap.*`是预编译的文件。
而`bootstrap.min.*`是编译过且压缩后的文件，用户可以根据自己需要引用。
程序目录中，还有`bootstrap.*.map`格式的文件，这是Source map文件，需要在[特定的浏览器开发者工具](https://developers.google.com/web/tools/chrome-devtools/javascript/source-maps)下才可用式。 

## 6 基本模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>你好，世界！</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```



## 7 浏览器支持

**手机浏览器**

| ------- | Chrome  | Firefox   | Safari    |
| ------- | --------- | --------- | --------- |
| Android | Supported | Supported | N/A       |
| iOS     | Supported | Supported | Supported |

**桌面浏览器**

|---------| Chrome  | Firefox   | Internet Explorer | Opera     | Safari  |
| ------- | --------- | ----------------- | --------- | --------- | ------------- |
| Mac     | Supported | Supported         | N/A       | Supported | Supported     |
| Windows | Supported | Supported         | Supported | Supported | Not supported |



## 8 浏览器兼容

#### 让 IE8 支持H5新标签

页面中引入`respond.js`

```html
<!-- 注意： 页面必须通过服务器访问 -->
<script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
```

#### IE兼容模式

页面中添加如下代码

```html
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

#### 国产浏览器切换webkit内核

页面中添加如下代码

```html
<meta name="renderer" content="webkit">
```

###### 