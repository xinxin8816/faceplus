# faceplus
A simple face recognition based on Python

------
依赖包 requirements.txt  

database.csv 权限数据库
datamap.csv 本地识别用人脸数据库

demo.py 测试红外摄像头demo
generate.py 图片提取人脸特征生成8-bit的灰度图像
create_csv.py 灰度图像创建本地人脸数据库
facerec.py 本地识别模块
face++_1.py 云端识别模块
face++_2.py 同上，和1本质上没太大区别
gpio.py 硬件锁驱动模块
chat.py 联网模块，里面有包含修改权限数据库函数
		直接运行chat.py是服务器模式，另外一台机子通过 chat.py+IP 运行来链接服务器。
nfc.py NFC模块部分，用来获取卡UID