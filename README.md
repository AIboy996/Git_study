# learn git
learn how to git

### 最常用的几个命令
```git
1、初始化仓库
git init

2、链接远程库
git remote add [name一般设置为origin] [adress]

3、修改文件之后存入暂存区
git add [file name]

4、从暂存区提交到仓库区
git commit -m [message]

5、推送到远程仓库——GitHub
git push [remote] [branch]

第一次推送可以加上 -u参数
git push -u [remote] [branch]
由于远程库是空的，我们第一次推送master分支时，加上了-u参数，
Git不但会把本地的master分支内容推送的远程新的master分支，
还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

6、把GitHub上的更新下载下来，并且合并
git pull [remote] [branch]
```
