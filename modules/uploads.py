# -*- encoding: utf-8 -*-
"""
@File    :   uploads.py
@Time    :   2024/01/09 23:46:35
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
import os
import sys
import yaml
import requests
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from qiniu import Auth, put_file, etag


class UPLOADS:
    def __init__(self):
        "This is init fun"
        self.config = yaml.safe_load(open("config.yml", "rb"))

    def __path2file__(self, path: str):
        return path.split("/")[-1]

    def __file_exist__(self, path: str):
        pass

    def aliyun(self, path: str, target: str = None):
        alioss_key_id = self.config["ali_oss"]["oss_access_key_id"]
        alioss_key_secret = self.config["ali_oss"]["oss_access_key_secret"]
        self.aliauth = oss2.Auth(alioss_key_id, alioss_key_secret)
        bucket = oss2.Bucket(
            self.aliauth,
            "https://{}.aliyuncs.com".format(self.config["ali_oss"]["endpoint"]),
            self.config["ali_oss"]["bucket"],
        )
        object_name = (
            self.__path2file__(path)
            if not target
            else target + self.__path2file__(path)
        )
        bucket.put_object_from_file(
            object_name,
            path,
        )
        url = bucket.sign_url("GET", object_name, 3600, slash_safe=True)
        return url

    def http_post(self, url: str, path: str):
        res = requests.post(
            url=self.config["http_post"]["url"],
            files={"file": open(path)},
            headers=self.config["https_post"]["header"],
            json=self.config["https_post"]["body"],
        )
        return res.text

    def tencent_oss(self, path: str):
        pass

    def qiniu_oss(self, path: str, target: str = None):
        q = Auth(
            self.config["qiniu_oss"]["access_key"],
            self.config["qiniu_oss"]["secret_key"],
        )
        key = f"{target}/{path.split('/')[-1]}"
        token = q.upload_token(self.config["qiniu_oss"]["bucket"], key, 3600)
        ret, info = put_file(token, key, path, version="v2")
        return {"ret": ret, "info": info}
