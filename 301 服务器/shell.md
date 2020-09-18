### 1.Shell解析器

   shell是一个命令行解释器，它接收用户/应用程序命令，然后调用操作系统内核

- Linux提供的Shell解析器有：

  ```
  [root@yu ~]# cat /etc/shells 
  /bin/sh
  /bin/bash
  /usr/bin/sh
  /usr/bin/bash
  ```

- bash和sh的关系
  
  ```
  [root@yu bin]# ll | grep bash
  -rwxr-xr-x    1 root root     964536 Apr  1 10:17 bash
  lrwxrwxrwx    1 root root         10 May 11 17:05 bashbug -> bashbug-64
  -rwxr-xr-x    1 root root       6964 Apr  1 10:17 bashbug-64
  lrwxrwxrwx    1 root root          4 May 11 17:05 sh -> bash
  ```

- Centos默认的解析器是bash

  ```
  echo $SHELL
  ```

### 2.Shell脚本

1. 脚本格式

   第一行#!/bin/bash指定解释器

   ```
   #!/bin/bash
   echo "helloworld"
   ```

2. 执行方式

   - 采用bash或sh+脚本的相对路径或绝对路径（不用赋予脚本执行权限）

     本质是bash解析器帮你执行脚本，所以脚本本身不需要执行权限。

     ```
     bash hello.sh
     ```

   - 采用输入脚本的绝对路径或相对路径执行脚本(必须先赋予可执行权限+x）　

     本质是脚本需要自己执行，所以需要执行权限

     ```
     [root@yu~]# chmod +x hello.sh  
     [root@yu ~]# ./hello.sh
     helloworld
     [root@yu ~]# /root/hello.sh
     helloworld
     ```

   - 多命令处理
     在/root目录下创建一个yu.txt,在yu.txt文件中增加“世界你好”

     ```
     #!/bin/bash
     
     cd /root	
     touch yu.txt
     echo "世界你好" > yu.txt 
     ```

### 3.Shell的变量

#### 3.1 系统变量

- 常用系统变量
  $HOME、$PWD、$SHELL、$USER等

  显示当前Shell中所有变量：set

  ```
  [root@yu data]# $HOME
  bash: /root: Is a directory
  [root@yu data]# $PWD
  bash: /root/data: Is a directory
  ```

#### 3.2 自定义变量

- 基本语法

  - 定义变量：变量=值 

  - 撤销变量：unset 变量

  - 声明静态变量：readonly变量，注意：不能unset

  - 可把变量提升为全局环境变量，可供其他Shell程序使用

    ```
    export 变量名
    ```

- 变量定义规则

  - 等号两侧不能有空格

    ```
    [root@yu ~]# A=6
    [root@yu ~]# echo $A
    6
    ```

  - 变量名称可以由字母、数字和下划线组成，但是不能以数字开头，环境变量名建议大写。

  - 在bash中，变量默认类型都是字符串类型，无法直接进行数值运算。

    ```
    [root@yu ~]# C=3+2
    [root@yu ~]# echo $C
    3+2
    ```

  - 变量的值如果有空格，需要使用双引号或单引号括起来。

    ```
    [root@yu ~]# D="i am"
    [root@yu ~]# echo $D
    i am
    ```
  
- declare 声明变量

  ```
  declare -i ab //声明整数型变量
  ab=56 //改变变量内容
  echo $ab  //显示变量内容
  56     
  ```

  ```
  declare -a cd='([0]="a" [1]="b" [2]="c")' //声明数组型变量
  echo ${cd[1]}   //显示变量内容
  b   
  echo ${cd{@}} //显示整个数组变量内容
  a b c  
  ```

- lcoal

  shell脚本中定义得变量是global,作用域从定义的开始，一直到shell结束或被显式删除的删除为止

  shell函数定义的变量也是global,其作用域从函数被调用执行变量的地方开始，到shell结束或者显式的的删除为止。函数定义的变量也可以是local的，其作用域限于函数内部，但是函数的参数是local的。

  如果局部变量和全局变量名字相同，那么在这个函数内部，会使用局部变量。

#### 3.3 特殊变量：$n

- 基本语法
  	$n（功能描述：n为数字，$0代表该脚本名称，$1-$9代表第一到第九个参数，十以上的参数，十以上的参数需要用大括号包含，如${10}）

  ```
  [root@yu data]# vi t1.sh
  #！/bin/bash
  echo $0
  echo $1 $2
  [root@yu data]# sh t1.sh  0 1
  t1.sh
  0 1
  ```

#### 3.4 特殊变量：$#

- 基本语法
  	$#  (功能描述：获取输入参数个数，常用于循环）

#### 3.5 特殊变量：$*、$@*


	$*	  （功能描述：这个变量代表命令行中所有的参数，$*把所有的参数看成一个整体）
	$@	（功能描述：这个变量也代表命令行中所有的参数，不过$@把每个参数区分对待）

#### 3.6 特殊变量：$？

- 基本语法
  　　$？（功能描述：最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行；如果这个变量的值为非0（具体是哪个数，由命令自己来决定），则证明上一个命令执行不正确了。）
    　　2．案例实操
    	（1）判断helloworld.sh脚本是否正确执行
  [atguigu@hadoop101 datas]$ ./helloworld.sh 
  hello world
  [atguigu@hadoop101 datas]$ echo $?
  0

### 4.运算符		

- 基本语法
  　　1、“$[运算式]”或“$((运算式))”
    　　2、expr  + , - , \*,  /,  %    加，减，乘，除，取余
    　　注意：expr运算符间要有空格

- 案例实操： 

  - 计算3+2的值

    ```
    [root@yu data]# expr 3 + 2
    5
    ```

  - 计算（2+3）X4的值

    ```
    [root@yu data]# expr `expr 2 + 3` \* 4
    20
    ```

  - 采用$[运算式]方式

    ```
    [root@yu data]# s=$[(2+3)*4]
    [root@yu data]# echo $s
    20
    ```

### 5.条件判断

- 基本语法
  　　[ condition ]（注意condition前后要有空格）
    　　注意：条件非空即为true，[ yu ]返回true，[] 返回false

- 两个整数之间比较
  = 字符串比较
  -lt 小于（less than）			-le 小于等于（less equal）
  -eq 等于（equal）				-gt 大于（greater than）
  -ge 大于等于（greater equal）	-ne 不等于（Not equal）

  ```shell
  [root@yu ~]# [ 23 -ge 22 ]
  [root@yu ~]# echo $?
  0
  ```

- 按照文件权限进行判断
  -r 有读的权限（read）			-w 有写的权限（write）
  -x 有执行的权限（execute）

  ```shell
  # yu.txt是否有写权限
  [root@yu ~]# [ -w yu.txt ]
  [root@yu ~]# echo $?
  0
  ```

- 按照文件类型进行判断
  -f 文件存在并且是一个常规的文件（file）
  -e 文件存在（existence）		-d 文件存在并是一个目录（directory）

  ```shell
  # yu1.txt文件是否存在
  [root@yu ~]# [ -e yu1.txt ]
  [root@yu ~]# echo $?
  1
  ```

- 多条件判断（&& 表示前一条命令执行成功时，才执行后一条命令，|| 表示上一条命令执行失败后，才执行下一条命令）

  ```
  [root@yu ~]# [ 23 -ge 22 ] && echo ok || echo "not ok"
  ok
  ```

  ```
  [root@yu ~]# [ 23 -ge 22 ] && [ ] || echo "not ok"
  not ok
  ```

### 6.流程控制

?		exit -1 退出脚本

#### 6.1 if 判断

-  基本语法

  ```
  if [ 条件判断式 ];then 
  程序 
  fi 
  
  
  或者 
  if [ 条件判断式 ] 
  then 
  程序
  fi
  ```

  注意事项：
  　　1、[ 条件判断式 ]，中括号和条件判断式之间必须有空格
  　　2、if后要有空格

- 案例
  　　（1）输入一个数字，如果是1，则输出yu，如果是2，则输出xue，如果是其它，什么也不输出。

  ```
  [root@yu data]# vi if.sh
  #!/bin/bash
  
  if [ $1 -eq 1 ];then
  echo 1
  elif [ $1 -eq 2 ];then
  echo 2
  fi
  ```

#### 6.2 case 语句

- 基本语法

  ```shell
  case $变量名 in 
  "值1"） 
  如果变量的值等于值1，则执行程序1 
  ;; 
  "值2"） 
  如果变量的值等于值2，则执行程序2 
  ;; 
  *） 
  如果变量的值都不是以上的值，则执行此程序 
  ;; 
  esac
  ```

  注意事项：
  1) case行尾必须为单词“in”，每一个模式匹配必须以右括号“）”结束。
  2) 双分号“;;”表示命令序列结束，相当于java中的break。
  3) 最后的“*）”表示默认模式，相当于java中的default。

- 案例
  输入一个数字，如果是1，则输出1，如果是2，则输出2，如果是其它，输出3。

  ```
  #!/bin/bash
  
  case $1 in
  1)
  echo 1
  ;;
  2)
  echo 2
  ;;
  *)
  echo 3
  ;;
  esac
  ```

#### 6.3 for 循环

- 基本语法1

  ```
  for (( 初始值;循环控制条件;变量变化 )) 
  do 
      程序   
  done
  ```

- 案例
  从1加到100

  ```
  #!/bin/bash
  
  s=0
  for ((i=0;i<=100;i++))    #for后空不空格都可以
  do
      s=$[$s+$i]
  done
  
  echo $s
  ```

- 基本语法2

  ```
  for 变量 in 值1 值2 值3… 
  do 
     程序 
  done
  ```

- 案例
  打印所有输入参数

  ```
  #!/bin/bash
  
  for i in $*
  do
  echo "12 $i"
  done
  
  ```
  - 比较$*和$@区别

    ```
    $*和$@都表示传递给函数或脚本的所有参数，不被双引号“”包含时，都以$1 $2 …$n的形式输出所有参数，完全相同
    ```

    ```
    当它们被双引号“”包含时，“$*”会将所有的参数作为一个整体，以“$1 $2 …$n”的形式输出所有参数；“$@”会将各个参数分开，以“$1” “$2”…”$n”的形式输出所有参数。
    ```

#### 6.4 while 循环

- 基本语法

  ```
  while [ 条件判断式 ] 
  do 
     程序
  done
  ```

- 案例
  从1加到100

  ```
  #!/bin/bash
  
  i=1
  s=0
  while [ $i -le 100 ]
  do
    s=$[$i+$s]
    i=$[$i+1]
  done
  
  echo $s
  ```

### 7.read读取控制台输入

- 基本语法
  	read(选项)(参数)
    	选项：-p：指定读取值时的提示符；
                  -t：指定读取值时等待的时间（秒）。
     参数：指定读取值的变量名

- 案例实操
  提示5秒内，读取控制台输入，并赋值给name

  ```
  #!/bin/bash
  
  read -t 5 -p "请在5秒内输入你的名字"  name
  
  echo "$name"
  ```

### 8.函数

#### 8.1 系统函数

- basename基本语法(获得文件名)
  　　basename [string / pathname] [suffix]  	（功能描述：basename命令会删掉所有的前缀包括最后一个（‘/’）字符，然后将字符串显示出来
    　　选项：
    　　suffix为后缀，如果suffix被指定了，basename会将pathname或string中的suffix去掉。

- 案例
  获取/root/data/t1.txt路径的文件名称

  ```
  [root@yu data]# basename /root/data/t1.txt 
  t1.txt
  #去掉后缀
  [root@yu data]# basename /root/data/t1.txt  .txt  
  t1
  ```

- dirname基本语法(获取文件路径,目录路径)
  dirname 文件绝对路径	（功能描述：从给定的包含绝对路径的文件名中去除文件名（非目录的部分），然后返回剩下的路径（目录的部分））

- 案例实操
  获取t1.txt文件的路径

  ```
  [root@yu data]# dirname  /root/data/t1.txt     #要绝对路径
  /root/data
  ```

#### 8.2 自定义函数

- 基本语法

  ```
  [ function ] funname()
  {
  Action;
  [return int;]
  }
  funname
  ```

?       必须在调用函数地方之前，先声明函数，shell脚本是逐行运行。不会像其它语言一样先编译。
?       函数返回值，只能通过$?系统变量获得，可以显示加：return返回，如果不加，将以最后一条命令运行结果，      作为返回值。return后跟数值n(0-255)

- 案例
  计算两个输入参数的和

  ```
  #!/bin/bash
  
  sum(){
  s=0
  s=$[$1+$2]
  echo $s
  }
  sum $1 $2
  
  [root@yu data]# sh fun.sh 1 2
  3
  ```

### 9.Shell工具（重点）

#### 9.1 cut

　　cut的工作就是“剪”，具体的说就是在文件中负责剪切数据用的。cut 命令从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段输出。

- 基本用法
  cut [选项参数]  filename
  说明：默认分隔符是制表符
  选项参数： -f    列号，提取第几列
  					-d   分隔符，按照指定分隔符分割列 

- 案例

  - 数据准备

    ```
    [root@yu data]# vi cut.txt
    
    good day 1
    good day 2
    study up 3　
    ```

  - 切割cut.txt第一列

    ```
    [root@yu data]# cut -d " " -f 1 cut.txt 
    good
    good
    study　
    ```

  - 切割cut.txt第二、三列

    ```
    [root@yu data]# cut -d " " -f 2,3 cut.txt 
    day 1
    day 2
    up 3　
    ```

  - 在cut.txt文件中切割出study

    ```
    [root@yu data]# cat cut.txt | grep "study" | cut -d " " -f 1
    study
    ```

  - 选取系统PATH变量值，第2个“：”开始后的所有路径：

    ```
    [root@yu data]# echo $PATH |cut -d : -f 3-
    [root@yu data]# echo $PATH
    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
    [root@yu data]# echo $PATH |cut -d : -f 3-
    /usr/sbin:/usr/bin:/root/bin
    ```

  - 切割ifconfig 后打印的IP地址

    ```
    [root@yu data]# ifconfig eth0 | grep "inet addr" | cut -d: -f 2 | cut -d" " -f1
    192.168.1.102
    ```

#### 9.2 sed

　　sed是一种流编辑器，它一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”，接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。**文件内容并没有改变**，除非你使用重定向存储输出。

- 基本用法
  sed [选项参数]  ‘command’  filename

- 选项参数
  -e   直接在指令列模式上进行sed的动作编辑。

- 命令功能描述
  a   新增，a的后面可以接字串，在下一行出现
  d  删除
  s   查找并替换 

- 案例

  - 数据准备

    ```
    [root@yu data]# vi sed.txt
    good day
    good day
    study up
    ```

  - 将“你 好”这个单词插入到sed.txt第二行下，打印。

    ```
    [root@yu data]# sed '2a "你好"' sed.txt 
    good day
    good day
    "你好"
    study up
    ```

    注意：文件并没有改变

  - 删除sed.txt文件所有包含good的行

    ```
    [root@yu data]# sed '/good/d' sed.txt 
    study up
    ```

  - 将sed.txt文件中good替换为well

    ```
    [root@yu data]# sed 's/good/well/g' sed.txt 
    well day
    well day
    study up
    ```

    注意：‘g’表示global，全部替换

  - 将sed.txt文件中的第二行删除并将good替换为well

    ```
    [root@yu data]# sed -e '2d' -e 's/good/well/g' sed.txt 
    well day
    study up
    ```

#### 9.3 awk

　　一个强大的文本分析工具，把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行分析处理。

- 基本用法
  awk [选项参数]  ‘pattern1{action1}   pattern2{action2}...’  filename
  pattern：表示AWK在数据中查找的内容，就是匹配模式
  action：在找到匹配内容时所执行的一系列命令

    **‘pattern1{action1}’** 是单引号不是双引号

- 选项参数说明
  -F : 指定输入文件折分隔符
  -v : 赋值一个用户定义变量

- 案例实操

  - 数据准备

    ```
    [root@yu data]# cp /etc/passwd ./
    [root@yu data]# cat passwd
    ```

  - 搜索passwd文件以root关键字开头的所有行，并输出该行的第7列。

    ```
    [root@yu data]# awk -F : '/^root/{print $7}' passwd 
    /bin/bash
    ```

    注意：只有匹配了pattern的行才会执行action

  - 搜索passwd文件以root关键字开头的所有行，并输出该行的第1列和第7列，中间以“，”号分割。

    ```
    [root@yu data]# awk -F : '/^root/{print $1,$7}' passwd 
    root /bin/bash
    ```

  - 只显示/etc/passwd的第一列和第七列，以逗号分割，且在第一行前面添加user，shell。在最后一行添加"hello,world"。

    ```
    [root@yu data]# awk -F : 'BEGIN{print "user,path"} {print $1","$7} END{print "hello,world"}' passwd 
    user,path
    root,/bin/bash
    bin,/sbin/nologin
    dockerroot,/sbin/nologin
    hello,world
    ```

    注意：BEGIN 在所有数据读取行之前执行；END 在所有数据执行之后执行。

  - 将passwd文件中的用户id增加数值1并输出

    ```
    [root@yu data]# awk -F: '{print $3+1}' passwd
    或
    [root@yu data]# awk -v i=1 -F: '{print $3+1}' passwd
    ```

- awk的内置变量

  变量
  FILENAME    文件名
  NR                 已读的记录数
  NF                  浏览记录的域的个数（切割后，列的个数）

- 案例实操

  - 统计passwd文件名，每行的行号，每行的列数

    ```
    [root@yu data]#  awk -F: '{print "filename:"  FILENAME ", linenumber:" NR  ",columns:" NF}' passwd 
    filename:passwd, linenumber:1,columns:7
    filename:passwd, linenumber:2,columns:7
    ```

  - 切割IP

    ```
    [root@yu data]# ifconfig eth0| grep "inet" | awk -F " " '{print $2}'
    172.26.31.191
    ```

  - 查询sed.txt中空行所在的行号

    ```
    [root@yu data]# awk '/^$/{print NR}' sed.txt 
    4
    ```

#### 9.4 sort

　　sort命令是在Linux里非常有用，它将文件进行排序，并将排序结果标准输出。

- 基本语法
  sort(选项)(参数)
  选项
  -n   依照数值的大小排序
  -r   以相反的顺序来排序
  -t   设置排序时所用的分隔字符
  -k   指定需要排序的列
  参数：指定待排序的文件列表

- 案例实操

  - 数据准备

    ```
    [root@yu data]# vim sort.sh
    bb:40:5.4
    bd:20:4.2
    xz:50:2.3
    cls:10:3.5
    ss:30:1.6
    ```

  - 按照“: ”分割后的第三列倒序排序。

    ```
    [root@yu data]# sort -t : -nrk 3 sort.sh 
    bb:40:5.4
    bd:20:4.2
    cls:10:3.5
    xz:50:2.3
    ss:30:1.6
    ```

#### 9.5 echo命令  

1、显示普通字符串

```
echo "It is a test"           # It is a test
```

2、显示转义字符

```
echo "\"Hello World\""        # "It is a test"
```

3、显示变量

```
echo "$name is xxx"
```

4、转义

```
echo -e "OK! \n"      # OK! 
echo  "Ok! \n"        # OK! \n

echo -e "OK! \c" # -e 开启转义 \c 下一个显示不换行
```

5、显示结果重定向至文件

```
echo "It is a test" > myfile      #会自动创建文件
```

6、原样输出字符串，不进行转义或取变量(单引号)

```
[root@yu data]# name=yu
[root@yu data]# echo '$name'
$name
[root@yu data]# echo "$name"
yu
```

7、显示命令执行结果

```
echo `date`
```

8、printf 另一个输出命令

printf format-string [argument...]

- format-string:为格式控制字符串，arguments:为参数列表

- ```
  #!/bin/bash
  # author:菜鸟教程
  # url:www.runoob.com
   
  printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
  printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
  printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
  printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876 
  ```

  ```
  #执行结果
  姓名     性别   体重kg
  郭靖     男      66.12
  杨过     男      48.65
  郭芙     女      47.99
  %s %c %d %f都是格式替代符
  
  %-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。
  %-4.2f 指格式化为小数，其中.2指保留2位小数。
  ```

### 第10章 企业面试题

####   10.1 京东

- 使用Linux命令查询file1中空行所在的行号

  ```
  [root@yu data]# awk '/^$/{print NR}' file1
  2
  ```

- 有文件chengji.txt内容如下:
    　　张三 40
    　　李四 50
    　　王五 60
    　　使用Linux命令计算第二列的和并输出

  ```
  cat chengji.txt | awk -F " " '{sum+=$2} END{print sum}'   #这里sum不要$sum
  ```

####  10.2 搜狐&和讯网

- Shell脚本里如何检查一个文件是否存在？如果不存在该如何处理？

  ```
  #!/bin/bash
  
  if [ -f file.txt ]; then
     echo "文件存在!"
  else
     echo "文件不存在!"
  fi
  ```

#### 10.3 新浪

- ：用shell写一个脚本，对文本中无序的一列数字排序,并求和

  ```
  [root@yu data]# cat test.txt 
  9
  8
  7
  6
  5
  4
  3
  2
  10
  1
  ```

  ```
  [root@yu data]# sort -n test.txt 
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  ```

  ```
  [root@yu data]# sort -n test.txt | awk '{sum+=$1;print $1} END{print "sum="sum}'
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  sum=55
  ```

#### 10.4 金和网络

- 请用shell脚本写出查找当前文件夹（/root/data）下所有的文本文件内容中包含有字符”bin/bash”的文件名称

  ```
  [root@yu data]# grep -r "bin/bash" /root/data | awk -F : '{print $1}'
  /root/data/if.sh
  /root/data/read.sh
  /root/data/hello.sh
  ```

#### 10.5 其他

- 输入两个整数m和n，计算从m到n的整数求和的结果

  ```
  #!/usr/bin/bash
  printf 'm = '
  read m
  printf 'n = '
  read n
  a=$m
  sum=0
  while [ $a -le $n ]
  do
      sum=$[ sum + a ]
      a=$[ a + 1 ]
  done
  echo 、"结果是: $sum"
  ```

- 自动创建文件夹和指定数量的文件(...)

  ```
  #!/usr/bin/bash
  printf '输入文件名: '
  read file
  printf '输入文件数量(<1000): '
  read num
  if [ $num -ge 1000 ]
  then
      echo '文件数量不能超过1000'
  else
      if [ -e $dir -a -d $dir ]
      then
          rm -rf $dir
      else
          if [ -e $dir -a -f $dir ]
          then
              rm -f $dir
          fi
      fi
      mkdir -p $dir
      index=1
      while [ $index -le $num ]
      do
          if [ $index -lt 10 ]
          then
              pre='00'
          elif [ $index -lt 100 ]
          then
              pre='0'
          else
              pre=''
          fi
          touch $dir'/'$file'_'$pre$index
          index=$[ index + 1 ]
      done
  fi
  ```

- 自动安装指定版本的Redis(...)

  ```
  #!/usr/bin/bash
  install_redis() {
      if ! which redis-server > /dev/null
      then
          cd /root
          wget $1$2'.tar.gz' >> install.log
          gunzip /root/$2'.tar.gz'
          tar -xf /root/$2'.tar'
          cd /root/$2
          make >> install.log
          make install >> install.log
          echo '安装完成'
      else
          echo '已经安装过Redis'
      fi
  }
  
  install_redis 'http://download.redis.io/releases/' $1
  ```

  