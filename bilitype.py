import sys
import time
import ifzf
import requests
import re
import os
import json
from datetime import datetime, timedelta



def bilitype(dynamic_type):
    dynamic_type=dynamic_type
    if dynamic_type==1:
        return "转发动态"

    elif dynamic_type == 2:
        return "图文动态"

    elif dynamic_type == 4:
        return "文字动态"

    elif dynamic_type == 8:
        return "投稿动态"

    elif dynamic_type == 64:
        return "专栏动态"




# if __name__ == '__main__':
#     print(bilitype(4))
