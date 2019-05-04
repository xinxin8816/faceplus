# coding:utf-8
"""
Created on 2018-3-23 16:00:06
@author: xinxin8816
"""
import requests
from json import JSONDecoder
import cv2

key = "pM5Sh3M8qcF9503Q0fsBOgvH26vNq8Pv" #来自旷视科技的API，此key有调用频率限制
secret = "UPziWDeLgHDyqhIEnuYqGTUzZOniW8I4"
filepath1 = "\demo\data\yun\\1.jpg"
filepath2 = "\demo\data\yun\\2.jpg"
filepath3 = "\demo\data\yun\\3.jpg"


# files = {"image_file": open(filepath1, "rb")}
# cap = cv2.VideoCapture(0)

def detect_face(filepath):  # 上传图片至face++服务器
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}
    data = {"api_key": key, "api_secret": secret, "return_gesture": "1"}
    # starttime = datetime.datetime.now()
    response = requests.post(http_url, data=data, files=files)
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def detect_face_64(image_base64):  # 以base64二级制编码方式上传
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    params = {
        'api_key': key,
        'api_secret': secret,
        'image_base64': image_base64
    }
    response = requests.post(http_url, data=params)
    req_dict = response.json()
    print(req_dict)
    return req_dict


def set_face(outer_id):  # 创建一个人脸的集合 FaceSet，用于存储人脸标识 face_token
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    params = {
        'api_key': key,
        'api_secret': secret,
        'outer_id': outer_id
    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def compare(faceId1, faceId2):  # 对比两个人脸标识 face_token 来判断是否是同一个人。
    params = {}
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    params['face_token1'] = faceId1
    params['face_token2'] = faceId2
    params['api_key'] = key
    params['api_secret'] = secret
    r = requests.post(url, params)
    return r.json()


def addface(faceset, facetokens):  # 为一个已经创建的 FaceSet 添加人脸标识 face_token
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset,
        'face_tokens': facetokens
    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def get_face_set():  # 获取所有 FaceSet id
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    params = {
        'api_key': key,
        'api_secret': secret,

    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def delete_faceset(faceset_token, check_empty):  # 删除指定 FaceSet
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
        'check_empty': check_empty
    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def faceset_update(faceset_token, display_name, user_data):  # 更新一个人脸标识 faceset_token 属性（显示名、自定义内容）
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/update'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
        'display_name': display_name,
        'user_data': user_data
    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def faceset_getdetail(faceset_token):  # 获取一个 FaceSet 的所有信息
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
    }
    r = requests.post(url, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_compare(image_file1, face_token2):  # 即时识别图像人脸，并对比人脸标识 face_token 来判断是否是同一个人，1对1。
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    files = {"image_file1": open(image_file1, "rb")}
    params = {
        'api_key': key,
        'api_secret': secret,
        'face_token2': face_token2
    }
    r = requests.post(url, files=files, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_search(image_file1, faceset_token):  # 即时识别图像人脸，并搜索 FaceSet 来是否拥有同一个人，1对N。
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': faceset_token,
    }
    r = requests.post(url, files=files, data=params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def face_SetUserID(face_token, user_id):  # 增加一个人脸标识 faceset_token 属性（显示名、自定义内容）
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    params = {
        'api_key': key,
        'api_secret': secret,
        'face_token': face_token,
        'user_id': user_id
    }
    r = requests.post(url, data=params)
    req_dict = r.json()
    print(req_dict)
    return req_dict


if __name__ == "__main__":
    get_face_set()
    image1 = detect_face(filepath3)
    faceId1 = image1['faces'][0]['face_token']
    addface('98e8cde36b62cd12370a6126cfa4b408', faceId1)
    img = cv2.imread(filepath2)
    face_information = face_search(filepath2, '98e8cde36b62cd12370a6126cfa4b408')  # 该帧与faceset中人脸进行匹配
    if face_information['faces']:  # [faces]数组不能为空，能在图像中找到脸
        confidence = face_information['results'][0]['confidence']
        thresholds = face_information['thresholds']['1e-5']
        if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
            user_id = face_information['results'][0]['user_id']  # 获得唯一人脸id
            w = face_information['faces'][0]['face_rectangle']['width']
            h = face_information['faces'][0]['face_rectangle']['top']
            x = face_information['faces'][0]['face_rectangle']['left']
            y = face_information['faces'][0]['face_rectangle']['height']
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框
            font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
            cv2.putText(img, user_id, (x, y - 5), font, 1, (0, 0, 255), 1)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
            cv2.imwrite('D:\\PYTHON0\\my_face_handsome\\video_face\\1.jpg', img)
