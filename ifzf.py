import sys
import time

import requests
import re
import os
import json



def ifzf(tpid):
    tpid=tpid
    url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id={uid}'.format(uid=tpid)

    imgpost = 'https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url=url)
    result = json.loads(str(response.content, 'utf-8'))
    # dt=html.json()['data']['cards'][0]
    data = result['data']['card']
    print(data)

    tp = data['desc']['type']
    print(tp)
    # fasongneir = '---------Bilibili转发开始---------'
    # print(fasongneir)
    # postdata = json.dumps({"msg": fasongneir})
    # time.sleep(2)
    # repp = requests.post(url=imgpost, data=postdata, headers=headers)
    # print(repp)


    if tp == 2:
        nr = data['card']
        js = json.loads(nr)
        nr = js['item']['description']
        pic_url = js['item']['pictures']
        print(nr)
        # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
        tupian = ""


        for pic in pic_url:
            print(pic['img_src'])
            jpg = pic['img_src']
            # print(jpg)
            # postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg}})
            # time.sleep(2)
            # repp = requests.post(url=imgpost, data=postdata, headers=headers)
            # print(repp)
            zuhe = "<img src=\"" + jpg + "\" >"
            tupian += zuhe
        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = nr + huanghang + tupianxianshi + tupian

        return content

    elif tp == 64:
        # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
        tupian=''
        nr = data['card']
        js = json.loads(nr)

        zltitle = js['title']
        zlpic_url = js['image_urls'][0]
        print(zltitle)
        print(zlpic_url)
        # jpg = pic['img_src']
        # print(jpg)
        zuhe = "<img src=\"" + zlpic_url + "\" >"
        tupian += zuhe
        # postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
        # time.sleep(4)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = zltitle + huanghang + tupianxianshi + tupian

        return content

        # return zltitle

    elif tp == 4:
        # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
        tupian = ''
        nr = data['card']
        js = json.loads(nr)
        wenzi = js['item']['content']
        print(wenzi)
        return wenzi
    elif tp == 8:
        # 投稿动态
        # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
        tupian = ''
        nr = data['card']
        js = json.loads(nr)
        tgtlttle = js['title']
        tgpic_url = js['pic']
        zuhe = "<img src=\"" + tgpic_url + "\" >"
        tupian += zuhe
        # postdata = json.dumps({"msg": {"type": "image", "url": "%s" % tgpic_url}})
        # time.sleep(4)
        # repp = requests.post(url=imgpost, data=postdata, headers=headers)
        # print(repp)
        huanghang = "<br />"
        tupianxianshi = '<meta name="referrer" content="no-referrer" />'
        content = tgtlttle + huanghang + tupianxianshi + tupian

        return content


        # return tgtlttle



#
#
# if __name__ == '__main__':
#     d=ifzf(607804998435580564)
#     print(d)

