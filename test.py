# -*- encoding: utf-8 -*-
"""
@File    :   test.py
@Time    :   2024/01/09 23:32:28
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
import yaml
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from modules.uploads import UPLOADS


upload = UPLOADS()

upload.aliyun("./requirements.txt","test/")