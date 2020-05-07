

import subprocess

import requests

# ######## a. agent方案 #####
# res = subprocess.getoutput('ipconfig')
#
# ip = res[10:13]
#
# print(ip)
#
#
# #### request模块将数据提交到API
#
# requests.post('http://127.0.0.1:8000/asset', data=ip)


######## b. ssh类方式 #####

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.51', port=22, username='root', password='123')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result = stdout.read()
print(result)

# 关闭连接
ssh.close()
























