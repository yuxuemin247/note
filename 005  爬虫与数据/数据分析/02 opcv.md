opencv  c++写的代码

 python 调用cv2模块中的方法

- 图片操作

  ```
  import numpy as np 
  import cv2 
  #读取图片,不能包含中文,
  jin1 = cv2.imread('./jin,jpg')
  jin1
  jin1.shape
  #第一个参数是打开窗口名字,第二个是数据
  cv2.imshow('jin',jin1)
  #等待键盘输入,单位毫秒,如果是0,无限等待
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  #BGR 蓝绿红 cv2读取图片,颜色通道是BGR
  #PIL 读取图片,颜色通道是RGB
  jin2 =cv2.cvtColor(jin1,code = cv2.COLOR_BGR2GRAY)
  cv2.imshow('gray',jin2)
  while True:
      if ord('q')==cv2.waitKey(1000)   #键盘输入q时关闭
  cv2.destroyAllwindows()
  #写图片
  cv2.imwrite('./jin1_gray.jpg',jin2)
  ```

- 视频操作

  ```
  import numpy as np 
  import cv2
  
  #读取视频
  cap = cv2.VideoCapture('./video2.mp4')
  cap  #<VideoCapture 00000189481A69D0>
  #获取属性, cv2.CAP_PROP_FPS 是帧数
  cap.get(propId = cv2.CAP_PROP_FPS)
  
  #flag 是 True 或Flase 
  #frame 是每一张图片
  flag,frame = cap.read()
  
  #级联分类器,给人脸特征数据,返回可以识别人脸的对象
  dector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
  
  #保存视频写操作
  video_writer = cv2.VideoWriter('./po.mp4',cv2.VideoWriter_fourcc('M','P','4','v'),24,(w,h))
  
  While cap.isOpened():
  	flag,frame =cap.read()
  	gray = cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
  	
  	#识别
  	face_zone = dector.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
  	
  	#画圆,thickness是线的宽度
  	for x,y,w,h in face_zone:
  		cv2.circle(frame,center=(x+w//2,y+h//2),radius = w//2,color =[0,0,255],thickness=2)
      #最后一帧了,结束死循环
      if flag == False:
      	break
      #将每一帧写入
      video_writer.write(frame)
      #展示每一帧
     	cv2.imshow('liang',frmae)
     	
     	if ord('q') == cv2.waitKey(1):
          break
  
  #关闭流,释放资源,写入文件       
  cv2.destroyAllWindows()
  cap.release()
  video_writer.release()
      
  ```


- 音频操作

  scipy

  ```
  from scipy.io import wavfile
  #读取
  music =wavfile.read('文件路径')
  #音乐数据
  music = music[1]
  #写音乐数据
  #44100是1秒的采样频率,
  #music[::120*44100]是对音乐数据进行截取2分钟
  wavfile.write('文件路径',44100,music[::120*44100])
  ```

  