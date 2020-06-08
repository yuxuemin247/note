#### 	一. 版本控制器的分类:

- `SVN `

  集中式版本控制器(必须有中央服务器)，一旦服务器毁灭, 代码就消失·

- GIT

  分布式版本控制器 ，即便没有中央服务器一样可以本地版本控制

#### 二. GIT

- 安装:https://gitforwindows.org/

  - 下载Git源代码压缩文件

    ```
    wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.23.0.tar.xz
    ```

  - 解压缩和解归档

    ```
    xz -d git-2.23.0.tar.xz
    tar -xvf git-2.23.0.tar
    ```

  - 安装底层依赖库

    ```
    yum -y install libcurl-devel
    yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
    ```

  - 安装配置

    ```
    cd git-2.23.0
    ./configure --prefix=/usr/local    
    #可以指定安装目录，统一管理
    ```

  - 构建和安装

    ```
    make && make install
    ```

  - 安装完成检查自己的git版本

    ```
    git --version
    git config --global user.email "yuxuemin247@163.com"
    git config --global user.name "于学敏"
    ```

#### 三. GIT使用

- git 从clone 开始使用

  - 构建ssh免密连接，将公钥放到代码托管平台

    ```
    ssh-keygen -t rsa -b 2046 -c "yxuuemin247@163.com"
    ```

  - 克隆代码

    ```
    git clone --depth=1 仓库地址 [想改的文件夹名称]
    #只保留最新代码，最后一次的提交记录。
    
    #git 指定分支拉取
    ```

  - 创建分支

    ```
    git branch 分支名 要基于的分支名
    #远程分支加 origin
    ```
  
- git从本地初始化 使用

  - 进入文件夹,本地仓库初始化

  ```
    git init
  ```

  - 在本地进行版本控制

    ```
    git add .    
    git commit -m "提交信息"
    ```

  - 在码云/`github/gitlab`创建仓库

    ```
    初始化仓库的那些选项不要选，
    ```

  - 关联远程仓库

    ```
    git remote add origin    https://gitee.com/come_along/code.git 
    origin是远程仓库的别名，以后使用origin就可以了。一般大家都默认使用origin作为别名
    git remote remove origin
    取消远程关联
    ```
  -  推送

    ```
     git  push -u master:master
     #其中，`-u`是`--set-upstream`的缩写，用来指定推送的服务器仓库，后面的origin就是刚才给仓库起的简短的别名，冒号前面的master是本地分支名，冒号后面的master是远程分支名，如果本地分支master已经和远程分支master建立过关联，则冒号以及后面的部分可以省略。									
    ```

#### 四. Git的标准流程

分支管理策略

##### git-flow

- 两个长线分支: master 、develop

- 三个短线分支 : feature 、release 、`hotfix`

  ```
  feature（开发特定功能的分支，开发结束后合并到develop）
  ```

  ```
  release（从develop分离出来的为发布做准备的分支,发布结束后合并到master和develop)
  ```

  ```
  hotfix（产品发布后出现问题时紧急建立的分支，直接从master分离，问题修复后合并到master并打上标签，同时还要合并到develop来避免将来的版本遗漏了这个修复工作，如果此时有正在发布中的release分支，还要合并到release分支）
  ```

- ##### 开发新功能

  - 从develop分支创建feature分支

    ```
    git switch -c  feature/user develop
    或者
    git checkout -b feature/user develop
    ```

  - 在`feature`分支上进行开发并实施版本控制

    ```
    git add . 
    git commit -m "xx"
    ```

  - 工作完成，将feature分支合并到develop分支

    ```
    git checkout develop
    git merge --no-ff feature/user
    git branch -d feature/user
    git push origin develop
    ```

- 发布

  - 从develop分支创建release分支

    ```
    git checkout -b release-0.1 develop
    git push -u origin release-0.1
    ...
    git pull
    git commit -a -m "xxx"
    ```

  - 将release分支合并回master和develop分支

    ```
    git checkout master
    git merge --no-ff release-0.1
    git push
    
    git checkout develop
    git merge --no-ff release-0.1
    git push
    
    git branch -d release-0.1
    git push --delete release-0.1
    git tag v0.1 master
    git push --tags
    
    ```

- 修复线上bug

  - 创建`hotfix`分支

    ```
    git checkout -b hotfix-0.1.1 master
    git push -u origin hotfix-0.1.1
    ... ... ...
    git pull
    git commit -a -m "............"
    ```

  - 将`hotfix`分支合并回`develop`和`master`分支。

    ```
    git checkout master
    git merge --no-ff hotfix-0.1.1
    git push
    
    git checkout develop
    git merge --no-ff hotfix-0.1.1
    git push
    
    git branch -d hotfix-0.1.1
    git push --delete hotfix-0.1.1
    git tag v0.1.1 master
    git push --tags
    ```

- Git-flow流程比较容易控制各个分支的状况，但是在运用上`github-flow`要复杂得多，因此实际使用的时候通常会安装名为`gitflow`的命令行工具（Windows环境的Git自带了该工具）或者使用图形化的Git工具（如`SourceTree`）来简化操作

##### `github-flow`（PR流程）

- 克隆服务器上的代码到本地

  ```
  git clone git@gitee.com:jackfrued/python.git
  ```

- 创建并切换到自己的分支

  ```
  git switch -c 分支名
  或者
  git branch -b 分支名
  ```

- 在自己的分支上开发并作本地版本控制

  ```
  git add . 
  git commit -m "xxx"
  ```

- 将自己的分支推到服务器

  ```
  git push origin 分支名
  ```

- 在线发起一次合并请求(Pull Request 或者 Merge Request),请求将自己的工作成果合并到`master`分支，合并之后可以删除该分支。

  ```
  这种分支管理策略就是被称为github-flow或PR的流程，它非常简单容易理解，只需要注意以下几点：
  1. master的内容都是可以进行发布的内容（不能直接在master上进行修改）。
  2. 开发时应该以master为基础建立新分支（日常开发任务在自己的分支上进行）。
  3. 分支先在本地实施版本控制，然后以同名分支定期向服务器进行push操作。
  4. 开发任务完成后向master发送合并请求。
  5. 合并请求通过审查之后合并到master，并从master向正式环境发布。
  当然，github-flow的缺点也很明显，master分支默认就是当前的线上代码，但是有的时候工作成果合并到master分支，并不代表它就能立刻发布，这样就会导致线上版本落后于master分支。
  ```

- 如果Pull Request（Merge Request）被接受那么工作成果就会出现在master分支上
  如果合并代码时出现冲突无法自动合并，应该先通过git pull将冲突代码拉到本地，使用
  `git diff`查看哪些地方发生了冲突，而是要当面沟通手动解决冲突以后重新提交代码，将自己的分支push到服务器，再次发起合并请求。

#### 五.  其他操作

##### 	分支操作

- 创建和切换分支

  ```
  git branch 分支名 [要基于的分支名]
  git switch 分支名
  ```

  或

  ```
  git switch  -c  分支名
  git checkout -b 分支名
  ```

- 关联远程分支

  - 如果当前分支还没有关联到远程分支

    ```
    git branch -u origin/develop
    ```

  - 如果需要为指定的分支关联远程分支

    ```
    git branch -u origin/develop 分支名
    ```

  - 或者创建分支时，使用--track参数，关联远程分支

    ```
    git branch --track 分支名 origin/develop
    ```

  - 解除本地分支与远程分支的关联

    ```
    git branch --unset-upstream 分支名
    ```

- 分支合并

  ```
  git switch develop   #切换到要合并到的分支
  git merge --no-ff feature/user 
  ```

  --no-ff是指不使用Fast Forward合并。使用快速合并，分支上的历史版本就全部丢掉了。

- 合并冲突

  在合并分支时，没有冲突的部分Git会自动合并。如果发生了冲突，会有`CONFLICT (content): Merge conflict in <filename>. Automatic merge failed; fix conflicts and then commit the result`（自动合并失败，修复冲突之后再次提交）的提示，git pull拉取代码，     `git diff `来查看冲突部分，解决冲突后，重新提交

- 分支变基

  分支合并操作可以将多个分支上的工作成果最终合并到一个分支上，在多次合并操作之后，分支可能会变得非常的混乱和复杂。为了解决这个问题，可以使用`git rebase`操作来实现分支变基。

  变基后和合并就是扁平的，直直一条线了。

  ```
  git rebase develop
  git switch develop
  git merge feature/user
  注意：绝对不能在公共分支（如develop）上做变基操作！！！
  ```

- 删除分支

  ```
  git branch -d 分支名
  git push origin --delete 远程分支名  #删除远程分支名 
  ```

##### 临时保存

- ```
  git stash      #临时保存
  git stash pop  #恢复刚才的工作
  #将当前工作区和暂存区发生的变动放到一个临时的区域(堆栈)，让工作区变干净。这个命令适用于手头工作还没有提交，但是突然有一个更为紧急的任务（如线上bug需要修正）需要去处理的场景。
  #临时保存手头工作，让工作区跟暂存区和仓库是同步状态
  ```

##### 版本回退

- git reset 

  - --soft      只把本地仓库回退，暂存区和工作区都不改变(撤回commit操作)
  - --mixed  默认的，只回退暂存区和本地仓库，工作区不改变 

  - --hard    本地仓库、暂存区、工作区都回退

  ```
  git reset --hard 哈希码
  git reset --hard HEAD^
  git reset --hard HEAD~1
  ```

  ```
  #拉取和强制覆盖
  git fetch  --all
  git reset  --hard origin/master
  git pull
  ```

  git log

  ```
  git log    提交记录，回退后git log查不到后面的提交记录
  git reflog 可以查看到所有的提交记录，版本
  ```


  - git remote -v   #查看是否有远端仓库对应

  - git fetch  + git merge

    ```
    等同于git pull 拉下来自动合并
    git pull origin 分支名   #拉取远程分支合并到本地分支
    ```

##### 日志查看

- git log

  ```
  git log --graph --oneline --abbrev-commit
  ```

- git `reflog`

  查看所有的日志

##### 其他用法

- 查看区别

  ```
  git diff 
  #常用于比较工作区和仓库、暂存区与仓库、两个分支间有什么差别
  ```

- 打标签

  ```
  git tag v0.1 master
  git push --tags
  ```

- 用暂存区文件恢复工作区文件

  ```
  git restore 文件名
  ```

- 将add添加到暂存区的文件取消 追踪

  ```
  git rm --cached  
  ```

- 在线生成版本忽略文件

  ```
  在线生成版本控制忽略文件：http://gitignore.io/
  ```

- 挑选某个分支的单次提交并作为一个新的提交引入到你当前分支上。

  ```
  git cherry-pick
  ```

- 撤回提交信息

  ```
  git revert
  ```

- 下载远程仓库的所有变动，然后再根据需要进行合并操作

  ```
  git fetch origin master:temp
  git merge temp
  #这两个合起来相当于git pull(拉取下来自动合并)
  ```

  











