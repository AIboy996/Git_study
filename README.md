# learn git
learn how to git

### GitHub给出的初始化方法

![image](https://github.com/AIboy996/learngit/blob/master/%E6%96%B0%E5%BB%BA%E5%BA%93.bmp)

### 对应的注释
这里只写命令行方式的注释

...or creat a new repository on the command line
```bash
git init   #初始化本地库

git add README.md   #添加到暂存区

#由于在github上新建库的时候，我没有勾选生成README文件，所以新建的库完全是空的；
#而如果勾选了这个选项会自动生成README文件，并且生成默认分支main

git commit -m "first commit"   #提交到工作区

git branch -M main   #把分支名称改为main

#git的默认分支名称是master，经过提交文件后会自动生成master分支；
#但是github的默认分支是main，为了统一故把本地库的分支也改为main

git remote add origin https://github.com/AIboy996/Python_study.git   #链接到远程库

#这里的origin是可以自定义的远程库名称，一般就命名为origin

git push -u origin main   #把本地库的文件推到远程库上

#由于远程库是空的，我们第一次推送main分支时，加上了-u参数，
#Git不但会把本地的mian分支内容推送的远程新的main分支，
#还会把本地的main分支和远程的main分支关联起来，在以后的推送或者拉取时就可以简化命令。
```
### 在这之后的工作
```git
1、修改了本地文件想要同步到github上

首先  git add [name]

之后  git commit -m [message]

最后  git push origin main

2、在github上修改了文件想要同步到本地

只要  git pull origin main
```
