# -- coding: utf-8 -- 
"""
Created on 2018-4-1 12:00:48
@author: xinxin8816
"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
while True: 
	GPIO.output(12, GPIO.HIGH) 
	time.sleep(1)
	GPIO.output(12, GPIO.LOW) 
	time.sleep(1)
