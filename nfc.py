# coding:utf-8
"""
Created on 2019-4-13 08:36:37
@author: xinxin8816
"""
from pynfc import Nfc, Desfire, Timeout

n = Nfc("pn532_i2c:/dev/i2c-1")
Card_default_key = b'\x00' * 8
Card_blank_token = b'\xFF' * 1024 * 4

for target in n.poll():
    try:
        print(target.auth(Card_default_key if type(target) == Desfire else Card_blank_token)) #若卡有密匙则用默认密匙解锁
        print(target.uid)
    except TimeoutException:
        pass