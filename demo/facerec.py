#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
demo 2.0
Created on 2019-1-20 16:00:06
@author: xinxin8816
"""

import multiprocessing as mp
import cv2
import os
import sys
import time
import numpy as np

resX = 640
resY = 480

face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml')

#三种识别算法，△留意Python2.7语法不同 2019-1-21
#model = cv2.face.createEigenFaceRecognizer()
model = cv2.face.FisherFaceRecognizer_create()
#model = cv2.createLBPHFaceRecognizer()
t_start = time.time()
fps = 0

def normalize(X, low, high, dtype=None):
    """将X中的给定数组规范化为低和高之间的值"""
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    X = X - float(minX)
    X = X / float((maxX - minX))
    # scale to [low...high].
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)

def load_images(path, sz=None):
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    filepath = os.path.join(subject_path, filename)
                    if os.path.isdir(filepath):
                        continue
                    img = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    if (img is None):
                        print ("image " + filepath + " is none")
                    else:
                        print (filepath)
                    if (sz is not None):
                        img = cv2.resize(img, (200, 200))
                    X.append(np.asarray(img, dtype=np.uint8))
                    y.append(c)
                except:
                    print ("Unexpected error:", sys.exc_info()[0])
                    raise
            print (c)
            c = c+1
    print (y)
    return [X,y]

def get_faces( img ):
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces, img, gray

def draw_frame( faces, img, gray ):
    global xdeg
    global ydeg
    global fps
    global time_t
    for ( x, y, w, h ) in faces:
        img=cv2.rectangle( img, ( x, y ),( x + w, y + h ), ( 200, 255, 0 ), 2 )
        roi = gray[x:x+w, y:y+h]
        try:
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
            params = model.predict(roi)
            sign=("%s %.2f" % (names[params[0]], params[1]))
            cv2.putText(img, sign, (x, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )
            if (params[0] == 0):
                cv2.imwrite('face_rec.jpg', img)
        except:
            continue

    fps = fps + 1
    sfps = fps / (time.time() - t_start)
    cv2.putText(img, "FPS : " + str( int( sfps ) ), ( 10, 15 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )
    cv2.imshow( "recognize-face", img )

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,resX)  
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,resY)
    pool = mp.Pool( processes=4 )
    #人名与datamap.csv数据库里面的对应
    names = ['yun', 'song', 'yang']
    if len(sys.argv) < 2:
        print ("USAGE: facerec.py <人脸数据存放路径> [<数据对应表>]")
        sys.exit()
    [X,y] = load_images(sys.argv[1])
    y = np.asarray(y, dtype=np.int32)
    if len(sys.argv) == 3:
        out_dir = sys.argv[2]
    model.train(np.asarray(X), np.asarray(y))
    read, img = camera.read()
    pr1 = pool.apply_async( get_faces, [ img ] )   
    read, img = camera.read()
    pr2 = pool.apply_async( get_faces, [ img ] )  
    read, img = camera.read() 
    pr3 = pool.apply_async( get_faces, [ img ] )   
    read, img = camera.read()
    pr4 = pool.apply_async( get_faces, [ img ] )
    fcount = 1
    while (True):
        read, img = camera.read()
        if   fcount == 1:
            pr1 = pool.apply_async( get_faces, [ img ] )
            faces, img, gray=pr2.get()
            draw_frame( faces, img, gray )
        elif fcount == 2:
            pr2 = pool.apply_async( get_faces, [ img ] )
            faces, img, gray=pr3.get()
            draw_frame( faces, img, gray )
        elif fcount == 3:
            pr3 = pool.apply_async( get_faces, [ img ] )
            faces, img, gray=pr4.get()
            draw_frame( faces, img, gray )
        elif fcount == 4:
            pr4 = pool.apply_async( get_faces, [ img ] )
            faces, img, gray=pr1.get()
            draw_frame( faces, img, gray )
            fcount = 0
        fcount += 1
        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()