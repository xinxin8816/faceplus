#coding:utf-8
"""
Created on 2018-4-10 9:58:40
@author: xinxin8816
"""
import network
import sys

def heard(phrase):
	print("them:" + phrase)

if (len(sys.argv) >= 2):
	network.call(sys.argv[1], whenHearCall=heard)
else:
	network.wait(whenHearCall=heard)

while network.isConnected():
	phrase = raw_input() #python2
	#phrase = input()
	print("me:" + phrase)
	network.say(phrase)