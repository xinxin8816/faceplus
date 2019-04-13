#coding:utf-8
"""
Created on 2019-4-13 08:36:37
@author: xinxin8816
"""
import os
import numpy as np
import re

nfcdata = os.popen('nfc-list')
type(nfcdata)
line = nfcdata.readlines()
data_list = []
while line:
    num = list(map(float,line.split()))
    data_list.append(num)
    line = nfcdata.readline()
data_array = np.array(data_list)
print(data_array[3])