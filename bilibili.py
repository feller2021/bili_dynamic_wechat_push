#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : B站
# Desc      : B站主模块

import requests, json, sys, re
import time
from datetime import datetime, timedelta
import fanfaf
import ifzf
import os



class bzMonitor():
    def __init__(self, ):
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Content-Type': 'application/x-www-form-urlencoded',

            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        self.uid = ['672328094','483311105','294081438','1711589','25910292','11442277','4549624','21876627']  # 这里添加关注人的uid

    # 获取各用户的json连接
    def getbzurl(self):
        try:
            self.bzurl = []
            for i in self.uid:
                url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=%s&offset_dynamic_id=0&need_top=1&platform=web' % (
                    i)
                self.bzurl.append(url)
        except Exception as e:
            self.echoMsg('Error', e)

            sys.exit()

    # 获取各用户当前视频数目
    def getBZQueue(self):
        try:
            for i in self.bzurl:
                res = requests.get(i, headers=self.reqHeaders)

                result = json.loads(str(res.content, 'utf-8'))

                data = result['data']

                with open('bilibili.txt', 'a') as f:
                    for idd in data['cards']:
                        jk = idd['desc']['dynamic_id']
                        f.write(str(jk) + '\n')
                self.echoMsg('Info', '视频数目获取成功')
        except Exception as e:
            self.echoMsg('Error', e)
            sys.exit()

    # 监控函数
    def startbzmonitor(self, ):

        returnDict = {}  # 获取视频相关内容
        try:
            bilibili = []
            with open('bilibili.txt', 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    bilibili.append(line)
            for i in self.bzurl:
                res = requests.get(i, headers=self.reqHeaders)
                result = json.loads(str(res.content, 'utf-8'))

                data = result['data']

                for dynamic_idd in data['cards']:
                    dk = dynamic_idd['desc']
                    cardss = dynamic_idd['card']

                    jk = dynamic_idd['desc']['dynamic_id']

                    if str(jk) not in bilibili:
                        with open('bilibili.txt', 'a') as f:
                            f.write(str(jk) + '\n')
                            self.echoMsg('Info', 'B站视频更新啦!!!')
                            fanfaf.jiexi(dk,cardss,jk)
        except Exception as e:
            self.echoMsg('Error', e)
            sys.exit()


# 格式化输出
    def echoMsg(self, level, msg):
        if level == 'Info':
            print('[Info] %s' % msg)

        elif level == 'Error':
            print('[Error] %s' % msg)




if __name__ == '__main__':
    b = bzMonitor()
    b.getbzurl()
    with open('bilibili.txt', 'r') as f2:
        text = f2.read()
        if text == '':
            b.getBZQueue()
    newBZ = b.startbzmonitor()
