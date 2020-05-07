匿名函数

```go
	a:= func() {
		fmt.Println("cccc")
	}
	a()
```

闭包

```go
package main

import "fmt"
//闭包函数，x地址都一样，用的是同一个x
func main(){
	f:=closure(10)
	fmt.Println(f(1))
	fmt.Println(f(2))
}

func closure(x int) func(int) int  {
	fmt.Printf("%p\n",&x)
	return func(y int) int {
		fmt.Printf("%p\n",&x)
		return x+y
	}
}

```

defer

![image-20190619004059061](http://ww4.sinaimg.cn/large/006tNc79ly1g465mld64fj31ny0u0gvz.jpg)

```go
package main

import "fmt"

//闭包函数，x地址都一样，用的是同一个x
func main(){
	//第一
	//fmt.Println("a")
	//defer fmt.Println("b")
	//defer fmt.Println("c")
	//第二
	//for i:=0;i<3 ;i++  {
	//	defer fmt.Println(i)
	//}
	//第三
	//闭包，i一直是引用
	for i:=0;i<3 ;i++  {
		defer func() {
			fmt.Println(i)
		}()
	}
}


```

panic和recover

panic基本使用

```go
package main

import "fmt"
func main(){
	A()
	B()
	C()
}


func A(){
	fmt.Println("A")
}
func B(){
	panic("出错了")
}

func C(){
	fmt.Println("C")
}
```

panci+recover

```go
package main

import "fmt"
func main(){
	A()
	B()
	C()
}


func A(){
	fmt.Println("A")
}
func B(){
	defer func() {
		//err不为nil时，表示恐慌状态（出错）
		if err:=recover();err!=nil{
			fmt.Println("恢复B")
		}
	}()
	panic("出错了")
}

func C(){
	fmt.Println("C")
}

```

分析如下结果：

```go
package main

import "fmt"

func main(){
	var fs=[4]func(){}
	for i :=0;i<4;i++{

		defer fmt.Println("defer i = ",i)
		defer func() {
			fmt.Println("defer_closure i=",i)

		}()
		fs[i]= func() {
			fmt.Println("closure i =",i)
		}
	}
	for _ ,f:=range fs{
		f()
	}

}


```

结构体struct

![image-20190619011115178](http://ww3.sinaimg.cn/large/006tNc79ly1g465mm2336j31es0u0k1t.jpg)

基本使用：

```go
package main

import "fmt"

type test struct {
	
}
func main(){
	a:=test{}
	fmt.Println(a)

}


```

使用

```go
package main

import "fmt"

type person struct {
	Name string
	Age int

}
func main(){
	//a:=person{}
	////赋值
	//a.Name="lqz"
	//a.Age=18


	//初始化
	a:=person{
		Name:"lqz",
		Age:18,
	}
	fmt.Println(a)
	//a 是值类型，在函数传递是值拷贝
	A(a)
	fmt.Println(a)
	//要修改原值，需要用指针
	B(&a)
	fmt.Println(a)
	//或者在定义a的时候，直接就用地址
	b:=&person{
		Name:"lqz",
		Age:18,
	}
	//也可以修改，不需要*
	b.Age=99
	//(*b).Age=10
	B(b)
	fmt.Println(b)

}

func A(per person)  {
	per.Age=100
	fmt.Println(per)

}

func B(per *person)  {
	per.Age=100
	fmt.Println(per)

}
```

匿名结构体

```go
	a:= struct {
		Name string
		Age int
	}{
		Name:"lqz",
		Age:19,
	}
```

结构体嵌套

```go
package main

import "fmt"

type person struct {
	Name string
	Age int
	Contact struct{
		Phone,City string

	}
}
func main(){
	a:=person{Name:"lqz",Age:19}
	a.Contact.Phone="1222222"
	a.Contact.City="shanghai"
	fmt.Println(a)
}


```

匿名字段

```go
package main

import "fmt"

type person struct {
	string
	int

}
func main(){
	//顺序不能反
	a:=person{"lqz",19}
	fmt.Println(a)
}


```

结构体比较

```go
package main

import "fmt"

type person struct {
	Name string
	Age int

}
type person2 struct {
	Name string
	Age int


}

func main(){
	//顺序不能反
	a:=person{"lqz",19}
	//b:=a
	b:=person{"lqz",19}
	fmt.Println(a==b)
	
	c:=person2{"lqz",19}
	fmt.Println(a==c)
}


```

模拟继承，组合

```go
package main

import "fmt"

type human struct {
	Sex int

}
type teacher struct {
	//相当于匿名字段
	human
	Name string
	Age int


}

func main(){
	a:=teacher{Name:"lqz",Age:19}
	fmt.Println(a)

	//给Sex赋值
	//方法一
	b:=teacher{Name:"lqz",Age:19,human:human{Sex:1}}
	fmt.Println(b)
	//b.human.Sex=0
	b.Sex=10
	fmt.Println(b)

}


```



接口

![image-20190620003952489](http://ww4.sinaimg.cn/large/006tNc79ly1g46xx0ss0pj314g0l04qp.jpg)



接口基本定义使用

```go
package main

import "fmt"

//定义一个接口，内部有Name方法，返回值为string
type USB interface {
	Name() string
	Connect()
}
//定义一个结构体
type PhoneConnecter struct {
	name string
}

//给PhoneConnect结构体绑定方法
func (pc PhoneConnecter) Name()string{
	return pc.name
}

func (pc PhoneConnecter) Connect(){
	fmt.Println("连接",pc.name)
}
func main(){
	//定义一个接口类型变量a
	var a USB
	//只要是实现了USB接口中所有方法的结构体，都属于USB类型
	a=PhoneConnecter{"PhoneConnecter"}
	//调用结构体a的连接方法
	a.Connect()

	//执行Disconnect函数
	//a 实现了USB的所有接口，所以就是USB类型，可以传递
	Disconnect(a)


}

func Disconnect(usb USB)  {
	fmt.Println("断开连接")

}


```

接口的嵌入结构

```go
//定义一个connecter接口,可以把该接口嵌入到另一个接口中
type Connecter interface {
	Connect()
}
type USB interface {
	Name() string
	Connecter
}
```

类型判断

```go
func Disconnect(usb USB)  {

	//类型判断
	if pc,ok:=usb.(PhoneConnecter);ok{
		fmt.Println("断开连接",pc.name)
		return
	}
	fmt.Println("未知设备")

}
```

空接口（相当于python中的object类）

```go
//定义一个空接口，所有类型都实现了空接口
type empty interface {
	
}
```

通过switch判断结构体属于什么类型

```go
//通过switch结构判断属于什么类型
//func Disconnect(usb empty)  {
func Disconnect(usb interface{})  {
	//switch结构判断类型
	switch v:=usb.(type) {
	case PhoneConnecter:
		fmt.Println("断开连接",v.name)
	default:
		fmt.Println("未知类型")
	}

}
```

接口转换（只能从多的向少的转）

```go
	//定义一个PhoneConnecter并初始化
	pc:=PhoneConnecter{"PC connecter"}
	//定义一个Connecter
	var a Connecter
	//将pc强制转换为Connecter类型
	a=Connecter(pc)
	a.Connect()
```

向上转换会报错

```go

//定义一个TVConnecter
type TVConnecter struct {
	name string
}
//只实现一个connect方法
func (tv TVConnecter) Connect()  {
	fmt.Println("连接",tv.name)
}


//在main函数中（报错）
	tv:=TVConnecter{"Tv Connector"}
	var a USB
	a=USB(tv)

```

类型转换时，是值的拷贝，而不是引用

```go
	pc:=PhoneConnecter{"phone"}
	var a Connecter
	//强制类型转换时，是值的拷贝，而不是引用
	a=Connecter(pc)
	a.Connect()
	pc.name="pppp"
	a.Connect()
```

空接口默认值为nil

```go
var a interface{}
fmt.Println(a==nil)

//定义一个指向int类型的指针，为nil
var p *int  = nil
//让a等于p
a=p
//false，a不为nil，a存的是指向nil的指针，不为空，所以不是nil
fmt.Println(a==nil)
fmt.Println(p==nil)
```

反射

![image-20190620015816936](http://ww3.sinaimg.cn/large/006tNc79ly1g47063wizlj313q0dmh2k.jpg)

基本使用，获取结构体的名字，结构体中属性值，数据类型以及值

 ```go
package main

import (
	"fmt"
	"reflect"
)
//定义一个User结构体
type User struct {
	Id int
	Name string
	Age int
}
//绑定一个hello方法
func (u User)Hello(){
	fmt.Println("hello world")

}
func main(){
	a:=User{}
	Info(a)

}


//定义一个函数，接受任意类型参数
func Info(o interface{}){
	//通过反射，获取o的类型
	t:=reflect.TypeOf(o)
	//打印o的类型
	fmt.Println(t)
	fmt.Println(t.Name())

	//打印所包含的字段
	v:=reflect.ValueOf(o)
	fmt.Println("Fields:")
	//t.NumField() 结构体中元素个数
	for i:=0;i<t.NumField();i++{
		//或得结构体的具体字段
		f:=t.Field(i)

		//取出字段的值
		val:=v.Field(i).Interface()
		//f.Name 字段名字
		//f.Type 字段类型
		fmt.Printf("%s:%v=%v\n",f.Name,f.Type,val)
	}
}

 ```

取得方法信息

```go
	//t.NumMethod() t类型方法的个数
	for i:=0;i<t.NumMethod();i++{
		//反射出方法来
		m:=t.Method(i)
		fmt.Printf("%s  : %v\n",m.Name,m.Type)


	}
```

注意在调用Info的时候如果传指针，函数内部需要判断传入的是否是结构体类型

```go
a:=User{}
Info(&a)


//Info函数

//定义一个函数，接受任意类型参数
func Info(o interface{}){
	//通过反射，获取o的类型
	t:=reflect.TypeOf(o)
	//打印o的类型
	fmt.Println(t)
	fmt.Println(t.Name())

	//打印所包含的字段
	v:=reflect.ValueOf(o)
	fmt.Println("Fields:")
	//判断一下传入的值是否是结构体类型
	//t.Kind() 返回是什么类型-------------
	//k!=reflect.Struct  k 不为结构体类型时，直接跳出
	if k:=t.Kind();k!=reflect.Struct{
		fmt.Println("错误，不是结构体类型")
		return
	}
//--------------------end

	//t.NumField() 结构体中元素个数
	for i:=0;i<t.NumField();i++{
		//或得结构体的具体字段
		f:=t.Field(i)

		//取出字段的值
		val:=v.Field(i).Interface()
		//f.Name 字段名字
		//f.Type 字段类型
		fmt.Printf("%s:%v=%v\n",f.Name,f.Type,val)

	}
	//t.NumMethod() t类型方法的个数
	for i:=0;i<t.NumMethod();i++{
		//反射出方法来
		m:=t.Method(i)
		fmt.Printf("%s  : %v\n",m.Name,m.Type)


	}


}
```

反射匿名字段

```go
package main

import (
	"fmt"
	"reflect"
)

//定义一个User结构体
type User struct {
	Id int
	Name string
	Age int
}


type Manager struct {
	User
	title string
}
func main(){

	m:=Manager{User:User{1,"ok",12},title:"123"}
	//取出m的类型
	t:=reflect.TypeOf(m)

	//取到
	//fmt.Printf("%v\n",t.FieldByIndex([]int{0,0}))
	//打印出第0个字段的详情，Anonymous表示是否匿名
	//fmt.Printf("%#v\n",t.Field(0))

	//取到第0个字段内的第0个值，传切片  取到的就是id
	fmt.Printf("%#v\n",t.FieldByIndex([]int{0,0}))
	//取到第0个字段内的第0个值，传切片 取到的就是Name
	fmt.Printf("%#v\n",t.FieldByIndex([]int{0,1}))
}


```

通过反射修改int类型的值

```go
func main(){
	x:=123
    //取变量的值，注意要传指针，通过内存地址进行操作
	v:=reflect.ValueOf(&x)
	//通过Elem获取变量的value，调用setInt方法设置值为999
	v.Elem().SetInt(999)
	fmt.Println(x)
}
```

并发

-并发concurrency
​	-很多人都是冲着Go打死宣扬的高并发而忍不住跃跃欲试，但其实从源码的解析来看
​	goroutine只是由官方实现的超级“线程池”而已。不过话说回来，每个实例4-5kb的栈内存占用
​	和由于实现机制而大幅减少的创建和销毁开销，是制造Go号称高并发的原因。另外goroutine的简单易用，也在语言层面上给予了开发者巨大的遍历
​	-并发不是并行：
​		并发主要由切换时间片来实现“同时”运行
​		并行则是直接利用多核实现多线程的运行
​	-goroutine奉行通过通信来共享内存，而不是共享内存来通信
​	-基本使用
​		-定义函数：
​			func goroutine(){
​				fmt.Println("go go go")
​			}
​		-调用：
​			go goroutine()
​			//睡两秒
​			time.Sleep(2*time.Second)
​	-通信（channel）
​		-channel是goroutin沟通的桥梁，大都是阻塞同步的
​		-通过make创建，close关闭
​		-channel是引用类型
​		-可以通过for range 来迭代不断操作channel
​		-可以设置缓存大小，在未被填满前不会发生阻塞
​	-goroutin+channel
​		//定义一个channel
​		c := make(chan bool)
​		go func() {
​			fmt.Println("go go go")
​			//把true写入channel
​			c <- true
​		}()
​		//取出channel中的值，程序刚到这，取不到值，会等待，匿名函数执行完成放入值，才能取出来
​		<-c
​	-for range 迭代channel
​		c := make(chan bool)
​		go func() {
​			fmt.Println("go go go")
​			c <- true
​			//在对channel类型进行迭代操作的时候，必须在某个地方关闭，并且关系成功，否则会造成死锁
​			close(c)
​		}()
​		for v:=range c{
​			fmt.Println(v)
​		}
​	-有缓存和无缓存
​		-无缓存是同步阻塞的
​			//定义一个无缓存的channel
​			c := make(chan bool)
​			go func() {
​				fmt.Println("go go go")
​				<-c
​			}()
​			//无缓存channel，值放进去，会等待着读，程序不会结束，直到有人读出来，所以看到的效果是go go go打印
​			c<-true
​			

		-有缓存是异步的，不会阻塞，值放进去就不管了，不会等待读
			//定义一个有缓存的channel
			c := make(chan bool,1)
			go func() {
				fmt.Println("go go go")
				<-c
			}()
			//有缓存channel，值放进去，不会等待着读，程序结束，看到的效果是go go go没有打印
			c<-true
	-通过有缓存channel实现等待所有任务执行完成
			-定义函数：
				func goroutin(c chan bool, index int) {
					//定义一个变量a为1
					a := 1
					for i := 0; i < 1000000; i++ {
						//循环1百万次，+1
						a++
					}
					fmt.Println(index, a)
					c <- true
				}
			-main函数中调用
				//runtime.NumCPU()获取cpu个数
				//使用多核优势，多核同时执行
				runtime.GOMAXPROCS(runtime.NumCPU())
				//定义一个缓存大小为10的channel
				c := make(chan bool, 10)
				for i := 0; i < 10; i++ {
					go goroutin(c, i)
				}
				//	循环结束，c中被放了10个true
				for i := 0; i < 10; i++{
					<-c
					//a:=<-c
					//fmt.Println(a)
				}
				
	-通过withgroup实现等待所有任务执行完成（同步包实现多个goroutin打印内容）
			-定义函数
				func goroutin(wg *sync.WaitGroup, index int) {
					//定义一个变量a为1
					a := 1
					for i := 0; i < 100000; i++ {
						a++
					}
					fmt.Println(index, a)
					//	每执行完一个任务，调一下Done，表示该任务完成
					wg.Done()
	
				}
			-main函数中调用	
				runtime.GOMAXPROCS(runtime.NumCPU())
				//定义一个空的WaitGroup
				wg := sync.WaitGroup{}
				//增加10个任务
				wg.Add(10)
				for i := 0; i < 10; i++ {
					//传入wg的引用
					go goroutin(&wg, i)
				}
				//等待所有任务完成
				wg.Wait()