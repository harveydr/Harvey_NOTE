## SDKMAN!
是在大多数基于Unix的系统上管理多个软件开发工具包的并行版本的工具，它提供了一个方便的命令行界面（CLI）和API来安装、切换、删除和列出sdk相关信息。

## 安装和查看SDKMAN!
```
curl -s "https://get.sdkman.io"|bash
# 安装完成后，在终端输入：
source "$HOME/.sdkman/bin/sdkman-init.sh"

# 安装到自定义位置
# SDKMAN!的默认安装位置为：$HOME/.sdkman，可以通过设置SDKMAN_DIR环境变量来修改安装位置
export SDKMAN_DIR="/usr/local/sdkman" && curl -s "https://get.sdkman.io" | bash

# 查看SDKMAN!版本
sdk version
```
## Beta版本
SDKMAN的Beta版本，包含一些cli的新功能，但是可能不稳定，如果需要使用Beta版本，需要修改~/.sdkman/etc/config文件：
```
# ~/.sdkman/etc/config
sdkman_beta_channel=true
```

然后打开一个终端执行：
```
sdk selfupdate force
```

如果不需要使用Beta版本了，将上面的配置修改为false，在执行一次更新即可。

## 卸载SDKMAN!
SDKMAN!没有提供自动化的卸载方法,可以通过以下命令进行卸载:
```
tar zcvf ~/sdkman-backup_$(date +%F-%kh%M).tar.gz -C ~/ .sdkman
$ rm -rf ~/.sdkman
```

然后从.bashrc，.bash_profile和/或.profile文件中编辑和删除初始化代码片段。如果您使用ZSH，请将其从.zshrc文件中删除。要删除的代码片段如下所示：
```
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
[[ -s "/home/dudette/.sdkman/bin/sdkman-init.sh" ]] && source "/home/dudette/.sdkman/bin/sdkman-init.sh"
```

## 使用SDKMAN！

### 列出支持的软件
> sdk list

### 列出软件的版本
> sdk list grade  # 软件的名称

### 安装软件包
> sdk install gradle  # 软件包名称

### 安装指定版本的软件包
> sdk install gradle 4.4.1  # 后面跟上版本号即可

### 安装本地宝
> sdk install groovey 3.0.0-SNAPSHOT /path/to/groovy-3.0.0-SNAPSHOT

### 卸载包
> sdk uninstall scala 2.11.6

### 选择软件包版本
> sdk use scala 2.12.1

### 设置默认版本
> sdk default scala 2.11.6

### 查看当前使用的版本
> sdk current java

### 查看所有本地宝的当前版本
> sdk current

### 升级软件包
> sdk upgrade sprintboot

### 升级本地所有软件包
> sdk upgrade

### 离线模式
> sdk offline enable  # 激活离线模式

> sdk offline disable  # 关闭离线模式
当电脑没有网的时候，离线模式会进行自动切换

### SDKMAN!自身的版本升级
> sdk selfupdate  

> sdk selfupdate force  # 强制重新安装，也是一种升级的方式
