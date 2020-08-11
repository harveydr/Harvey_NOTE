## Linux使用yum安装mysql8
> 参考文档：https://www.cnblogs.com/4666yy/p/11066221.html

- 下载安装包：
```
wget http://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
```
- 执行mysql rpm包
```
rpm -ivh mysql80-community-release-el7-1.noarch.rpm
```
- 安装mysql server
```
yum install mysql-server
```
- 权限设置（必须，不然无法启动mysql）
```
chown mysql:mysql -R /var/lib/mysql
```
- 初始化mysql
```
mysqld --initialize
```
- 启动mysql
```
systemctl start mysqld
```
- 查看mysql运行状态
```
systemctl status mysqld
```
- 查看mysql配置文件
```
/etc/my.cnf
```
- 重置登录密码：刚开始安装的Mysql5.7是会随机生成一个root密码的，我们要先找到这个随机密码，然后改新密码。我们可以通过grep命令查找随机root密码。
```
grep "password" /var/log/mysqld.log
```
- 使用mysql重置密码
```
mysql>set password = 'root@123456';
```

