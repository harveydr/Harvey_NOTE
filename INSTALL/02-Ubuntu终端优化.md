# Ubuntu安装后的界面优化

## 基础工具安装
```
sudo apt install python python3 git curl vim
```

## 安装zsh
```
sudo apt install zsh
```
## 安装oh-my-zsh

> 官方教程：https://ohmyz.sh/#install

若官网链接拒绝访问，则使用国内镜像：
- via curl
```
sh -c "$(curl -fsSL https://gitee.com/shmhlsy/oh-my-zsh-install.sh/raw/master/install.sh)"
```
- via wget
```
sh -c "$(wget -O- https://gitee.com/shmhlsy/oh-my-zsh-install.sh/raw/master/install.sh)"
```
- 优秀的zsh主题

> robbyrussell, gallois, rkj-repos

## autojump、zsh-autosuggestion和zsh-syntax-highlighting
> 参考文档：https://www.zrahh.com/archives/167.html

- autojump:
```
git clone git://github.com/joelthelion/autojump.git
```

cd /autojump，执行:
```
./install.py
```

vim ~/.zshrc，把以下代码加到尾部:
```
# 使用git安装的
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
```

- zsh-autosuggestion
```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# ~/.zshrc:
plugins=(git zsh-autosuggestions) "git是其他插件，空格隔开
```

- zsh-syntax-highlighting
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# ~/.zshrc:
plugins=(git zsh-syntax-highlighting) "git是其他插件，中间用空格
```

## 模糊搜索器ctrlp
> 参考文档：https://github.com/ctrlpvim/ctrlp.vim

安装
```
Plugin 'ctrlpvim/ctrlp.vim'
```
