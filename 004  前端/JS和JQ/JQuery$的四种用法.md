


    <script>
        //$函数参数是一个匿名函数或箭头函数，传入的函数是页面加载完成要去执行的回调函数
        $(function(){
            console.log('页面加载完成')
    })
        //$函数的参数是一个样式表选择器，获取页面元素得到一个JQuery对象,JQuery是伪数组，内部元素是原生的js。JQuery它有更多的属性,更方便
        $('#app>ul>li>a').on('click',(evt) =>{
            evt.preventDefault() //阻止标签的原生事件，如a标签的跳转
        //$函数的参数是一个原生的javaScript对象，返回与原生javaScript对象对应的JQuery对象
        $(evt.target).parent().remove()
    })
    $('#but11').on('click',()=>{
    $('#app>ul').append(
        // $函数的参数是一个标签字符串(创建一个元素,并获得对应的JQuery对象)
        $('<li></li>').text('水果').append(
        $('<a></a>').text('x')
        )
    )
    })
</script>