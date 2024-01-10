# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2024/01/09 23:19:25
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
import time
import yaml
import shutil
import schedule
from modules.uploads import UPLOADS

uploads = UPLOADS()

with open("config.yml", "rb") as fp:
    config = yaml.safe_load(fp)

#print(config)

for backup in config["backup_dirs"]:
    backup_dir = backup["dir"]
    if backup["compression"]:
        compression_type = backup["compression_type"]
        shutil.make_archive("./bbackup/test", compression_type, backup["dir"])
    for depend in config["depends"]:
        pass

