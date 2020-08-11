## Git 版本管理程序
--------------------------------

## 如何安装git
Ubuntu系统可使用apt进行安装
```
sudo apt-get install git
```
## git初始化
```
git init
git add xxx.txt  把文件修改提交到暂存区
git add yyy.md  把暂存区的文件提交到当前分支
git commit -m 'your subscribe'
git status
git diff  查看修改内容
git log  查看提交历史
git log --pretty=oneline  减少输出参数

[版本回退]
git reset --hard HEAD^  回退到上一版本
git reset --hard 1094a  回退到未来版本（1094a是版本号)
git reflog  查看命令历史（可用来找版本号）

[撤销修改]
git diff HEAD -- xxx.txt  查看工作区和版本库里面最新版本的区别
git checkout -- xxx.txt  撤销工作区的修改，但不会撤销暂存区的修改
git reset HEAD xxx.txt  把暂存区的修改撤销掉，重新放回工作区

[删除文件]
git rm xxx.txt
git commit -m 'remove xxx.txt'
(如果删错了，可以用git checkout -- xxx.txt撤销工作区的修改)

[远程仓库]
ssh-keygen -t rsa -C "youremail@qq.com"  然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。

如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：
然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容。

GitHub允许你添加多个Key。假定你有若干电脑，你一会儿在公司提交，一会儿在家里提交，只要把每台电脑的Key都添加到GitHub，就可以在每台电脑上往GitHub推送了。

[关联远程仓库]
git remote add origin git@github.com:HarveyRH360/learngit.git

[取消与远程库的关联]
git remote remove origin

[把本地内容推送到远程库上]
git push -u origin master  将本地的master和远程的master关联起来，在以后推送或拉取时就可以简化命令
git push origin master

[SSH 警告]
当你第一次使用Git的clone或者push命令连接GitHub时，会得到一个警告：

The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
RSA key fingerprint is xx.xx.xx.xx.xx.
Are you sure you want to continue connecting (yes/no)?
这是因为Git使用SSH连接，而SSH连接在第一次验证GitHub服务器的Key时，需要你确认GitHub的Key的指纹信息是否真的来自GitHub的服务器，输入yes回车即可。

Git会输出一个警告，告诉你已经把GitHub的Key添加到本机的一个信任列表里了：

Warning: Permanently added 'github.com' (RSA) to the list of known hosts.
这个警告只会出现一次，后面的操作就不会有任何警告了。

如果你实在担心有人冒充GitHub服务器，输入yes前可以对照GitHub的RSA Key的指纹信息是否与SSH连接给出的一致。

[从远程库克隆]
git clone git@github.com:HarveyRH360/learngit.git
git clone https://github.com/HarveyRH360/learngit.git  使用https除了速度慢以外，还有个最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用https。

[分支管理]
git checkout -b dev  创建并切换到dev分支，-b参数表示创建并切换，相当于以下两个命令：
git branch dev  创建分支dev
git checkout dev  切换分支

git branch  查看所有分支
git branch -d dev  删除分支

git merge dev  合并指定分支到当前分支，快速合并(Fast-forward)。
git switch -c dev  创建并切换到新的分支。使用switch切换分支更科学，不容易搞混
git switch master 直接切换到已有的分支

[解决冲突]
创建dev分支并修改内容、提交
回到master分支并修改内容、提交
合并dev分支到当前分支：存在冲突，并使用>>>>/<<<<标记了冲突的内容
手动修改master分支的内容并提交
git log --graph --pretty=oneline --abbrev-commit  可以使用该命令查看分支合并图
删除dev分支

[分支管理策略]
合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。

git merge --no-ff -m "merge with no-ff" dev  禁用Fast forward模式进行分支合并
git log --graph --pretty=oneline --abbrev-commit  查看分支合并图

[Bug分支]



[标签管理]
git tag v1.0  创建标签
git tag  查看所有标签。标签是按照字母排序的，而不是时间顺序。
git log --pretty=oneline --abbrev-commit  简要查看提交历史
git tag v0.9 f323cd  给某个commit id创建标签
git show v0.9  查看标签信息
git tag -a v2.0 -m 'version 2.0 released' 323de  创建带有说明的标签
git tag -d v0.9  删除标签
git push origin v2.0 推送某个标签到远程
git push origin --tags  推送全部本地标签到远程

删除远程标签比较麻烦一点：
git tag -d v0.9  先删除本地标签
git push origin :refs/tags/v0.9  再从远程删除
```
