##### 图像灰度处理的三种方法

-  灰度化处理就是将一幅色彩图像转化为灰度图像的过程。彩色图像分为R，G，B三个分量，分别显示出红绿蓝等各种颜色，灰度化就是使彩色的R，G，B分量相等的过程。灰度值大的像素点比较亮（像素值最大为255，为白色），反之比较暗（像素最下为0，为黑色）。 

- ```
  import matplotlib.pyplot as plt
  %matplotlib inline
  import numpy as np
  
  img = plt.imread('路径') #读取图片
  plt.imshow(img) #展示图片
  img.shape  #三维 (2448,3264,3)
  ```

  - ```
    #最大值法,这种方法转换的灰度图亮度很高
    gray = img.max(axis = -1)
    plt.imshow(gray,cmap = plt.cm.gray)    #灰度化处理
    gray.shape   #(2448,3264)
    ```

  - ```
    #平均值法,这种方法产生的灰度图像比较柔和
    gray = img.mean(axis = 2)
    plt.imshow(gray,cmap = plt.cm.gray)
    ```

  - ```
    # 加权平均值法 红绿蓝
    # 0.299,0.587,0.114
    w = np.array([0.299,0.587,0.114])
    gray = img.dot(w)
    gray.shape    #(2448,3264)
    ```

  ##### `matplotlib`基础知识

  - 图表包括的基本元素

    - X轴和Y轴
    - 刻度,刻度表示坐标轴的分隔,包括最小刻度和最大刻度
    - X轴和Y轴刻度标签(`xlabel`,`ylabel`)
    - 绘图区域和实际绘图区域

  - 画单一曲线

    - ```
      x = np.linspace(0,2*np.pi)   #默认是等分为50份
      y = np.sin(x)
      plt.plot(x,y)
      ```

  - 画多个曲线

    - ```
      #可以使用多个plot函数,在一个图中绘制多个曲线
      plt.plot(x,y)
      plt.plot(x,y2)  #最好使用同一个X
      ```

    - ```
      也可以在一个plot函数中传入多对X,Y的值,在一个图中绘制多个曲线
      plt.plot(x,y,x,y2)
      ```

  - 加网格线

    - ```
      plt.plot(x,y)
      plt.grid()
      ```

  - 设置坐标轴界限

    - ```
      x = np.arange(1,5)
      plt.plot(x,x*1.5,x,x*3.0)
      plt.xlim(0,5)
      plt.ylim(0,10)
      plt.show()
      ```

    - ```
      x = np.arange(1, 5)
      plt.plot(x, x*1.5, x, x*3.0)
      # plt.axis() # shows the current axis limits values；如果axis方法没有任何参数，则返回当前坐标轴的上下限
      # (1.0, 4.0, 0.0, 12.0)
      # plt.axis([0, 15, -5, 13]) # set new axes limits；axis方法中有参数，设置坐标轴的上下限；参数顺序为[xmin, xmax, ymin, ymax]
      plt.axis(xmax=5,ymax=23) # 可使用xmax,ymax参数
      plt.show()
      #或者使用类型 equal x轴y轴相等  off 关闭坐标轴    #'tight'
      plt.axis('equal')
      ```

  - 全局的字体设置

    - ``` 
      from matplotlib import rcParams
      rcParams['font.sans-serif']  = 'KaiTi'  #设置字体为楷体
      rcParams['axes.unicode_minus'] = False   #设置显示+ -号
      plt.xlabel('X',fontsize = 20,color = 'red')  #设置X轴刻度标签,字体大小颜色
      plt.ylabel('X**2 + Y**2 = 1',fontsize = 20,rotation = -60) #设置Y轴刻度标签,旋转等
      plt.title('Cicle圆',fontize=30) #设置标题
      ```

  - 图例

    - ```
      x = np.linspace(0,2*np.pi)
      plt.plot(x,np.sin(x),x,np.cos(x))
      plt.legend(['正弦波','余弦波'],loc='right',ncol=2)  
      #默认会找空白地方,可以loc='right'等等指定,loc参数可以元组(x,y)等 ncol控制图例中有几列
      ```

  - 线条的样式

    - ```
      plt.plot(x,np.sin(x),color='red',marker='*',linestyle = '--',alpha=0.2)
      #设置线条样式为 '--',点为'*',颜色为red,alpha设置透明度
      #dashes=[2, 5, 5, 2] 设置破折号序列各自的宽度
      ```

  - 保存文件

    - ```
      #通过plt.subplot()方法传入facecolor参数,来设置坐标轴的背景色
      ax = plt.subplot(1,1,1,facecolor = 'green')
      ax.plot(x,np.sin(x),color = 'red',marker = '*',linestyle  = '--')
      plt.savefig('./fig3.pdf',dpi = 500,facecolor = 'green')
      #filename,图像格式由文件扩展名推断得出,例如.pdf推断出PDF .png推断出png
      #dpi 图像分辨率(每英寸点数),默认为100
      #facecolor 图像的背景色,默认为白色'w'
      ```

  - X Y轴坐标刻度

    -  `xticks()`和`yticks()`方法 

      ```
      x = [5, 3, 7, 2, 4, 1]
      plt.plot(x);
      plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f']); # 传入位置和标签参数，以修改坐标轴刻度
      plt.yticks(range(1, 8, 2));
      
      plt.show()
      ```

  ##### 四种图

  - 直方图



