# Bbackup  
一个文件或文件夹备份的工具。
[English](https://github.com/Pidbid/bbackup/blob/main/README.md)

## 安装与使用  
- 从github克隆之后运行一下代码  
  > git clone https://github.com/Pidbid/bbackup.git  
  > cd bbackup  
  > pip install -r requirements.txt  
  > 复制config_demo.yml 并修改配置后命名为config.yml  
  > python main.py

## 配置  
- depends  
  - 你可以选择同时向哪些目标地址备份，支持阿里云oss、腾讯云oss、http 的 post提交方法  
- backup_dirs  
  - dir # 本地待备份地址  
  - name # 备份任务的名字，备用来作为oss的备份文件夹  
  - compression # 备份时是否进行压缩  
  - exclude_folders # 不进行备份的文件夹
  - exclude_files # 不进行备份的文件  
  - schedule # 多长时间备份一次  
- ali_oss  
  - endpoint # 阿里云oss的 endpoint  
  - bucket # 阿里云oss的 bucket  
  - oss_access_key_id # 阿里云的 access_key  
  - oss_access_key_secret # 阿里云的 access_secret  
- qiniu_oss  
  - bucket # 七牛 bucket 的名称  
  - access_key  
  - secret_key  
- http_post:  
  - url # http post 的 url  
  - body # http body  
  - header # http header config

## 特性  
- [x] 文件夹备份  
- [ ] 文件备份  
- [x] 支持阿里云oss  
- [ ] 支持腾讯云oss  
- [x] 支持http 的 post方法进行备份  
- [x] 支持七牛oss

## 关于    
[Wicos](https://www.wicos.me)
