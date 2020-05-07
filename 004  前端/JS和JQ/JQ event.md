#  jQuery事件机制

## 1 事件操作

### 1.1 页面载入事件

```js
$(document).ready(function(){
  // 在这里写你的代码...
});
或者
$(function($) {
  // 你可以在这里继续使用$作为别名...
});
```



### 1.2 事件绑定

```
on(eve,[sel],[data],fn)  	1.7+ 在选择元素上绑定一个或多个事件的事件处理函数
bind(type,[data],fn)	 	3.0- 请使用on()
one(type,[data],fn)			为每一个匹配元素的特定事件（像click）绑定一个一次性的事件处理函数
```



### 1.3 解除事件绑定

```
off(eve,[sel],[fn])     	1.7+ 在选择元素上移除一个或多个事件的事件处理函数
unbind(t,[d|f])				3.0- 请使用off()
```

### 1.4 触发事件

```
trigger(type,[data])		 在每一个匹配的元素上触发某类事件

triggerHandler(type, [data]) 
这个特别的方法将会触发指定的事件类型上所有绑定的处理函数。但不会执行浏览器默认动作，也不会产生事件冒泡
这个方法的行为表现与trigger类似，但有以下三个主要区别：
* 第一，他不会触发浏览器默认事件。
* 第二，只触发jQuery对象集合中第一个元素的事件处理函数。
* 第三，这个方法的返回的是事件处理函数的返回值，而不是据有可链性的jQuery对象。此外，如果最开始的jQuery对象集合为空，则这个方法返回 undefined 。
```



### 1.5 事件委派

```
live(type,[data],fn)	1.7-
die(type,[fn])			1.7-
delegate(s,[t],[d],fn)	3.0-
undelegate([s,[t],fn])	3.0-
全部移除了，请使用 on()
```

```js
$(document).on('click', 'button', fn)
```



### 1.6 事件切换

```
hover([over,]out)		   一个模仿悬停事件（鼠标移动到一个对象上面及移出这个对象）的方法
toggle([spe],[eas],[fn])   1.9-用于绑定两个或多个事件处理器函数，以响应被选元素的轮流的 click 事件
```

## 2 事件列表

```
blur([[data],fn])
change([[data],fn])
click([[data],fn])
dblclick([[data],fn])
error([[data],fn])
focus([[data],fn])
focusin([data],fn) 		
	当元素获得焦点时，触发 focusin 事件。 focusin事件跟focus事件区别在于，他可以在父元素上检测子元素获取焦点的情况

focusout([data],fn)
	当元素失去焦点时触发 focusout 事件。focusout事件跟blur事件区别在于，他可以在父元素上检测子元素失去焦点的情况。

keydown([[data],fn])
keypress([[data],fn])
keyup([[data],fn])
mousedown([[data],fn])
mouseenter([[data],fn])
	当鼠标指针穿过元素时，会发生 mouseenter 事件。该事件大多数时候会与mouseleave 事件一起使用。与 mouseover 事件不同，只有在鼠标指针穿过被选元素时，才会触发 mouseenter 事件。如果鼠标指针穿过任何子元素，同样会触发 mouseover 事件。

mouseleave([[data],fn])
	当鼠标指针离开元素时，会发生 mouseleave 事件。该事件大多数时候会与mouseenter 事件一起使用。与 mouseout 事件不同，只有在鼠标指针离开被选元素时，才会触发 mouseleave 事件。如果鼠标指针离开任何子元素，同样会触发 mouseout 事件。

mousemove([[data],fn])
mouseout([[data],fn])
mouseover([[data],fn])
mouseup([[data],fn])
resize([[data],fn])
scroll([[data],fn])
select([[data],fn])
submit([[data],fn])
unload([[data],fn])
```

## 3 事件对象

**属性**

```
eve.currentTarget		在事件冒泡阶段中的当前DOM元素
eve.data				当前执行的处理器被绑定的时候，包含可选的数据传递给jQuery.fn.bind
eve.delegateTarget		1.7+ 当currently-called的jQuery事件处理程序附加元素
eve.namespace			当事件被触发时此属性包含指定的命名空间
eve.pageX				鼠标相对于文档的左边缘的位置
eve.pageY				鼠标相对于文档的顶部边缘的位置
eve.relatedTarget		在事件中涉及的其它任何DOM元素
eve.result				这个属性包含了当前事件事件最后触发的那个处理函数的返回值，除非值是 undefined
eve.target				最初触发事件的DOM元素
eve.timeStamp			返回事件触发时距离1970年1月1日的毫秒数
eve.type				事件类型
eve.which				针对键盘和鼠标事件，这个属性能确定你到底按的是哪个键或按钮
```

**方法**

```
eve.preventDefault()			阻止默认事件行为的触发
eve.isDefaultPrevented()		根据事件对象中是否调用过 event.preventDefault() 方法来返回一个布尔值
eve.stopPropagation()			防止事件冒泡到DOM树上，也就是不触发的任何前辈元素上的事件处理函数
eve.isPropagationStopped()		检测 event.stopPropagation() 是否被调用过
eve.stopImmediatePropagation() 	阻止剩余的事件处理函数执行并且防止事件冒泡到DOM树上
eve.isImmediatePropagation() 	检测 event.stopImmediatePropagation() 是否被调用过
```

