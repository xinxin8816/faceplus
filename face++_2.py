# coding:utf-8
"""
face++2.0
Created on 2018-7-23 16:00:06
@author: xinxin8816
"""

import requests
from json import JSONDecoder
import time
import cv2
import os

key = "wUkL-ctNFvh_f6A-Qp9b2bTKaPyn1I3I"
secret = "1JEHsrIholzaA2v91LkW4JL9F1G-LzB9"
filepath1 = "D:\Study\树莓派\\test\data\yun\\1.jpg"
filepath2 = "D:\Study\树莓派\\test\data\yun\\2.jpg"
filepath3 = "D:\Study\树莓派\\test\data\yun\\3.jpg"
data = {"api_key": key, "api_secret": secret}


# files = {"image_file": open(filepath1, "rb")}
# cap = cv2.VideoCapture(0)

def detect_face(filepath):  # 传入图片文件
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}

    # starttime = datetime.datetime.now()
    response = requests.post(http_url, data=data, files=files)
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def detect_face_64(filepath):  # 传入base64编码
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}

    # starttime = datetime.datetime.now()
    response = requests.post(http_url, data=data, files=files)
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def set_face():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    params = {
        'api_key': key,
        'api_secret': secret,

    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def compare(faceId1, faceId2):
    params = {}
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    params['face_token1'] = faceId1
    params['face_token2'] = faceId2
    params['api_key'] = key
    params['api_secret'] = secret
    r = requests.post(url, params)
    return r.json()


def addface(faceset, facetokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset,
        'face_tokens': facetokens
    }
    r = requests.post(url, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def get_face_set():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    params = {
        'api_key': key,
        'api_secret': secret,
    }
    r = requests.post(url, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def delete_faceset(faceset_token, check_empty):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
        'check_empty': check_empty
    }
    r = requests.post(url, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def faceset_update(faceset_token, display_name, user_data):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/update'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
        'display_name': display_name,
        'user_data': user_data
    }
    r = requests.post(url, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def faceset_getdetail(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
    }
    r = requests.post(url, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_compare(image_file1, face_token2):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    files = {"image_file1": open(image_file1, "rb")}
    params = {
        'api_key': key,
        'api_secret': secret,
        'face_token2': face_token2
    }
    r = requests.post(url, files=files, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_search(image_file1, faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token
    }
    r = requests.post(url, files=files, params=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_SetUserID(face_token, user_id):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    params = {
        'api_key': key,
        'api_secret': secret,
        'face_token': face_token,
        'user_id': user_id
    }
    r = requests.post(url, params=params)
    req_dict = r.json()
    print(req_dict)
    return req_dict


if __name__ == "__main__":
    capInput = cv2.VideoCapture(1)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_right = 0  # 识别的人脸有没有在faceset中发现，有置1
    recognize_inf = 0  # 识别的人脸在faceset中发现，置1,持续显示id信息一定时间标志位
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
    i = 0
    while (1):
        ret, img = capInput.read()  # 摄像头获取该帧图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像转灰度
        faces = faceCascade.detectMultiScale(gray, 1.1, 7)  # 送入Haar特征分类器
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if len(faces) == 0:  # 视频中无脸出现
            cv2.imshow('ImageCaptured', img)
        else:
            if i >= 20 and face_right == 0:
                i = 0
                cv2.imwrite('D:\\PYTHON0\\my_face_handsome\\video_face\\1.jpg', img)  # 写入该帧图像文件
                face_information = face_search('D:\\PYTHON0\\my_face_handsome\\video_face\\1.jpg',
                                               'e55232f11a305f9165caf50ef16ae053')  # 该帧与faceset中人脸进行匹配
                if face_information['faces']:  # [faces]数组不能为空，能在图像中找到脸
                    confidence = face_information['results'][0]['confidence']
                    thresholds = face_information['thresholds']['1e-5']
                    os.remove('D:\\PYTHON0\\my_face_handsome\\video_face\\1.jpg')  # 删除该帧图像文件，为下一次处理准备
                    if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
                        user_id = face_information['results'][0]['user_id']  # 获得唯一人脸id
                        recognize_inf = 1
                        face_right = 1
                    else:
                        face_right = 0
                else:
                    face_right = 0  # 未能在图像中找到脸
            else:
                i = i + 1

            for x, y, w, h in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框

            if face_right == 1:
                cv2.putText(img, user_id, (x, y - 5), font, 1, (0, 0, 255), 1)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
                cv2.putText(img, 'Welcome:', (x - 20, y - 50), font, 2, (0, 0, 0), 2)
                cv2.imshow('ImageCaptured', img)
                if recognize_inf:
                    b = (time.localtime()[5])
                    a = (time.localtime()[5])
                    recognize_inf = 0
                if (abs(a - b) <= 3):  # 现在该提示信息3s
                    a = (time.localtime()[5])
                else:
                    face_right = 0
            else:
                cv2.putText(img, "stranger", (x, y - 5), font, 1, (0, 255, 0), 1)
                cv2.imshow('ImageCaptured', img)

capInput.release()
cv2.destroyAllWindows()
