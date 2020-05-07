##### 一. 版本控制器的分类:

​		

		SVN : 十年前, 非常火的软件. 
			特点: 集中式版本控制器(有中央服务器)
			缺点: 一旦服务器毁灭, 代码就消失		
		GIT : 
			特点: 分布式版本控制器 ，即便没有中央服务器一样可以版本控制
			优点: 相对于SVN, 不用担心服务器挂掉
		相同点:
			服务端(存储代码)
			客户端(用来管理代码)	
##### 二. GIT

​		历史:
​			linux之父发明的
​		安装:
​			网站 : https://gitforwindows.org/

		使用:	
			原始的方法:
				a. 快速开发一个新版本, 上线 V1, 继续开发新的功能V2, 开发了一半	
				b. 紧急 bug 出现, 两个小时解决:			
					将V2的功能放到某一个地方保存			
					然后拷贝线上的代码, 解决bug, 继续上线			
			git的方式:
				a.  初始化管理代码
					git init : 对当前的项目初始化 git
					
					git add <文件> / git add . : 将当前的目录下的文件添加到暂存区
			
					git status : 查看当前目录下面的所有文件的状态
					
					git commit -m '辅助信息' 提交代码到版本库
					
					ps:
						git config --global user.name  "eagon"
						git config --global user.email 'eagom@163.com'
										git会自动检测, 文件的变化
					
						git add <文件> / git add . : 将当前的目录下的文件添加到暂存区
					
						git status : 查看当前目录下面的所有文件的状态
						
						git commit -m '辅助信息' 提交代码到版本库


​					
​			b.  开发一个新的功能, 发短信的功能
​					
​						git add <files> / .
​						
​						git status
​						
​						git commit -m '注释' 将文件提交到本地版本库


​				
​		   c.  短信功能太烧钱了, 想回退到上一版本
​				
​					回滚上一个版本:
​						
​						git reset  --soft / --mix / --hard   commit_id 
​						
​					将代码从本地版本库拉回工作区:
​						
​					    git reset --hard 691cb5f2dfa176871f0d0be8225f34e27c67c248
​	
​					返回上一个最新的版本:
​						git reflog : 查看所有的log日志
​						git reset --hard commit_id


​				
​			d.  现在开发了一个功能(直播功能), 开发到一半, 线上出现bug:
​					
​						方法一: stash	
​							出现bug和修改的文件不是一个文件:
​							
​							git stash : 将之前修改的内容保存到某一个地方 					    						(***************************)
​							修改bug完毕
​							git add .
​							git commit -m 'xinxi '	
​							git stash pop : 将之前 保存的修改部分, 再次拉回来
​								
​							git add .
​							git commit -m 'xxxx'
​							
​							出现bug的文件和修改的文件是一个文件:	
​	                        git stash : 将之前修改部分代码保存到某一个地方
​	                        修改bug完毕
​	                        git add .
​	                        git commit -m 'xinxi '
​						
​							出现冲突:
​								<<<<<<< Updated upstream
​								myage = 123
​								=======
​								age  = 18
​								height = 180
​								>>>>>>> Stashed changes
​	
​							解决方法:
​								手动解决
​									age  = 18
​									height = 180
​										
								git add .
								git commit -m 'xxxxx'						
	
					方法二:
							
					推荐使用 分支
							
					master : 上线代码的时候, 使用的是主分支代码, 需要保证没有任何bug
					dev    : 开发的时候, 使用的分支
									git branch : 查看所有的分支
							
					git branch <分支名> (dev / bug) : 开启一个新的分支
							
					git checkout 分支名 (dev) : 将master上的代码拷贝了一份, 给dev分支开发
							
					需要注意的是:
					以后开发代码的时候, 不能再 master 上开发, 需要自己开一个分支开发, dev
							
					在dev分支上, 开始开发代码:
								vim gongeng.txt
								git add .
								git commit -m 'xxxxxx'	
	                            此时, 出现了一个bug, 需要修复bug:
								
								git checkout master    切换到主分支
								
								git branch bug  : 产生一个新的bug分支
								
								修复bug:
									vim msg.txt
									git add .
									git commit -m 'xxxxxx'
								
								合并bug代码:
									git checkout master
									git merge bug:
										没有冲突: 过
										有冲突: 
											手动解决冲突
										git add .
										git commit -m  'xxxx'
										
							bug修复完毕之后, 又开始到dev分支上进行开发	
							
								git checkout dev
	
							功能开发完毕, 不要贸然的合并代码, 问一下领导, 接下来怎么做?			
	
							合并dev的代码到master上:  (权限属于领导)
							
								git checkout master
								
								git merge dev
								
									出现如下界面, 说明没有任何冲突出现:
										Merge branch 'dev'
										# Please enter a commit message to explain why this merge is necessary,
										# especially if it merges an updated upstream into a topic branch.
										#
										# Lines starting with '#' will be ignored, and an empty message aborts
										# the commit.
									
									如果有冲突出现, 手动解决冲突


​							
​							起分支名:
​								
​								git branch  0603fixmsg 
​								
​							解决完bug后, bug分支有没有必要存在?
​								需要 , 以后查看的时候方便查看问题
​								不需要, bug的分支的使命已经完成,因此删掉 (git branch -d bug)


​				
​				
​				
​				c. 服务端(存储代码的地方)
​					
​					很开心的在家里面和公司办公
​				
​					公用:
​						国外: https://github.com/
​						
​						国内: https://gitee.com/
​						
​	               私用:
​						gitlab (公司自己用)			
​	
​					码云为例:
​						
​						git remote add 远程仓库名 远程仓库地址
​						
						https: https://gitee.com/lupython/s5git.git
						
						git remote add origin https://gitee.com/lupython/s5git.git
						
						报错: 没有全新, 用 https
						
						git : git@gitee.com:lupython/s5git.git
						git remote add origin https://gitee.com/lupython/s5git.git
						需要配置公钥和私钥
						
						方法:
							ssh-keygen -t rsa -C "youemail@163.com"
							一直回车，不用输入密码，完成之后，可以再主目录里找到.ssh文件夹，内有id_rsa和id_rsa.pub两个文件， id_rsa是私钥，id_rsa.pub是公钥
	
							把公钥放到服务器上



						在公司:
							
							现在再master分支上:
								git push origin master
							
								git checkout dev
								
							开发新的功能3:
									开发完毕
									git add .
									git commit -m 'xxxx'
									
									git push origin dev
								
								下班...
						
						回家了:
							
							新的电脑上, 也需要进行公钥私钥的认证
							
							git clone 代码的地址
							
							git branch dev origin/dev
							
							git checkout dev
							
							开发功能4:
								开发完毕
								git add .
								git commit -m 'xxxx'	
								git push origin dev
								
							上班...
						
						回到公司:
							git pull origin dev  : 将线上最新的代码拉到本地, 保证本地的代码是最新的
							开发功能5:
								开发
								
								但是突然忘记提交了....
							
							回家了....


​						
​						回家:
​							开发功能6:
​								git add .
​								git commit -m 'xxxx'
​								
​								git push origin dev
​							
​							上班


​						所有的提交代码,也就是push操作的时候, 如果你没有git pull, 保证本地的代码版本是最新的话, 会报错:
​								! [rejected]        dev -> dev (fetch first)
​								error: failed to push some refs to 'git@gitee.com:lupython/s5git.git'
​								hint: Updates were rejected because the remote contains work that you do
​								hint: not have locally. This is usually caused by another repository pushing
​								hint: to the same ref. You may want to first integrate the remote changes
​								hint: (e.g., 'git pull ...') before pushing again.
​								hint: See the 'Note about fast-forwards' in 'git push --help' for details.
​	

						因此, 我们需要每次push之前, pull一下, 确保代码是最新的


​							
​							
​	协同开发:
​						
​			多人开发同一个项目
​						
​			在你入职的时候, 领导会给你开一个gitlab的账号, 然后将你拉入你要开发的那个项目中
​						
​			接下来, 在你的电脑上, 配置公钥私钥免密登录, 
​						
​			常见的问题:
​							
​					自己的代码自己管, 千万不要手贱, 动别人的代码  (********************)
​							
​					遇到配置文件, config.py, 将配置选项汇总给领导, 让领导改 config.py		

git切换远程分支

##### 三  一些使用

- ```
  #拉取和强制覆盖
  git fetch  --all
  git reset --hard origin/master
  git pull
  ```

- ```
  #git,commit之后,想撤销
  git reset --soft HEAD~1
  #只是撤回commit操作,代码仍然保留
  ```

- ```
  #git 回滚到原来版本
  git reflog  查看
  git reset --hard '名字前几位'
  ```

- git stash

  ```
  save the local change ,and back to the state of your last commit 
   能够将所有未提交的修改（工作区和暂存区）保存至堆栈中，用于后续恢复当前工作目录。
  ```

  


