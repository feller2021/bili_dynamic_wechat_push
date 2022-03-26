import sys
import time
import ifzf
import bilitype
import requests
import re
import os
import json
from datetime import datetime, timedelta

# imgpost = 'https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'

# headers = {'Content-Type': 'application/json'}


def jiexi(dk, cardss, jk):
    # data=data
    # print(data)
    # dk = i['desc']
    # cardss = i['card']
    #
    # jk = i['desc']['dynamic_id']
    dk = dk
    cardss = cardss
    jk = jk

    uname = dk['user_profile']['info']['uname']
    dynamic_type = dk['type']
    timestamp = dk['timestamp']

    timestamp=int(timestamp)
    dynamic_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    dynamic_time2=datetime.strptime(dynamic_time1, "%Y-%m-%d %H:%M:%S")+ timedelta(hours=8)
    dynamic_time=str(dynamic_time2)
    print(uname)
    print(dynamic_type)
    print(dynamic_time)
    dynamic_id = dk['dynamic_id']
    lj = 'https://m.bilibili.com/dynamic/' + str(dynamic_id)
    now = datetime.now() + timedelta(hours=8)

    dc = now.strftime("%H:%M:%S")
    tzshj = dc
    print("github通知时间是：" + tzshj)
    d1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print("github时间d1是：" + d1)
    d3 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    print(d3)

    d2 = datetime.strptime(dynamic_time, "%Y-%m-%d %H:%M:%S")

    timedelay = d3 - d2

    timedelay = str(timedelay)
    print(timedelay)

    # print(type(content))
    # print(content)
    if dynamic_type == 1:
        # 转发动态
        content = json.loads(cardss)
        content = content['item']
        zfnr = content['content']
        zfnr = str(zfnr)
        orig_dy_id = content['orig_dy_id']

        lj = 'https://m.bilibili.com/dynamic/' + str(orig_dy_id)

        diaoifzf = ifzf.ifzf(orig_dy_id)
        diaoifzf = str(diaoifzf)
        typ = bilitype.bilitype(dynamic_type)
        # fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + zfnr + '\n' + '------------------------' + '\n' + '------------------------' + '\n' + diaoifzf + '\n' + '------------------------'

        fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' '
        print(fasongneir)
        postdata = json.dumps({"msg": fasongneir})
        time.sleep(2)
        fasongneir2 = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + zfnr + '\n' + '------------------------' + '\n' + '------------------------' + '\n' + diaoifzf + '\n' + '------------------------'

        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        FormData = {
            "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
            "content": fasongneir2,
            "summary": fasongneir,
            "contentType": 2,

            "topicIds": [

            ],
            "uids": [
                "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
            ],
            "url": ""
        }
        res = requests.post(url=url, json=FormData, headers=HEADERS)
        print(res.text)











    elif dynamic_type == 2:
        # 图文动态

        content = json.loads(cardss)
        content = content['item']
        neirong = content['description']
        pic_url = content['pictures']
        pictures_count = content['pictures_count']

        print(pictures_count)
        print(dynamic_id)
        typ = bilitype.bilitype(dynamic_type)

        # fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '图片数量：' + str(
        #     pictures_count) + ' ' + '张' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
        #     neirong) + '\n'

        fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '图片数量：' + str(
            pictures_count) + ' ' + '张' + '\n'

        print(fasongneir)
        fasongneir2 = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '图片数量：' + str(
            pictures_count) + ' ' + '张' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
            neirong) + '\n'
        # postdata = json.dumps({"msg": fasongneir})
        # time.sleep(2)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)

        # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
        tupian = ''
        for pic in pic_url:
            zlpic_url = pic['img_src']

            print(pic['img_src'])
            zuhe = "<img src=\"" + zlpic_url + "\" >"
            tupian += zuhe
            # postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
            # repp = requests.post(url=imgpost, data=postdata, headers=headers)
            # print(repp)

        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = fasongneir2 + huanghang + tupianxianshi + tupian
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        FormData = {
            "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
            "content": content,
            "summary": fasongneir,
            "contentType": 2,

            "topicIds": [

            ],
            "uids": [
                "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
            ],
            "url": ""
        }
        res = requests.post(url=url, json=FormData, headers=HEADERS)
        print(res.text)


    elif dynamic_type == 4:
        # 文字动态
        content = json.loads(cardss)
        content = content['item']

        wenzi = content['content']
        typ = bilitype.bilitype(dynamic_type)

        print(wenzi)
        # fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
        #     wenzi) + '\n'
        fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n'

        fasongneir2 = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
            wenzi) + '\n'
        # print(fasongneir)
        # postdata = json.dumps({"msg": fasongneir})
        # time.sleep(2)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        FormData = {
            "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
            "content": fasongneir2,
            "summary": fasongneir,
            "contentType": 2,

            "topicIds": [

            ],
            "uids": [
                "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
            ],
            "url": ""
        }
        res = requests.post(url=url, json=FormData, headers=HEADERS)
        print(res.text)



    elif dynamic_type == 8:
        # 投稿动态
        content = json.loads(cardss)
        tgtlttle = content['title']
        tgpic_url = content['pic']
        tgpic_url = str(tgpic_url)
        av = dk['rid_str']
        av = 'av' + str(av)
        lj = 'https://www.bilibili.com/video/' + av
        print(tgtlttle)
        print(tgpic_url)
        typ = bilitype.bilitype(dynamic_type)
        # fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
        #     tgtlttle) + '\n'
        fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n'

        fasongneir2 = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
            tgtlttle) + '\n'
        print(fasongneir)
        # postdata = json.dumps({"msg": fasongneir})
        # time.sleep(2)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        # time.sleep(2)
        # zlpic_url = pic['img_src']

        # print(pic['img_src'])
        # postdata36 = json.dumps({"msg": {"type": "image", "url": "%s" % tgpic_url}})
        # repp2 = requests.post(url=imgpost, data=postdata36, headers=headers)
        # print(repp2)
        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = fasongneir2 + huanghang + tupianxianshi + tgpic_url
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        FormData = {
            "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
            "content": content,
            "summary": fasongneir,
            "contentType": 2,

            "topicIds": [

            ],
            "uids": [
                "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
            ],
            "url": ""
        }
        res = requests.post(url=url, json=FormData, headers=HEADERS)
        print(res.text)



    elif dynamic_type == 64:
        # 专栏动态
        content = json.loads(cardss)
        zltitle = content['title']
        zlpic_url = content['image_urls'][0]
        zlpic_url = str(zlpic_url)
        print(zltitle)
        print(zlpic_url)
        typ = bilitype.bilitype(dynamic_type)
        # fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
        #     zltitle) + '\n'
        fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n'

        fasongneir2 = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '动态类型：' + typ + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + 'B站链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
            zltitle) + '\n'
        print(fasongneir)
        postdata = json.dumps({"msg": fasongneir})
        time.sleep(2)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        # time.sleep(2)
        # zlpic_url = pic['img_src']

        # print(pic['img_src'])
        # postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
        # repp2 = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp2)
        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = fasongneir2 + huanghang + tupianxianshi + zlpic_url
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        FormData = {
            "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
            "content": content,
            "summary": fasongneir,
            "contentType": 2,

            "topicIds": [

            ],
            "uids": [
                "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
            ],
            "url": ""
        }
        res = requests.post(url=url, json=FormData, headers=HEADERS)
        print(res.text)
    print("Write OK")
