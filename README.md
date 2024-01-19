# Bbackup
A file/folder compression backup cohabit.  
[中文说明](https://github.com/Pidbid/bbackup/blob/main/README_ZH.md)

## Install & Usage 
- clone Bbackup from github  
  > git clone https://github.com/Pidbid/bbackup.git  
  > cd bbackup  
  > pip install -r requirements.txt  
  > copy config_demo.yml and rewname to config.yml  
  > python main.py

## Configuration  
- depends  
  - you can backup file to oss or your own server fron http[post]  
- backup_dirs  
  - dir # your local backup dir  
  - name # backup task name and it will be the floder on oss  
  - compression # compression or not when backup task running  
  - exclude_folders # some folders that were excluded from the backup task
  - exclude_files # some files that were excluded from the backup task  
  - schedule # The time interval for the backup task  
- ali_oss  
  - endpoint # alioss endpoint  
  - bucket # alioss bucket  
  - oss_access_key_id # aliyun your own access_key  
  - oss_access_key_secret # aliyun your own access_secret  

## Features
- [x] backup folder  
- [ ] backup files  
- [x] alioss support  
- [ ] tencent cloud oss support  
- [ ] http post support  

## About  
[Wicos](https://www.wicos.me)
