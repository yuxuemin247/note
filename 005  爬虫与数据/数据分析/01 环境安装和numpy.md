1、数据分析环境搭建	

```
1）自己搭建开发环境
		安装了3.6.8python（自定义安装目录,读写操作都有权限）
		配置环境变量( 要配两个,script是pip的环境变量)
		数据分析环境：numpy、pandas、jupyter、scipy、sklearn、matplotlib、tensorflow、seaborn、pyecharts……
		直接pip install  xxx 安装即可,需要什么安装什么
		jupyter，数据分析开发工具，浏览器中编写代码，命令行启动jupyter：jupyter notebook
		命令行一直运行，后端，浏览器，前端
		命令行中写代码，映射到浏览器，写代码灵活
		jupyter notebook在哪启动时，位置在哪里，浏览器目录就是当前目录
```

```
2)使用anaconda集成开发环境
   一路下一步安装即可(修改安装目录)
				配置环境变量
				启动jupyter:jupyter notebook
				jupyter notebook 在哪启动时，位置在哪里，浏览器目录就是当前目录
```

##### 3 .`jupyter`介绍(其实就是命令行加浏览器可视化)

   数据分析开发工具(有点类似于`pycharm`,完全可以在`pycharm`中写,`txt`中写)

​    使用:创建的代码文件后缀名是 `.ipynb` `ipython notebook的缩写`   ` jupyter继承ipython`

   ` jupyter`中有运行单元,单元中写代码,写代码规则和python完全一样的

```
    状态栏run,单击运行  Ctrl + Enter   
			          ALt  + Enter  运行本单元并且插入新单元

     插入新的代码单元
     a above   上面插入一行
     b bellow  下面插入一行
     删除 DD
     
     导包时  Table 提示功能 (pycharm导包ALT +Enter)
     方法参数,API提示
     		shift +table
 			pycharm中是ctrl + p
 	 单元格左边 *号 表示正在运行 		
     魔法指令:
     		代码运行计时 %time 一行代码   只能%time当前行的运行时间
     		           
     		           #%%time上一行连注释都不能有
     		           %%time   #跨行
                         代码
      
                       %%timeit
                       代码
                       计算平均的运行时间(应用代码运行时间比较短)
      %lsmagic  显示所有的魔法指令(一些常用linux指令),魔法指令使jupyter更加灵活                
      比如 %ls 显示当前文件目录
      
      markdown 
      		 键盘输入m就转化成markdown
      集成:代码,图片,公式,注释,markdown于一体的超级web页面
```

#####   2 `Numpy`使用   

```
 numeric(数字化) Python
 numpy包的核心是ndarray对象,n维数组 
 numpy和之前的列表相似,功能更加强大,对象封装了常用计算方法
 运行速度很快,c,c++
```

###### `numpy`对象的创建

​	`

- `np.array(列表)`

- 使用`np`的routines函数创建

  - ```
    import numpy as np
    #生成4行5列的二维矩阵,数字用0~100之间随机数填充
    np.random.randint(0,100,size=(4,5))
    #标准正态分布,dimession维度 平均值为0,方差为1
    np.random.randn(d0,d1,...dn)
    # loc为平均值,scale 标准差,偏差 size个数 round保留2位
    np.random.normal(loc=175,scale=10,size=1000).round(2)
    ```

  - ```
    #shape 形状 4行5列(二维) 有几个数就是几维
    np.ones(shape=(4,5),dtype=np.int8)
    np.zeros(shape=(4,5),dtype=float,order='c')
    #c 只是代表存储时是按行还是列存
    np.full(shape=(4,5),fill_value=3)
    #用3来填充
    #单位矩阵(对角线)
    np.eye(N=5) 
    ```

  - ```
    #等差数列,左闭右闭,生成100个
    np.linspace(0,99,num=100)
    #等差数列,左闭右开,步长为2
    np.arrage(0,100,2)
    ```

###### `ndarray`的属性

- 4个必记参数 

  - ```
    ndim 维度
    shape 形状(各维度的长度)
    size 总长度
    dtype 元素类型
    ```

###### `ndarray`的基本操作

- 索引

  - 一维与列表完全一致,多维之间用`,`隔开

    ```
    nd2 = np.random.randint(0,100,size=(4,5))
    nd2
    array([[28, 97, 20, 77, 67],
           [87, 32, 39, 11, 37],
           [24,  9, 95, 38,  9],
           [55, 47, 20, 28, 77]])
    nd2[0,2] 值为20
    nd2[2]   值为[24,9,95,38,9]
    # 根据索引修改数据
    nd2[0,2] =100
    ```

- 切片

  一维相同,多维`,`隔开

  ```
  nd2[0:2,0:2] 
  ```

- 图片操作

  ```
  from PIL import Image
  cat = Image.open('相对路径')
  cat 
  ```

  ```
  cat_data = np.array(cat)
  #图片本质就是ndarray,彩色 三维:高度 宽度 像素(表示不同颜色) 红绿蓝三原色,搭配看可以变幻世界上任何颜色
  #降维 图片变成黑白的了
  cat_data([:,:,0])
  #每隔5个取一个,图片像素变小
  cat_data([::5,::5])
  # 红绿蓝 0,1,2  绿红蓝 1,0,2,图片变绿
  cat_data([:,:,[1,0,2])
  #图片展示
  Image.fromarray(cat_data)
  ```

- `matplotlib`图片展示

  ```
  import matplotlib.pyplot as plt
  %matplotlib inline
  #下面魔法指令就是为了作图方便
  #图片展示
  plt.imshow(cat_data)
  #虚化,马赛克
  plt.imshow(cat_data[::-9,::-9])
  ```

- 变形和转置

  变形 reshape函数,参数注意是一个tuple

  ```
  #要注意数据总量不变,不改变数据样本,将原来数据变为2行10列
  nd2.reshape(2,10)
  ```

  转置 axes指定转置的方式,行和列调整,互换,数据并没有打乱,图片旋转

- `numpy`级联  

  ```
    #级联的参数是列表,级联方向上形状相符
    np.concatenate([nd1,nd2])   #可以指定axis的值
    np.vstack()竖直方向,axis =0   #列数必须相等,级联放在下面
    np.hstack()水平方向 axis =1   #行数必须相等,级联放在右面
  ```

- 切分

  ```
  np.split
  np.vsplit 竖直
  np.hsplit 水平
  ```

- 副本(copy)

  ```
  所有的赋值运算不会为ndarray的任何元素创建副本,对赋值后的对象操作也会对原来的对象生效
  nd3=nd2
  id(nd2)
  id(nd3)  #nd2和nd3的地址是一样的,引用
  nd4 = nd2.copy() #深拷贝,复制了一份
  ```

- `numpy`聚合操作

  ```
  轴 计算的方向
  聚合函数,合并到一起,根据某一个方向进行合并,axis
  
  np.sum()    所有元素的和
  np.prod()     乘积
  np.mean()    平均值
  np.std()    标准差
  np.var()    方差
  np.min()    最小
  np.max()    最大
  np.argmin()    最小值索引
  np.argmax()    最大值索引
  np.median()    中位数索引
  np.percentile()     求解ndarray百分比 中位数，百分之50%  
  np.any()   有一个不为0就为true   
  np.all()    所有为0才为true
  np.power() 幂运算
  nd.ravel() 变为1维
  都有NAN类似的函数,忽裂NAN
  #ndarray对象可以直接nd.sum调用,如果没有可以使用 np.sum(nd)
  ```

  - `numpy`的统计学

    ```
    平均值,中位数,方差(自己和自己比较),标准差,协方差(两个属性求解),相关系数corrcoef
    ```

    ```
    #直方图 统计数据出现的频次
    np.histogram(nd,bins=2)
    #bins表示划分为多少份
    #查索引
    np.argwhere(nd<= 50)
    ```

- `numpy`保存加载文件

  ```
  np.save(file, arr, allow_pickle=True, fix_imports=True)
  np.save('路径',nd对象) #保存文件后缀名为npy
  np.load('路径')
  np.savetxt('路径',nd对象)
  np.loadtxt('路径')
  ```

- `numpy`的矩阵运算

  - 算术运算符

    - 加减乘除,对齐才能广播 
    - `np.add(nd1,nd2)`
    - 广播机制:规则1:为缺失的维度补1 规则2:假定缺失元素用已有值填充

  - 矩乘积 `np.dot()`

    ```
    #线性代数只是,解复杂方程
    x+y+z = 8
    2x-y+z = 8
    3x+y-z = 2
    
    
    a = np.array([[1,1,1],[2,-1,1],[3,1,-1]])
    c= np.array([8,8,2])
    #逆矩阵 
    a_inv = np.linalg.inv(a)
    b = np.dot(a_inv,c)
    b
    ```

- 排序(数据库操作，经常使用)

  - 快速排序

    ```
    排序可以用numpy模块的sort()生成新的对象,也可以用对象的sort(),直接改变原数据(不打印出来)
    np.sort()不改变输入
    ndarray.sort()本地处理，不占用空间，但改变输入
    ```

  - 部分排序

    ```
    np.partition(nd对象,k)
    #适用于我们不是对全部数据感兴趣,我们只是对最小或最大的一部分感兴趣.里面的数据还是乱的,只有想要的数据放在前面或后面(并且也没序)
     当k为正时,我们得到最小的k个数
     当k为负时,我们得到最大的k个数
    ```

- `numpy`中文网站：
  
  - https://www.numpy.org.cn/index.html

#####  4 . `kaggle` 天池大数据竞赛(阿里巴巴)

​	`kaggle` 历史很悠久,面有很多开源的项目，并且附有代码

​     所有的自然数 `x**n` +`y**n` = `Z**3`  n >= 3  正整数解 一个也没有 费马大定理

##### 5 数据分析 数据挖掘 BI  很多年的历史,条件宽松,报表

​    Excel  入门级的数据统计分析

​    SPSS    ---`超级EXcel`,软件就1个G,有数据分析,画图,算法,收费`1年10000rmb1个人`

​    `SAS`      ---`超级EXcel`, 跟SPSS类似,收费,一年一人`5000rmb`

​    `Matlab`  ---数据分析,也收费,基础版 1万1年,工具箱都买了,35万`RMB`

​    R语言   数据分析,稍微难一些,只能做数据分析,受众少

​	 python  + `numpy` +pandas + `sklearn`  +`tensorflow` +`matplotlib`  受众特别大,人员庞大

​     编程语言,写好代码,自动化运行(公司靠拢的目标)

​    

​	机器学习算法工程师,人工智能 Al

​		本质:就是解方程(比如上千万的参数)

​        方程就是规律的高度的总结

​       算法工程师,薪资很高,条件严格



   