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
    fasongneir = '-----------------Bilibili转发开始-----------------'
    print(fasongneir)
    postdata = json.dumps({"msg": fasongneir})
    time.sleep(2)
    repp = requests.post(url=imgpost, data=postdata, headers=headers)
    print(repp)


    if tp == 2:
        nr = data['card']
        js = json.loads(nr)
        nr = js['item']['description']
        pic_url = js['item']['pictures']
        print(nr)


        for pic in pic_url:
            print(pic['img_src'])
            jpg = pic['img_src']
            # print(jpg)
            postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg}})
            time.sleep(2)
            repp = requests.post(url=imgpost, data=postdata, headers=headers)
            print(repp)


        return nr

    elif tp == 64:
        nr = data['card']
        js = json.loads(nr)

        zltitle = js['title']
        zlpic_url = js['image_urls'][0]
        print(zltitle)
        print(zlpic_url)
        # jpg = pic['img_src']
        # print(jpg)
        postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
        time.sleep(4)
        repp = requests.post(url=imgpost, data=postdata, headers=headers)
        print(repp)

        return zltitle

    elif tp == 4:
        nr = data['card']
        js = json.loads(nr)
        wenzi = js['item']['content']
        print(wenzi)
        return wenzi
    elif tp == 8:
        # 投稿动态
        nr = data['card']
        js = json.loads(nr)
        tgtlttle = js['title']
        tgpic_url = js['pic']
        postdata = json.dumps({"msg": {"type": "image", "url": "%s" % tgpic_url}})
        time.sleep(4)
        repp = requests.post(url=imgpost, data=postdata, headers=headers)
        print(repp)


        return tgtlttle



#
#
# if __name__ == '__main__':
#     d=ifzf(607804998435580564)
#     print(d)


