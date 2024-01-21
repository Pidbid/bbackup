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
from loguru import logger
from modules.uploads import UPLOADS

seconds = 0

uploads = UPLOADS()

with open("config.yml", "rb") as fp:
    try:
        config = yaml.safe_load(fp)
    except yaml.YAMLError as exc:
        logger.error(exc)

logger.add(
    sink="./bbackup.log",
    level="INFO",
    rotation="00:00",
    retention="7 days",
    compression="zip",
    encoding="utf-8",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)


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


def main_job(seconds):
    for backup in config["backup_dirs"]:
        if seconds % schedule2seconds(backup["schedule"]) != 0 and seconds >= 0:
            print(f"skip {seconds}")
            continue
        logger.info(f"start to backup {backup['name']}")
        zip_name = f"{backup['name']}_{int(time.time()*1000)}.zip"
        zip_file = zipfile.ZipFile(f"./backup/{zip_name}", "w", zipfile.ZIP_DEFLATED)
        backup_dir = backup["dir"]
        try:
            exclude_folders = backup["exclude_folders"]
        except:
            exclude_folders = []
        try:
            exclude_files = backup["exclude_files"]
        except:
            exclude_files = []
        if exclude_folders == None:
            exclude_folders = []
        if exclude_files == None:
            exclude_files = []
        for dirpath, dirnames, filenames in os.walk(backup_dir):
            compress_dir = (
                backup_dir[: backup_dir.length - 1]
                if backup_dir[-1] == "/"
                else backup_dir
            )
            if os.path.basename(dirpath) not in exclude_folders:
                for file in filenames:
                    if file not in exclude_files:
                        zip_file.write(
                            os.path.join(dirpath, file),
                            arcname=os.path.join(
                                dirpath.replace(compress_dir, ""), file
                            ),
                        )
        zip_file.close()
        if backup["compression"]:
            for depend in config["depends"]:
                uploads.aliyun(f"./backup/{zip_name}", f'{backup["name"]}/')
                logger.info(f'{backup["name"]} backuped')
            os.remove(f"./backup/{zip_name}")


if __name__ == "__main__":
    while True:
        main_job(seconds=seconds)
        seconds += 1
        time.sleep(1)
