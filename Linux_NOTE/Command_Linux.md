### SCP命令
```
scp -r -i ~/.ssh/xxx.pem root@43.224.34.73:/home/lk ~/cpfile
scp -r -i ~/.ssh/xxx.pem /root/lk root@43.224.34.73:/home/lk/cpfile
```
### Ubuntu查找已安装的软件
```
apt list --installed
或
dpkg -l
```
### 查找某款软件
```
dpkg -l | grep xxx
```
### Ubuntu卸载已安装的软件

> sudo dpkg -r Name
> apt remove Name
