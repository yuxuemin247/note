# Bootstrap插件

## 1 BootStrap插件使用规则

### 1.1 单个引入

JavaScript 插件可以单个引入（使用 Bootstrap 提供的单个 `*.js` 文件），或者一次性全部引入（使用 `bootstrap.js` 或压缩版的 `bootstrap.min.js`）。 

> 某些插件和 CSS 组件依赖于其它插件。如果你是单个引入每个插件的，请确保在文档中检查插件之间的依赖关系。注意，所有插件都依赖 jQuery （也就是说，jQuery必须在所有插件**之前**引入页面）。 [`bower.json`](https://github.com/twbs/bootstrap/blob/v3.3.7/bower.json) 文件中列出了 Bootstrap 所支持的 jQuery 版本。

### 1.2 data属性

你可以仅仅通过 data 属性 API 就能使用所有的 Bootstrap 插件，无需写一行 JavaScript 代码。这是 Bootstrap 中的一等 API，也应该是你的首选方式。

话又说回来，在某些情况下可能需要将此功能关闭。因此，我们还提供了关闭 data 属性 API 的方法，即解除以 `data-api` 为命名空间并绑定在文档上的事件。就像下面这样：

```js
$(document).off('.data-api')
```

另外，如果是针对某个特定的插件，只需在 `data-api` 前面添加那个插件的名称作为命名空间，如下：

```js
$(document).off('.alert.data-api')
```



### 1.3 编程方式的 API

我们为所有 Bootstrap 插件提供了纯 JavaScript 方式的 API。所有公开的 API 都是支持单独或链式调用方式，并且返回其所操作的元素集合（注：和jQuery的调用形式一致）。

```js
$('.btn.danger').button('toggle').addClass('fat')
```

所有方法都可以接受一个可选的 option 对象作为参数，或者一个代表特定方法的字符串，或者什么也不提供（在这种情况下，插件将会以默认值初始化）：

```js
$('#myModal').modal()                      // 以默认值初始化
$('#myModal').modal({ keyboard: false })   // initialized with no keyboard
$('#myModal').modal('show')                // 初始化后立即调用 show 方法
```

每个插件还通过 `Constructor` 属性暴露了其原始的构造函数：`$.fn.popover.Constructor`。如果你想获取某个插件的实例，可以直接通过页面元素获取：`$('[rel="popover"]').data('popover')`。

**默认设置**

每个插件都可以通过修改其自身的 `Constructor.DEFAULTS` 对象从而改变插件的默认设置：

```js
$.fn.modal.Constructor.DEFAULTS.keyboard = false // 将模态框插件的 `keyboard` 默认选参数置为 false
```



### 1.4 避免命名空间冲突

某些时候可能需要将 Bootstrap 插件与其他 UI 框架共同使用。在这种情况下，命名空间冲突随时可能发生。如果不幸发生了这种情况，你可以通过调用插件的 `.noConflict` 方法恢复其原始值。

```js
var bootstrapButton = $.fn.button.noConflict() // return $.fn.button to previously assigned value
$.fn.bootstrapBtn = bootstrapButton            // give $().bootstrapBtn the Bootstrap functionality
```



### 1.5 事件

Bootstrap 为大部分插件所具有的动作提供了自定义事件。一般来说，这些事件都有不定式和过去式两种动词的命名形式，例如，不定式形式的动词（例如 `show`）表示其在事件开始时被触发；而过去式动词（例如 `shown` ）表示在动作执行完毕之后被触发。

从 3.0.0 版本开始，所有 Bootstrap 事件的名称都采用命名空间方式。

所有以不定式形式的动词命名的事件都提供了 `preventDefault` 功能。这就赋予你在动作开始执行前将其停止的能力。

```
$('#myModal').on('show.bs.modal', function (e) {
  if (!data) return e.preventDefault() // 阻止模态框的展示
})
```



### 1.6 版本号

每个 Bootstrap 的 jQuery 插件的版本号都可以通过插件的构造函数上的 `VERSION` 属性获取到。例如工具提示框（tooltip）插件：

```
$.fn.tooltip.Constructor.VERSION // => "3.3.7"
```



## 2 过渡效果 transition.js

### 2.1 关于过渡效果

对于简单的过渡效果，只需将 `transition.js` 和其它 JS 文件一起引入即可。如果你使用的是编译（或压缩）版的 `bootstrap.js` 文件，就无需再单独将其引入了。

### 2.3 包含的内容

Transition.js 是针对 `transitionEnd` 事件的一个基本辅助工具，也是对 CSS 过渡效果的模拟。它被其它插件用来检测当前浏览器对是否支持 CSS 的过渡效果。

### 2.4 禁用过度效果

通过下面的 JavaScript 代码可以在全局范围禁用过渡效果，并且必须将此代码放在 `transition.js` （或 `bootstrap.js` 或 `bootstrap.min.js`）后面，确保在 js 文件加载完毕后再执行下面的代码：

```
$.support.transition = false
```



## 3 模态框 modal.js

> 务必将模态框的 HTML 代码放在文档的最高层级内（也就是说，尽量作为 body 标签的直接子元素），以避免其他组件影响模态框的展现和/或功能。 

### 3.1 模态框定义

```html
<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Modal title</h4>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```



### 3.2 按钮

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
  Launch demo modal
</button>

```



### 3.3 模态框尺寸

```html
<!-- Large modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target=".bs-example-modal-lg">Large modal</button>

<div class="modal fade bs-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      ...
    </div>
  </div>
</div>

<!-- Small modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target=".bs-example-modal-sm">Small modal</button>

<div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
  <div class="modal-dialog modal-sm" role="document">
    <div class="modal-content">
      ...
    </div>
  </div>
</div>
```

 

### 3.4 禁止动画效果

如果你不需要模态框弹出时的动画效果（淡入淡出效果），删掉 `.fade` 类即可。

```html
<div class="modal" tabindex="-1" role="dialog" aria-labelledby="...">
  ...
</div>
```



### 3.5 模态框中使用栅格系统

```html
<div class="modal fade" tabindex="-1" role="dialog" aria-labelledby="gridSystemModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="gridSystemModalLabel">Modal title</h4>
      </div>
      <div class="modal-body">
        <div class="row">
          <div class="col-md-4">.col-md-4</div>
          <div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>
        </div>
        <div class="row">
          <div class="col-md-3 col-md-offset-3">.col-md-3 .col-md-offset-3</div>
          <div class="col-md-2 col-md-offset-4">.col-md-2 .col-md-offset-4</div>
        </div>
        <div class="row">
          <div class="col-md-6 col-md-offset-3">.col-md-6 .col-md-offset-3</div>
        </div>
        <div class="row">
          <div class="col-sm-9">
            Level 1: .col-sm-9
            <div class="row">
              <div class="col-xs-8 col-sm-6">
                Level 2: .col-xs-8 .col-sm-6
              </div>
              <div class="col-xs-4 col-sm-6">
                Level 2: .col-xs-4 .col-sm-6
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
```



### 3.6 基于触发器按钮的不同模态内容

```html
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">Open modal for @mdo</button>
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@fat">Open modal for @fat</button>
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@getbootstrap">Open modal for @getbootstrap</button>
...more buttons...

<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel">New message</h4>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group">
            <label for="recipient-name" class="control-label">Recipient:</label>
            <input type="text" class="form-control" id="recipient-name">
          </div>
          <div class="form-group">
            <label for="message-text" class="control-label">Message:</label>
            <textarea class="form-control" id="message-text"></textarea>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Send message</button>
      </div>
    </div>
  </div>
</div>
```

```js
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})
```



### 3.7 通过JavaScript处理模态框

#### 打开

```js
$('#myModal').modal(options)
```

#### 参数

| 名称     | 类型                         | 默认值 | 描述                                                         |
| -------- | ---------------------------- | ------ | ------------------------------------------------------------ |
| backdrop | boolean 或 字符串 `'static'` | true   | I指定一个静态的背景，当用户点击模态框外部时不会关闭模态框。  |
| keyboard | boolean                      | true   | 键盘上的 esc 键被按下时关闭模态框。                          |
| show     | boolean                      | true   | 模态框初始化之后就立即显示出来。                             |
| remote   | path                         | false  | **This option is deprecated since v3.3.0 and has been removed in v4.** We recommend instead using client-side templating or a data binding framework, or calling [jQuery.load](http://api.jquery.com/load/)yourself.如果提供的是 URL，将利用 jQuery 的 `load` 方法**从此 URL 地址加载要展示的内容（只加载一次）**并插入 `.modal-content` 内。如果使用的是 data 属性 API，还可以利用 `href` 属性指定内容来源地址。下面是一个实例：`<a data-toggle="modal" href="remote.html" data-target="#modal">Click me</a>` |

#### 方法

**`.modal(options)`**

将页面中的某块内容作为模态框激活。接受可选参数 `object`。

```
$('#myModal').modal({
  keyboard: false
})
```

**`.modal('toggle')`**

手动打开或关闭模态框。**在模态框显示或隐藏之前返回到主调函数中**（也就是，在触发 `shown.bs.modal` 或 `hidden.bs.modal` 事件之前）。

```
$('#myModal').modal('toggle')
```

**`.modal('show')`**

手动打开模态框。**在模态框显示之前返回到主调函数中** （也就是，在触发 `shown.bs.modal` 事件之前）。

```
$('#myModal').modal('show')
```

**`.modal('hide')`**

手动隐藏模态框。**在模态框隐藏之前返回到主调函数中** （也就是，在触发 `hidden.bs.modal` 事件之前）。

```
$('#myModal').modal('hide')
```

**`.modal('handleUpdate')`**

整模态的定位，以对抗滚动条，以防出现一个模式，这会使模态向左跳

只需要当模态的高度在打开时改变。

```
$('#myModal').modal('handleUpdate')
```

#### 事件

Bootstrap 的模态框类提供了一些事件用于监听并执行你自己的代码。

| 事件类型        | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| show.bs.modal   | `show` 方法调用之后立即触发该事件。如果是通过点击某个作为触发器的元素，则此元素可以通过事件的 `relatedTarget` 属性进行访问。 |
| shown.bs.modal  | 此事件在模态框已经显示出来（并且同时在 CSS 过渡效果完成）之后被触发。如果是通过点击某个作为触发器的元素，则此元素可以通过事件的 `relatedTarget` 属性进行访问。 |
| hide.bs.modal   | `hide` 方法调用之后立即触发该事件。                          |
| hidden.bs.modal | 此事件在模态框被隐藏（并且同时在 CSS 过渡效果完成）之后被触发。 |
| loaded.bs.modal | 从`远端的数据源`加载完数据之后触发该事件。                   |

```js
$('#myModal').on('hidden.bs.modal', function (e) {
  // do something...
})
```



## 4 下拉菜单 dropdown.js

### 4.1 JavaScript调用

```js
$('.dropdown-toggle').dropdown()
```

#### 方法

**`$().dropdown('toggle')`**

Toggles the dropdown menu of a given navbar or tabbed navigation.

####  事件

| Event Type         | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| show.bs.dropdown   | This event fires immediately when the show instance method is called. |
| shown.bs.dropdown  | This event is fired when the dropdown has been made visible to the user (will wait for CSS transitions, to complete). |
| hide.bs.dropdown   | This event is fired immediately when the hide instance method has been called. |
| hidden.bs.dropdown | This event is fired when the dropdown has finished being hidden from the user (will wait for CSS transitions, to complete). |

```js
$('#myDropdown').on('show.bs.dropdown', function () {
  // do something…
})
```



## 5 滚动监听 scrollspy.js

滚动监听插件是用来根据滚动条所处的位置来自动更新导航项的。滚动导航条下面的区域并关注导航项的变化。下拉菜单中的条目也会自动高亮显示。

> 依赖 Bootstrap 的导航组件
>
> 滚动监听插件依赖 Bootstrap 的导航组件用于高亮显示当前激活的链接。
>
> 无论何种实现方式，滚动监听都需要被监听的组件是 `position: relative;` 即相对定位方式。大多数时候是监听 `<body>` 元素



### 5.1 基本调用

```css
body {
  position: relative;
}
```

```html
<body data-spy="scroll" data-target="#navbar-example">
  ...
  <div id="navbar-example">
    <ul class="nav nav-tabs" role="tablist">
      ...
    </ul>
  </div>
  ...
</body>
```



### 5.2 JavaScript调用

```js
$('body').scrollspy({ target: '#navbar-example' })
```

#### 方法

**`.scrollspy('refresh')`**

当使用滚动监听插件的同时在 DOM 中添加或删除元素后，你需要像下面这样调用此刷新（ refresh） 方法：

```js
$('[data-spy="scroll"]').each(function () {
  var $spy = $(this).scrollspy('refresh')
})
```

#### 参数

可以通过 data 属性或 JavaScript 传递参数。对于 data 属性，其名称是将参数名附着到 `data-` 后面组成，例如 `data-offset=""`。

| 名称   | 类型   | 默认值 | 描述                                         |
| ------ | ------ | ------ | -------------------------------------------- |
| offset | number | 10     | 计算滚动位置时相对于顶部的偏移量（像素数）。 |

#### 事件

| 事件类型              | 描述                                                 |
| --------------------- | ---------------------------------------------------- |
| activate.bs.scrollspy | 每当一个新条目被激活后都将由滚动监听插件触发此事件。 |

```js
$('#myScrollspy').on('activate.bs.scrollspy', function () {
  // do something…
})
```



## 6 标签页  tab.js

### 6.1 基本使用

```html
<div>

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">
    <li role="presentation" class="active"><a href="#home" aria-controls="home" role="tab" data-toggle="tab">Home</a></li>
    <li role="presentation"><a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">Profile</a></li>
    <li role="presentation"><a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">Messages</a></li>
    <li role="presentation"><a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">Settings</a></li>
  </ul>

  <!-- Tab panes -->
  <div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="home">...</div>
    <div role="tabpanel" class="tab-pane" id="profile">...</div>
    <div role="tabpanel" class="tab-pane" id="messages">...</div>
    <div role="tabpanel" class="tab-pane" id="settings">...</div>
  </div>

</div>
```



### 6.2 Fade特效

```html
<div class="tab-content">
  <div role="tabpanel" class="tab-pane fade in active" id="home">...</div>
  <div role="tabpanel" class="tab-pane fade" id="profile">...</div>
  <div role="tabpanel" class="tab-pane fade" id="messages">...</div>
  <div role="tabpanel" class="tab-pane fade" id="settings">...</div>
</div>
```



### 6.3 JavaScript调用

```js
$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})
```

```js
$('#myTabs a[href="#profile"]').tab('show') // Select tab by name
$('#myTabs a:first').tab('show') // Select first tab
$('#myTabs a:last').tab('show') // Select last tab
$('#myTabs li:eq(2) a').tab('show') // Select third tab (0-indexed)
```

#### 方法

**`$().tab`**

该方法可以激活标签页元素和内容容器。标签页需要用一个 **data-target** 或者一个指向 DOM 中容器节点的 **href**。

**`.tab('show')`**

Selects the given tab and shows its associated content. Any other tab that was previously selected becomes unselected and its associated content is hidden. **Returns to the caller before the tab pane has actually been shown** (i.e. before the `shown.bs.tab`event occurs).

```js
$('#someTab').tab('show')
```

#### 事件

| 事件         | 描述                                                         | 实例                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| show.bs.tab  | 该事件在标签页显示时触发，但是必须在新标签页被显示之前。分别使用 **event.target** 和 **event.relatedTarget** 来定位到激活的标签页和前一个激活的标签页。 | `$('a[data-toggle="tab"]').on('show.bs.tab', function (e) {   e.target // 激活的标签页   e.relatedTarget // 前一个激活的标签页 })` |
| shown.bs.tab | 该事件在标签页显示时触发，但是必须在某个标签页已经显示之后。分别使用 **event.target** 和 **event.relatedTarget** 来定位到激活的标签页和前一个激活的标签页。 | `$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {   e.target // 激活的标签页   e.relatedTarget // 前一个激活的标签页 })` |

```js
$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  e.target // newly activated tab
  e.relatedTarget // previous active tab
})
```



## 7 工具提示 tooltips.js

### 7.1 基本使用

```html
<button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="left" title="Tooltip on left">Tooltip on left</button>

<button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="top" title="Tooltip on top">Tooltip on top</button>

<button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="bottom" title="Tooltip on bottom">Tooltip on bottom</button>

<button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="right" title="Tooltip on right">Tooltip on right</button>
```

### 7.2 JavaScript调用

```js
$('#example').tooltip(options)
```

#### 参数

| 选项名称  | 类型/默认值                     | Data 属性名称  | 描述                                                         |
| --------- | ------------------------------- | -------------- | ------------------------------------------------------------ |
| animation | boolean *默认值：true*          | data-animation | 提示工具使用 CSS 渐变滤镜效果。                              |
| html      | boolean *默认值：false*         | data-html      | 向提示工具插入 HTML。如果为 false，jQuery 的 text 方法将被用于向 dom 插入内容。如果您担心 XSS 攻击，请使用 text。 |
| placement | string\|function *默认值：top*  | data-placement | 规定如何定位提示工具（即 top\|bottom\|left\|right\|auto）。 当指定为 *auto* 时，会动态调整提示工具。例如，如果 placement 是 "auto left"，提示工具将会尽可能显示在左边，在情况不允许的情况下它才会显示在右边。 |
| selector  | string *默认值：false*          | data-selector  | 如果提供了一个选择器，提示工具对象将被委派到指定的目标。     |
| title     | string \| function *默认值：''* | data-title     | 如果未指定 *title* 属性，则 title 选项是默认的 title 值。    |
| trigger   | string *默认值：'hover focus'*  | data-trigger   | 定义如何触发提示工具： **click\| hover \| focus \| manual**。您可以传递多个触发器，每个触发器之间用空格分隔。 |
| delay     | number \| object *默认值：0*    | data-delay     | 延迟显示和隐藏提示工具的毫秒数 - 对 manual 手动触发类型不适用。如果提供的是一个数字，那么延迟将会应用于显示和隐藏。如果提供的是对象，结构如下所示：`delay: { show: 500, hide: 100 }` |
| container | string \| false *默认值：false* | data-container | 向指定元素追加提示工具。 实例： container: 'body'            |

#### 方法

| 方法                             | 描述                          | 实例                               |
| -------------------------------- | ----------------------------- | ---------------------------------- |
| **Options:** .tooltip(options)   | 向元素集合附加提示工具句柄。  | `$().tooltip(options)`             |
| **Toggle:** .tooltip('toggle')   | 切换显示/隐藏元素的提示工具。 | `$('#element').tooltip('toggle')`  |
| **Show:** .tooltip('show')       | 显示元素的提示工具。          | `$('#element').tooltip('show')`    |
| **Hide:** .tooltip('hide')       | 隐藏元素的提示工具。          | `$('#element').tooltip('hide')`    |
| **Destroy:** .tooltip('destroy') | 隐藏并销毁元素的提示工具。    | `$('#element').tooltip('destroy')` |

```js
$('#element').tooltip('destroy')
```

#### 事件

| 事件              | 描述                                                         | 实例                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| show.bs.tooltip   | 当调用 show 实例方法时立即触发该事件。                       | `$('#myTooltip').on('show.bs.tooltip', function () {   // 执行一些动作... })` |
| shown.bs.tooltip  | 当提示工具对用户可见时触发该事件（将等待 CSS 过渡效果完成）。 | `$('#myTooltip').on('shown.bs.tooltip', function () {   // 执行一些动作... })` |
| hide.bs.tooltip   | 当调用 hide 实例方法时立即触发该事件。                       | `$('#myTooltip').on('hide.bs.tooltip', function () {   // 执行一些动作... })` |
| hidden.bs.tooltip | 当提示工具对用户隐藏时触发该事件（将等待 CSS 过渡效果完成）。 | `$('#myTooltip').on('hidden.bs.tooltip', function () {   // 执行一些动作... })` |

```js
$('#myTooltip').on('hidden.bs.tooltip', function () {
  // do something…
})
```



## 8 弹出框 popover.js

### 8.1 基本使用

#### 基本

```html
<button type="button" class="btn btn-lg btn-danger" data-toggle="popover" title="Popover title" data-content="And here's some amazing content. It's very engaging. Right?">点我弹出/隐藏弹出框</button>
```

#### 弹出方向

```html
<button type="button" class="btn btn-default" data-container="body" data-toggle="popover" data-placement="left" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on 左侧
</button>

<button type="button" class="btn btn-default" data-container="body" data-toggle="popover" data-placement="top" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on 顶部
</button>

<button type="button" class="btn btn-default" data-container="body" data-toggle="popover" data-placement="bottom" data-content="Vivamus
sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on 底部
</button>

<button type="button" class="btn btn-default" data-container="body" data-toggle="popover" data-placement="right" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on 右侧
</button>
```

#### 点击并让弹出框消失

通过使用 `focus` 触发器可以在用户点击弹出框是让其消失。

> 实现“点击并让弹出框消失”的效果需要一些额外的代码
>
> 为了更好的跨浏览器和跨平台效果，你必须使用 `<a>` 标签，*不能*使用 `<button>` 标签，并且，还必须包含 `role="button"` 和 [`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#tabindex) 属性。

```html
<a tabindex="0" class="btn btn-lg btn-danger" role="button" data-toggle="popover" data-trigger="focus" title="Dismissible popover" data-content="And here's some amazing content. It's very engaging. Right?">可消失的弹出框</a>
```



### 8.2 javaScript调用

```js
$('#example').popover(options)
```

#### 参数

可以通过 data 属性或 JavaScript 传递参数。对于 data 属性，将参数名附着到 `data-` 后面，例如 `data-animation=""`。

| 选项名称  | 类型/默认值                     | Data 属性名称  | 描述                                                         |
| --------- | ------------------------------- | -------------- | ------------------------------------------------------------ |
| animation | boolean *默认值：true*          | data-animation | 向弹出框应用 CSS 褪色过渡效果。                              |
| html      | boolean *默认值：false*         | data-html      | 向弹出框插入 HTML。如果为 false，jQuery 的 text 方法将被用于向 dom 插入内容。如果您担心 XSS 攻击，请使用 text。 |
| placement | string\|function *默认值：top*  | data-placement | 规定如何定位弹出框（即 top\|bottom\|left\|right\|auto）。 当指定为 *auto* 时，会动态调整弹出框。例如，如果 placement 是 "auto left"，弹出框将会尽可能显示在左边，在情况不允许的情况下它才会显示在右边。 |
| selector  | string *默认值：false*          | data-selector  | 如果提供了一个选择器，弹出框对象将被委派到指定的目标。       |
| title     | string \| function *默认值：''* | data-title     | 如果未指定 *title* 属性，则 title 选项是默认的 title 值。    |
| trigger   | string *默认值：'hover focus'*  | data-trigger   | 定义如何触发弹出框： **click\| hover \| focus \| manual**。您可以传递多个触发器，每个触发器之间用空格分隔。 |
| delay     | number \| object *默认值：0*    | data-delay     | 延迟显示和隐藏弹出框的毫秒数 - 对 manual 手动触发类型不适用。如果提供的是一个数字，那么延迟将会应用于显示和隐藏。如果提供的是对象，结构如下所示：`delay: { show: 500, hide: 100 }` |
| container | string \| false *默认值：false* | data-container | 向指定元素追加弹出框。 实例： container: 'body'              |

#### 方法

| 方法                             | 描述                        | 实例                               |
| -------------------------------- | --------------------------- | ---------------------------------- |
| **Options:** .popover(options)   | 向元素集合附加弹出框句柄。  | `$().popover(options)`             |
| **Toggle:** .popover('toggle')   | 切换显示/隐藏元素的弹出框。 | `$('#element').popover('toggle')`  |
| **Show:** .popover('show')       | 显示元素的弹出框。          | `$('#element').popover('show')`    |
| **Hide:** .popover('hide')       | 隐藏元素的弹出框。          | `$('#element').popover('hide')`    |
| **Destroy:** .popover('destroy') | 隐藏并销毁元素的弹出框。    | `$('#element').popover('destroy')` |

```js
$('#element').popover('destroy') 
```

#### 事件

| 事件              | 描述                                                         | 实例                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| show.bs.popover   | 当调用 show 实例方法时立即触发该事件。                       | `$('#mypopover').on('show.bs.popover', function () {   // 执行一些动作... })` |
| shown.bs.popover  | 当弹出框对用户可见时触发该事件（将等待 CSS 过渡效果完成）。  | `$('#mypopover').on('shown.bs.popover', function () {   // 执行一些动作... })` |
| hide.bs.popover   | 当调用 hide 实例方法时立即触发该事件。                       | `$('#mypopover').on('hide.bs.popover', function () {   // 执行一些动作... })` |
| hidden.bs.popover | 当工具提示对用户隐藏时触发该事件（将等待 CSS 过渡效果完成）。 | `$('#mypopover').on('hidden.bs.popover', function () {   // 执行一些动作... })` |

```
$('#myPopover').on('hidden.bs.popover', function () {
  // do something…
})
```



## 9 警告信息 alert.js

### 9.1 基本使用

当使用 `.close` 按钮时，它必须是 `.alert-dismissible` 的第一个子元素，并且在它之前不能有任何文本内容。

为关闭按钮添加 `data-dismiss="alert"` 属性就可以使其自动为警告框赋予关闭功能。关闭警告框也就是将其从 DOM 中删除。

```html
<button type="button" class="close" data-dismiss="alert" aria-label="Close">
  <span aria-hidden="true">&times;</span>
</button>
```

为了让警告框在关闭时表现出动画效果，请确保为其添加了 `.fade` 和 `.in` 类。



### 9.2 JavaScript调用

#### 方法

**`$().alert()`**

让警告框监听具有 `data-dismiss="alert"` 属性的后裔元素的点击（click）事件。（如果是通过 data 属性进行的初始化则无需使用）

**`$().alert('close')`**

关闭警告框并从 DOM 中将其删除。如果警告框被赋予了 `.fade` 和 `.in` 类，那么，警告框在淡出之后才会被删除。

#### 事件

Bootstrap 的警告框插件对外暴露了一些可以被监听的事件。

| 事件类型        | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| close.bs.alert  | 当 `close` 方法被调用后立即触发此事件。                      |
| closed.bs.alert | 当警告框被关闭后（也即 CSS 过渡效果完毕之后）立即触发此事件。 |

```
$('#myAlert').on('closed.bs.alert', function () {
  // do something…
})
```



## 10 按钮 button.js

### 10.1 加载状态

```html
<button type="button" id="myButton" data-loading-text="Loading..." class="btn btn-primary" autocomplete="off">
  Loading state
</button>

<script>
  $('#myButton').on('click', function () {
    var $btn = $(this).button('loading')
    // business logic...
    $btn.button('reset')
  })
</script>
```

### 10.2 独立的按钮切换状态

```html
<button type="button" class="btn btn-primary" data-toggle="button" aria-pressed="false" autocomplete="off">
  Single toggle
</button>
```

### 10.3 Checkbox和Radio

```html
<div class="btn-group" data-toggle="buttons">
  <label class="btn btn-primary active">
    <input type="checkbox" autocomplete="off" checked> Checkbox 1 (pre-checked)
  </label>
  <label class="btn btn-primary">
    <input type="checkbox" autocomplete="off"> Checkbox 2
  </label>
  <label class="btn btn-primary">
    <input type="checkbox" autocomplete="off"> Checkbox 3
  </label>
</div>
```

```html
<div class="btn-group" data-toggle="buttons">
  <label class="btn btn-primary active">
    <input type="radio" name="options" id="option1" autocomplete="off" checked> Radio 1 (preselected)
  </label>
  <label class="btn btn-primary">
    <input type="radio" name="options" id="option2" autocomplete="off"> Radio 2
  </label>
  <label class="btn btn-primary">
    <input type="radio" name="options" id="option3" autocomplete="off"> Radio 3
  </label>
</div>
```



### 10.4 JavaScript方法

| 方法               | 描述                                                         | 实例                    |
| ------------------ | ------------------------------------------------------------ | ----------------------- |
| button('toggle')   | 切换按压状态。赋予按钮被激活的外观。您可以使用 **data-toggle** 属性启用按钮的自动切换。 | `$().button('toggle')`  |
| .button('loading') | 当加载时，按钮是禁用的，且文本变为 button 元素的 **data-loading-text** 属性的值。 | `$().button('loading')` |
| .button('reset')   | 重置按钮状态，文本内容恢复为最初的内容。当您想要把按钮返回为原始的状态时，该方法非常有用。 | `$().button('reset')`   |
| .button(string)    | 该方法中的字符串是指由用户声明的任何字符串。使用该方法，重置按钮状态，并添加新的内容。 | `$().button(string)`    |

```html
<button type="button" id="myStateButton" data-complete-text="finished!" class="btn btn-primary" autocomplete="off">
  ...
</button>

<script>
  $('#myStateButton').on('click', function () {
    $(this).button('complete') // button text will be "finished!"
  })
</script>
```



 ## 11 折叠 collapse.js

### 11.1 基本使用

```html
<a class="btn btn-primary" role="button" data-toggle="collapse" href="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Link with href
</a>
<button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Button with data-target
</button>
<div class="collapse" id="collapseExample">
  <div class="well">
    ...
  </div>
</div>
```



### 11.2 手风琴菜单

```html
<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
  <div class="panel panel-default">
    <div class="panel-heading" role="tab" id="headingOne">
      <h4 class="panel-title">
        <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          Collapsible Group Item #1
        </a>
      </h4>
    </div>
    <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
      <div class="panel-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading" role="tab" id="headingTwo">
      <h4 class="panel-title">
        <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Collapsible Group Item #2
        </a>
      </h4>
    </div>
    <div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">
      <div class="panel-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading" role="tab" id="headingThree">
      <h4 class="panel-title">
        <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Collapsible Group Item #3
        </a>
      </h4>
    </div>
    <div id="collapseThree" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree">
      <div class="panel-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
</div>
```

It's also possible to swap out `.panel-body`s with `.list-group`s.



### 11.3 JavaScript调用

```js
$('.collapse').collapse()
```

#### 选项

| 选项名称 | 类型/默认值              | Data 属性名称 | 描述                                                         |
| -------- | ------------------------ | ------------- | ------------------------------------------------------------ |
| parent   | selector *默认值：false* | data-parent   | 如果提供了一个选择器，当可折叠项目显示时，指定父元素下的所有可折叠的元素将被关闭。这与传统的折叠面板（accordion）的行为类似 - 这依赖于 accordion-group 类。 |
| toggle   | boolean *默认值：true*   | data-toggle   | 切换调用可折叠元素。                                         |

#### 方法

| 方法                            | 描述                                                | 实例                                                |
| ------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| **Options:** .collapse(options) | 激活内容为可折叠元素。接受一个可选的 options 对象。 | `$('#identifier').collapse({     toggle: false }) ` |
| **Toggle:** .collapse('toggle') | 切换显示/隐藏可折叠元素。                           | `$('#identifier').collapse('toggle') `              |
| **Show:** .collapse('show')     | 显示可折叠元素。                                    | `$('#identifier').collapse('show') `                |
| **Hide:** .collapse('hide')     | 隐藏可折叠元素。                                    | `$('#identifier').collapse('hide')`                 |

#### 事件

| 事件               | 描述                                                         | 实例                                                         |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| show.bs.collapse   | 在调用 show 方法后触发该事件。                               | `$('#identifier').on('show.bs.collapse', function () {     // 执行一些动作... })` |
| shown.bs.collapse  | 当折叠元素对用户可见时触发该事件（将等待 CSS 过渡效果完成）。 | `$('#identifier').on('shown.bs.collapse', function () {     // 执行一些动作... })` |
| hide.bs.collapse   | 当调用 hide 实例方法时立即触发该事件。                       | `$('#identifier').on('hide.bs.collapse', function () {     // 执行一些动作... })` |
| hidden.bs.collapse | 当折叠元素对用户隐藏时触发该事件（将等待 CSS 过渡效果完成）。 | `$('#identifier').on('hidden.bs.collapse', function () {     // 执行一些动作... })` |

```js
$('#myCollapsible').on('hidden.bs.collapse', function () {
  // do something…
})
```



## 12 轮播 carousel.js

### 12.1 基本使用

```html
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    <div class="item">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    ...
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
```



### 12.2 每个项目的标题

```html
<div class="item">
  <img src="..." alt="...">
  <div class="carousel-caption">
    <h3>...</h3>
    <p>...</p>
  </div>
</div>
```



### 12.3 JavaScript 调用

```js
$('.carousel').carousel()
```

#### 选项

| 选项名称 | 类型/默认值              | Data 属性名称 | 描述                                                         |
| -------- | ------------------------ | ------------- | ------------------------------------------------------------ |
| interval | number *默认值：5000*    | data-interval | 自动循环每个项目之间延迟的时间量。如果为 false，轮播将不会自动循环。 |
| pause    | string *默认值："hover"* | data-pause    | 鼠标进入时暂停轮播循环，鼠标离开时恢复轮播循环。             |
| wrap     | boolean *默认值：true*   | data-wrap     | 轮播是否连续循环。                                           |

#### 方法

| 方法               | 描述                                                  | 实例                                                |
| ------------------ | ----------------------------------------------------- | --------------------------------------------------- |
| .carousel(options) | 初始化轮播为可选的 options 对象，并开始循环项目。     | `$('#identifier').carousel({     interval: 2000 })` |
| .carousel('cycle') | 从左到右循环轮播项目。                                | `$('#identifier').carousel('cycle')`                |
| .carousel('pause') | 停止轮播循环项目。                                    | `$('#identifier').carousel('pause')`                |
| .carousel(number)  | 循环轮播到某个特定的帧（从 0 开始计数，与数组类似）。 | `$('#identifier').carousel(number)`                 |
| .carousel('prev')  | 循环轮播到上一个项目。                                | `$('#identifier').carousel('prev')`                 |
| .carousel('next')  | 循环轮播到下一个项目。                                | `$('#identifier').carousel('next')`                 |

#### 事件

| 事件              | 描述                                    | 实例                                                         |
| ----------------- | --------------------------------------- | ------------------------------------------------------------ |
| slide.bs.carousel | 当调用 slide 实例方法时立即触发该事件。 | `$('#identifier').on('slide.bs.carousel', function () {     // 执行一些动作... })` |
| slid.bs.carousel  | 当轮播完成幻灯片过渡效果时触发该事件。  | `$('#identifier').on('slid.bs.carousel', function () {     // 执行一些动作... })` |

```js
$('#myCarousel').on('slide.bs.carousel', function () {
  // do something…
})
```



## 13 附加 affix.js

 ### 12.1 基本使用

To easily add affix behavior to any element, just add `data-spy="affix"` to the element you want to spy on. Use offsets to define when to toggle the pinning of an element.

```html
<div data-spy="affix" data-offset-top="60" data-offset-bottom="200">
  ...
</div>
```

### 13.2 JavaScript调用

Call the affix plugin via JavaScript:

```js
$('#myAffix').affix({
  offset: {
    top: 100,
    bottom: function () {
      return (this.bottom = $('.footer').outerHeight(true))
    }
  }
})
```

#### 选项

Options can be passed via data attributes or JavaScript. For data attributes, append the option name to `data-`, as in `data-offset-top="200"`.

| Name   | type                               | default            | description                                                  |
| ------ | ---------------------------------- | ------------------ | ------------------------------------------------------------ |
| offset | number \| function \| object       | 10                 | Pixels to offset from screen when calculating position of scroll. If a single number is provided, the offset will be applied in both top and bottom directions. To provide a unique, bottom and top offset just provide an object `offset: { top: 10 }` or `offset: { top: 10, bottom: 5 }`. Use a function when you need to dynamically calculate an offset. |
| target | selector \| node \| jQuery element | the `window`object | Specifies the target element of the affix.                   |

#### 方法

**`$().affix(options)`**

Activates your content as affixed content. Accepts an optional options `object`.

```
$('#myAffix').affix({
  offset: 15
})
```

** `$().affix('checkPosition')`**

Recalculates the state of the affix based on the dimensions, position, and scroll position of the relevant elements. The `.affix`, `.affix-top`, and `.affix-bottom` classes are added to or removed from the affixed content according to the new state. This method needs to be called whenever the dimensions of the affixed content or the target element are changed, to ensure correct positioning of the affixed content.

```
$('#myAffix').affix('checkPosition')
```

#### 事件

Bootstrap's affix plugin exposes a few events for hooking into affix functionality.

| Event Type              | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| affix.bs.affix          | This event fires immediately before the element has been affixed. |
| affixed.bs.affix        | This event is fired after the element has been affixed.      |
| affix-top.bs.affix      | This event fires immediately before the element has been affixed-top. |
| affixed-top.bs.affix    | This event is fired after the element has been affixed-top.  |
| affix-bottom.bs.affix   | This event fires immediately before the element has been affixed-bottom. |
| affixed-bottom.bs.affix | This event is fired after the element has been affixed-bottom. |