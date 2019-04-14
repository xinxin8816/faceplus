#coding:utf-8
"""
Created on 2019-4-13 08:36:37
@author: xinxin8816
"""
import os
import re

nfcdata = os.popen('nfc-list')
type(nfcdata)
data = nfcdata.readlines()
print(nfcdata.readlines()[3])