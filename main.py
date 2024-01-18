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
import re
import os
import time
import yaml
import zipfile
import schedule
from loguru import logger
from modules.uploads import UPLOADS


seconds = 0

uploads = UPLOADS()
# zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

with open("config.yml", "rb") as fp:
    config = yaml.safe_load(fp)

# print(config)


def schedule2seconds(schedule_str: str):
    s_day = 0
    s_hour = 0
    s_minute = 0
    s_second = 0
    pattern = re.compile(r"(\d+)([dhms])")
    matches = pattern.findall(schedule_str)
    for i in matches:
        if i[1] == "d":
            s_day = int(i[0])
        elif i[1] == "h":
            s_hour = int(i[0])
        elif i[1] == "m":
            s_minute = int(i[0])
        elif i[1] == "s":
            s_second = int(i[0])
    return s_day * 24 * 60 * 60 + s_hour * 60 * 60 + s_minute * 60 + s_second


# print(schedule2seconds('1m25s'))


def main_job():
    global seconds
    for backup in config["backup_dirs"]:
        if seconds % schedule2seconds(backup["schedule"]) != 0:
            continue
        zip_name = f"{backup['name']}_{int(time.time()*1000)}.zip"
        zip_file = zipfile.ZipFile(f"./bbackup/{zip_name}", "w", zipfile.ZIP_DEFLATED)
        backup_dir = backup["dir"]
        try:
            exclude_folders = backup["exclude_folders"]
        except:
            exclude_folders = []
        try:
            exclude_files = backup["exclude_files"]
        except:
            exclude_files = []
        for dirpath, dirnames, filenames in os.walk(backup_dir):
            if dirpath not in exclude_folders:
                for file in filenames:
                    zip_file.write(os.path.join(dirpath, file))
        zip_file.close()
        if backup["compression"]:
            for depend in config["depends"]:
                uploads.aliyun(f"./bbackup/{zip_name}", f'{backup["name"]}/')
                logger.info(f'{backup["name"]} backuped')

schedule.every(1).seconds.do(main_job)
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        seconds += 1
        time.sleep(1)
