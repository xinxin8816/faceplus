# faceplus
一个基于Python的人脸识别项目。包括本地和云端两种识别方式。（已弃坑）

------

## 环境准备

开发基于Python2.7，理论支持Python3.x。

#### 安装OpenCV2开发环境

	sudo apt-get install -y libopencv-dev python-opencv libopencv-contrib-dev

#### 安装一些其它工具

	sudo apt-get install -y python-picamera python-pil python-tk

#### 摄像头配置
	sudo vim /etc/modules-load.d/modules.conf   //文件尾部添加一行 bcm2835-v4l2
	echo -e "\nbcm2835-v4l2" | sudo tee -a /etc/modules-load.d/modules.conf  //增加快捷方式

#### 自编译OpenCV3.x（可选）
需自行编译安装，树莓派3B+ 编译大约4小时。注意！OpenCV3版本需要修改如下内容：

	cv2.createEigenFaceRecognizer() —> cv2.face.EigenFaceRecognizer_create() 

	cv2.rectangle() —> img = cv2.rectangle()

#### Python依赖包 requirements.txt

------

## 本地模块说明

1.图片提取人脸特征生成8-bit的灰度图像。第一个参数为人物照片路径，子文件夹以不同人来分类

	python generate.py ./data

2.灰度图像创建本地人脸数据库，第一个参数为上述生成的灰度图像路径，第二个参数为生成人脸数据库的路径

	python create_csv.py ./data/generate/ > ./data/datamap.csv

3.进行人脸识别，第一个参数为上述生成的灰度图像路径，第二个参数为生成人脸数据库的路径

	python facerec.py ./data/generate ./data/datamap.csv

------
## 文件说明

data/lib 已经机器训练好的一些人脸数据库

database.csv 权限数据库

demo/datamap.csv 本地识别用人脸数据库

demo.py 测试红外摄像头demo

demo/generate.py 图片提取人脸特征生成8-bit的灰度图像

demo/create_csv.py 灰度图像创建本地人脸数据库

demo/facerec.py 本地识别模块

face++_1.py 云端识别模块

face++_2.py 同上，和1本质上没太大区别

gpio.py 硬件锁驱动模块

chat.py 联网模块，里面有包含修改权限数据库函数。直接运行 chat.py 是服务器模式，另外一台机子通过 chat.py+IP 运行来链接服务器。
	
nfc.py NFC模块部分，用来获取卡UID
