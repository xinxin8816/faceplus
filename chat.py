# coding:utf-8
"""
Created on 2018-4-10 9:58:40
@author: xinxin8816
"""
import network
import sys
import csv
import pandas as pd

database_PATH = 'database.csv'


def adddata(outer_id, displayname, lockright):  # 数据库增加新行
    row = [outer_id, displayname, lockright]
    with open(database_PATH, "a", encoding="ANSI") as database:
        csv_writer = csv.writer(database, dialect="excel")
        csv_writer.writerow(row)


def deldata(outer_id):  # 数据库删除行
    odata = pd.read_csv(database_PATH, encoding='ANSI')
    with open(database_PATH, "r", encoding="ANSI") as database:
        reader = csv.DictReader(database)
        name = [row['outer_id'] for row in reader]
    site = name.index(outer_id)
    odata.drop(odata.index[site], inplace=True)
    odata.to_csv(database_PATH, mode="w", header=True, index=False)


def updatedata(outer_id, lockright):  # 数据库修改lock权限
    with open(database_PATH, "r", encoding="ANSI") as database:
        reader = csv.DictReader(database)
        name = [row['outer_id'] for row in reader]
        site = name.index(outer_id)
        displayname = [row['displayname'] for row in reader]
    print(displayname[site])
    deldata(outer_id)
    adddata(outer_id, displayname[site], lockright)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Server Mode")
    else:
        print("Client Mode")


def heard(phrase):
    print("Receive:" + phrase)
    print(phrase.split())
    if phrase.split()[0] == 'doing':
        sys.exit(0)


if (len(sys.argv) >= 2):
    network.call(sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)

while network.isConnected():
    phrase = raw_input()  # python2
    # phrase = input()
    print("Send:" + phrase)
    network.say(phrase)
