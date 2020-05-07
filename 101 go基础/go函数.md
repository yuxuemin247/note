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



