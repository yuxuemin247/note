##### pandas

```
import pandas as pd
from panda import Series,DataFrame
```

##### Series(一维)

- values：一组数据（ndarray类型）

- index：相关的数据索引标签

- 创建

  - 方式一 ,传递列表,数组,

    ```
    #默认索引为0到N-1的整数型索引,可以通过设置index参数指定索引
    
    s = Series(data = np.random.randint(0,150,size=10),index=list('abcdefhijk'),name='python')
    s
    ```

  - 方式二,传递字典,key(行索引),value(数值)

- 索引和切片

  -  可以使用中括号取单个索引（此时返回的是元素类型），或者中括号里一个列表取多个索引（此时返回的仍然是一个Series类型）。分为显示索引和隐式索引： 显式索引,闭区间,隐式索引,开闭区间

  - 索引

    - s['d']   #获取单个,显式索引
    - s[['a','b']]  #获取多个,显式索引,多加一个[]
    - s[0]        # 获取单个,隐式索引
    - s.iloc[0]  #iloc获取,使用默认的隐式索引
    - s.loc['a']   #loc获取,使用显式索引

  - 切片

    - s['a':'d']
    - s['a':'d':2]
    - s.loc['a':'d']
    - s.iloc[0:3]

  - 属性

    - s.shape

    - s.size

    - s.index

    - s.value

      Series里的值就是ndarray

    - s.head()  #快速查看前5个

    - s.tail()     #快速查看后5个

      当索引没有对应的值时,可能出现缺失数据显示NaN(not a number)的情况

    - cond =s.isnull()   #查找空数据,空为true,返回索引

      s[cond]  

    - cond =s.notnull()   #删选为空数据

      s[cond]

       可以使用pd.isnull()，pd.notnull()，或自带isnull(),notnull()函数检测缺失数据 

  - Series的运算

    - s + 10     
    - s.add(10)
      - file_value=0,有空值时,填充0
    - s.astype(np,uint8)   转换里面数据类型
    - s.mean()
    - s.median()
    - s.value_counts()    统计数值出现了几次

  - Series之间的运算
    - s1 + s2   索引对齐计算,其他 广播机制缺少的补Nan
    - s1.add(s2,fill_value=0)    缺少的补0, 要想保留所有的index，则需要使用.add()函数 

  Series是对numpy的升级,numpy有的,Series都有

##### DataFrame(数据表格,只能是二维的:行:列)

- 创建

  - 传入字典,键为列名,

    ```
    df1 = DataFrame(data=['python':np.random.randint(0,100,size=4),'math':np.random.randint(0,100,size=4)],index=list('ABCDE')
    ```

  - 传入数组,列索引,行索引

    ```
    df2 = DataFrame(data = np.random.randint(0,100,size=(10,3)),columns = ['python','math','English'],index=list('ABCDEFGHIJ'))
    ```

- 保存成文件
  - df2.to_csv('./data.csv')
  - df2.to_excel('./data.xlsx')

- 读取文件

  - df3 = pd.read_csv('./data.csv')

    - 可能会有第一列Unnamed 

      ```
      df4 = df3.rename(columns ={'Unnamed: 0':'index'})
      df4
      df4.set_index(keys='index')
      ```

  - df5 = pd.read_excel('./data.xlsx')

- 索引
  - 行索引 
    - df.loc['行索引']
    - df.iloc['行隐式索引']
  - 列索引
    - df.列名  
    - df['列索引']
    - df[['列索引1','列索引2']]
- 元素索引
  - 先行后列 `df.loc[][]`
  - 先列后行 `df[][]`

- 切片
  - 行切片
    - 直接使用是df['行1'  :   '行3']对行切片
    - df.loc['行1' :  '行3']
    - df.iloc['隐式行索引1':'隐式行索引3']
  - 列切片
    - df.iloc[ :,列1:列3],列切片只有一种方式
- 属性
  
  - DataFrame属性:values  columns index shape
- DataFrame的运算
  - df2  - 10
  - df2.pow(2)
  - df2.divide(3).round(2)
  - df2.cov()      协方差
  - df2.corr()    相关系数
- df.info()

- df.describe()

- DateFrame之间的运算

  - 如果索引不对应,广播则默认补NaN

    df1.add(10,fill_value = 0)

    df1.add(s1,axis='index或者colum') 要对应对齐

    axis = 0         -----  index

    axis =1           -----columns


##### 创建多层索引:

```
df = DataFrame(np.random.randint(0,150,size=(20,3),columns=["python","Math","EN"],index=pd.MultiIndex.from_product([["Q","W","E","R","t"],["11","22"],["A","b"]]) 
#三层索引 5*2*2
#行列都可以,index 和columns
```

行列转换

```
df.stack(level=0) #列索引转化为行索引,0表示最外面的那一层
df.unstack(level=1) #行索引转化为列索引,1表示第二层
```

##### 聚合操作

```
df.sum() #默认axis=0是对一列聚合,可以指定axis=1对一行聚合
```

##### 拼接操作

- 级联pd.concat(),pd.append()

  - axis=0 行增加,axis=1,列增加

  - ```
    pd.concat([df1,df2], axis=0, join='outer', join_axes=None, ignore_index=False,
              keys=None, levels=None, names=None, verify_integrity=False,
              copy=True)
    #outer外连接,有不同列的属性都会保存,没有补NaN 内连接 inner只连接匹配的项
    #join_axes=[df1.columns] 以df1的列为主
    #ignore_index=True 忽略行索引, 重新建0,1,2,3 ...
    #keys=["期中","期末"]  ,加一层行索引比如df1的行索引前加期中,df2的行索引前加期末
    
    df1.append(df2) #一样,级联使用较多,所以有append
    ```

- 合并

  - 需要依据某一共同的列的值或行的值进行合并,

    - 当有多个列的值相同,可以显式的声明on="列名" ,或者left_on="",right_on =""来指定
    - 或者根据行索引合并,left_index = True,right_index =True

  - 使用pd.merge()合并时,会根据两者相同的column名称的那一列,作为key来进行合并

  - 每一列的顺序不要求一致

    ```
    一对一合并
    
    多对一合并
    
    多对多合并
    ```

  - 内合并(默认how='inner'),只保留匹配行的数据
    - 外合并(how='outer'),所有行的数据都被保留,没有值补NaN
    - 左合并(how='left'),左边的数据全保留
    - 右合并(how='right') 右边的数据全保留

  - 列冲突,当两个df中相同的名字的列时,可以使用suffixes指定冲突列名为 列名_A,列名_b

- 查询,query

  - DateFrame支持 df1.query("(year=2010 or year==2012)" and ages=='total')

- 将某一列作为索引

  - df.set_index('列名')