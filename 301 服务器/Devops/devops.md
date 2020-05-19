分支
GitLab CE/EE
除了版本控制外，提供了缺陷管理、持续集成

git flaw 

devops  开发和运维的组合 development operations，加强开发和运维的协作，广义是说这个产品的生命周期，参与的所有角色
一种文化，一种理念，我们使用很多自动化工具来实现它，比如gitlab

devops能够提升代码质量，提升产品质量
1、自动化测试 单元测试 sona
2、持续集成 就是代码合并

gitlab安装
yum install -y curl policy

上传包
rpm -ivh 包

gitlab包 本身带了很多服务有nginx,postgresql,redis

组，用户，项目
git
jenkins 基于java开发的持续集成工具，提供了数百个插件提供bulid、deploying
要装JDK环境

  查找配置文件目录
rpm -ql jenkins
改用户名字
systemctl start jenkins
安装插件，直接将插件解压扔到plugn目录下就可以
创建一个项目 ，构建一个自由风格的软件项目
默认生成一个workspace目录
源码管理

date +%F-%H-%M-%S

#!/usr/bin/sh
code_dir="/var/lib/jenkins/workspace/My-f"

在Jenkins构建触发器, 选择push和merge 选择分支 和生成token
在jitlab下项目下设置 intergrations(集成) 填入   n token ，和 jenkins url
添加 webhook 钩子函数

Jenkins把构建状态返回给了gitlab
系统管理，系统设置 ，gitlab的url,