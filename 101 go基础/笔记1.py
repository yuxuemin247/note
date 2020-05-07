
昨日回顾：
	1 go语言的介绍
	2 go语言安装，环境搭建
	3 go语言关键字和保留关键字
	4 变量命名规范
	5 变量定义：
		-变量一定要先定义再使用
		-变量的类型不能改变
		-var 变量名 变量类型 = 变量值
		-类型推到 var 变量名 =值
		-简短定义：变量名1,变量名2：=值1，值2
		-常量（恒定不变的量）：
			const 变量名 =变量值
			
	6 函数
		-func 函数名(){
			函数体内容
			}
		-有参数（一个参数，多个参数，多个同类型参）
			-func test(x int,y string)
			-func test(x ,y int)
		-有返回值
			-一个返回值（必须加返回值类型）
			-多个返回值（用括号包裹）
			-命名返回值：func test(a,b int )(c int,d string){
		-可变长参数
			-func test2(a ... int){
	7 if ---else if ---else	
		-if 后跟条件{
		}else if 后跟条件{
		}else{
		}
	8 循环
		-典型使用
			for i:=0;i<10 ; i++ {
			
			}
		-模拟while循环
		 for 条件{
		 }
		-死循环
			for {
			 }
			 
	9 switch（用于替换else if这种逻辑判断）
		i := 10
		switch i {
		case 1:
			fmt.Println("我是1")
		case 10:
			fmt.Println("我是1")
			fallthrough
		case 12:
			fmt.Println("我是1")
		}
				
	10 数组
		-定义：遵循变量定义a:=[3]int{1,2,3}
		-数组大小确定后，不能更改
		-数组是值类型（修改了b不会影响a）
		-数组的迭代
			a := [3]int{1, 2, 3}
			for i := 0; i < len(a); i++ {
				fmt.Println(a[i])
			}
			for i, v := range a {
				//for i:=range a{
				fmt.Println(i, "------", v)
				//fmt.Println(i)
			}
			
今日内容：
	切片
		
		
		