1、条件表达式要放在方括号之间，并且要有空格，例如: **[$a==$b]** 是错误的，必须写成 **[ $a == $b ]**。

2、read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量



##### shell echo命令

1、显示普通字符串

```
echo "It is a test"           # It is a test
```

2、显示转义字符

```
echo "\"Hello World\""        # "It is a test"
```

3、显示变量

read命令从标准输入读取一行，并把输入行的每个字段的值指定给shell变量

```
#!/bin/sh
read name
echo "$name is xxx"
```

```
sh test.sh
yu         #标准输入
yu is xxx  #输出
```

4、转义

```
echo -e "OK! \n"       #-e开启转义
echo "It is a test"


echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"
```

```
OK!

It is a test
OK! It is a test
```

5、显示结果重定向至文件

```
echo "It is a test" > myfile      #会自动创建文件
```

6、原样输出字符串，不进行转义或取变量(取单引号)

```
echo '$name\"'          $name\"
```

7、显示命令执行结果

```
echo `date`
```

##### `printf`命令

另一个输出命令，`printf`命令模仿c程序库(library)里的`printf()`程序

`printf format-string [argument...]`

- format-string:为格式控制字符串

- arguments:为参数列表

  ```
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

  

流程控制

if

```
a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi
```

for循环

```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done

for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done
```

while循环

```
while condition
do
    command
done

#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```

case

Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case语句格式如下：

```
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

`/dev/null `文件

```
command > dev/null
```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：



##### shell编程

之前我们提到过，Shell是一个连接用户和操作系统的应用程序，它提供了人机交互的界面（接口），用户通过这个界面访问操作系统内核的服务。Shell脚本是一种为Shell编写的脚本程序，我们可以通过Shell脚本来进行系统管理，同时也可以通过它进行文件操作。总之，编写Shell脚本对于使用Linux系统的人来说，应该是一项标配技能。

互联网上有大量关于Shell脚本的相关知识，我不打算再此对Shell脚本做一个全面系统的讲解，我们通过下面的代码来感性的认识下Shell脚本就行了。

例子1：输入两个整数m和n，计算从m到n的整数求和的结果。

```Shell
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
echo '结果: '$sum
```

例子2：自动创建文件夹和指定数量的文件。

```Shell
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

例子3：自动安装指定版本的Redis。

```Shell
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
