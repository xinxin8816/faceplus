# faceplus
A simple face recognition based on Python.Includes local and cloud dual recognition modes.
 [ReadmeCN](https://github.com/xinxin8816/faceplus/blob/master/READMECN.md "ReadmeCN")

------

## Result demo

![image](https://github.com/xinxin8816/faceplus/raw/master/screenshots/图片1.jpg)


![image](https://github.com/xinxin8816/faceplus/raw/master/screenshots/图片2.jpg)


![image](https://github.com/xinxin8816/faceplus/raw/master/screenshots/图片3.png)


![image](https://github.com/xinxin8816/faceplus/raw/master/screenshots/图片4.png)

------

## Environment

Based on Python 2.7, Theoretical support for Python 3.x.

#### Install OpenCV2.x

	sudo apt-get install -y libopencv-dev python-opencv libopencv-contrib-dev

#### Install Other tools

	sudo apt-get install -y python-picamera python-pil python-tk

#### Configuring camera
	sudo vim /etc/modules-load.d/modules.conf   //Add "bcm2835-v4l2" to the last line
	echo -e "\nbcm2835-v4l2" | sudo tee -a /etc/modules-load.d/modules.conf  //Add shortcuts

#### Self-compilation OpenCV3.x (optional)
You need to compile and install it yourself. The Raspberry Pi 3B+ is compiled for about 4 hours. note! The OpenCV3 version needs to be modified as follows:

	cv2.createEigenFaceRecognizer() —> cv2.face.EigenFaceRecognizer_create() 

	cv2.rectangle() —> img = cv2.rectangle()

#### Python require package in requirements.txt

------

## Local module description

1. The picture extracts facial features to generate an 8-bit grayscale image. The first parameter is the person photo path, and the subfolders are classified by different people.

		python generate.py ./data

2. The gray image creates a local face database, the first parameter is the gray image path generated above, and the second parameter is the path for generating the face database.

		python create_csv.py ./data/generate/ > ./data/datamap.csv

3. Now let's start face recognition, the first parameter is the gray image path generated above, and the second parameter is the path to generate the face database.

		python facerec.py ./data/generate ./data/datamap.csv

------
## Files description

##### data/lib

Some face databases that have been machine learning

##### Database.csv

Permission database

##### Demo/datamap.csv

Local recognition face database

##### Demo.py

Test infrared camera demo

##### Demo/generate.py

Image extraction facial features generate 8-bit grayscale images

##### Demo/create_csv.py

Grayscale image creation local face database

##### Demo/facerec.py

Local identification module

##### Face++_1.py

Cloud identification module

##### Face++_2.py

Same as above, and 1 is not much different in nature.

##### Gpio.py

Hardware lock driver module

##### Chat.py

The networking module has a database function that contains modify permissions. Running chat.py directly is in server mode, and another machine runs through chat.py+IP to link the server.
