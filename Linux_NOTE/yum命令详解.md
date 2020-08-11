# Linux yum命令详解
---

## 安装
yum install 全部安装
yum install package_Name 安装指定的安装包
yum groupinstall group_Name 安装程序组group_Name

## 更新和升级
yum update 全部更新
yum update package_Name 更新指定程序包
yum check-update 检查可更新的程序
yum upgrade package_Name 升级指定程序包
yum groupupdate group_Name 升级指定程序组

## 查找和显示
yum info package_Name 显示安装包信息
yum list 显示所有已经安装和可以安装的程序包
yum list package_Name 显示指定程序包安装情况
yum groupinfo group_Name 显示程序组信息
yum search string 根据关键字string查找安装包

## 删除程序
yum remove/erase package_Name 删除指定程序包
yum groupremove group1 删除程序组group1
yum deplist package1 查看程序package1依赖情况

5 清除缓存
yum clean packages 清除缓存目录下的软件包
yum clean headers 清除缓存目录下的 headers
yum clean oldheaders 清除缓存目录下旧的 headers
yum clean, yum clean all (= yum clean packages; yum clean oldheaders) 清除缓存目录下的软件包及旧的headers
