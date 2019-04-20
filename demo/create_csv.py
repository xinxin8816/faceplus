# coding:utf-8
"""
Created on 2018-3-23 16:00:06
@author: xinxin8816
"""
import sys
import os.path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: create_csv.py <生成的人脸数据路径>")
        sys.exit(0)

    BASE_PATH = sys.argv[1]
    SEPARATOR = ";"
    label = 0
    for dirpath, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirpath, subdirname)
            for filename in os.listdir(subject_path):
                image_filename = subject_path + "/" + filename
                abs_path = "%s/%s" % (subject_path, filename)
                print("%s%s%d" % (abs_path, SEPARATOR, label))
            label = label + 1
