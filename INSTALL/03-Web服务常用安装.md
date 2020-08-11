### Ubuntu安装Apache, MySQL, PHP7, phpMyAdmin

> 参考文档：https://blog.csdn.net/sanve/article/details/80770675

- CentOS7.3安装PHP7.2
虽然阿里云服务器ECS中的CentOS系统的默认源已经改为了阿里的mirror，但是如果直接使用命令 yum -y install php 安装的版本却不是php7。下文带你用最简单、最快的方式安装php7。

1. 删除系统中可能存在之前安装的php相关文件
```bash
yum -y remove php*
```
2. 不必担心会影响已经配置好的阿里源
```bash
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
3. 安装PHP7.2
```bash
yum -y install php72w php72w-cli php72w-common php72w-devel php72w-embedded php72w-fpm php72w-gd php72w-mbstring php72w-mysqlnd php72w-opcache ph  p72w-pdo php72w-xml
```

4. 如果你在使用Laravel框架，那么经过上述操作之后你会发现还缺少一个b cmath 扩展。在网上也有各种各样的安装命令，但大多数都麻烦。下面这条命令可以做到，一次安装成功。
````
yum install php72w-bcmath
````
