# -- coding: utf-8 -- 
"""
Created on 2018-4-1 12:00:48
@author: xinxin8816
"""
import sys
import os.path
import csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("usage: gpio.py <云端返回 outer_id>")
        sys.exit(0)

outer_id = sys.argv[1]
database_PATH = 'database.csv'
with open(database_PATH, "r", encoding = "ANSI") as database:
	reader = csv.DictReader(database)
	name = [row['outer_id'] for row in reader]
print(name)
site = name.index(outer_id)
with open(database_PATH, "r", encoding = "ANSI") as database:
	reader = csv.DictReader(database)
	lockright = [row['lockright'] for row in reader]
print(lockright[site])

if lockright[site] == 1:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	while True:
		GPIO.output(12, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(12, GPIO.LOW)
		time.sleep(1)