# tagbar - 更愉快的浏览代码

https://github.com/majutsushi/tagbar

tagbar相当于是给出了一个代码的大纲，让你读代码更方便。

## 安装
将github后缀放到Vundle的vimrc里面，PluginInstall安装即可：
```
Plugin 'majutsushi/tagbar'
```
但是要注意的是，tagbar需要一些依赖，详细请看github的Dependencies模块。

## 安装依赖
- ctags
```
git clone https://github.com/universal-ctags/ctags.git
```
Before running ./autogen.sh, install some packages.   
On Debian-based systems (including Ubuntu), do:
```
$ sudo apt install \
    gcc make \
    pkg-config autoconf automake \
    python3-docutils \
    libseccomp-dev \
    libjansson-dev \
    libyaml-dev \
    libxml2-dev
```
安装Ctags
```
$ ./autogen.sh
$ ./configure --prefix=/where/you/want # defaults to /usr/local
$ make
$ make install # may require extra privileges depending on where to install
```

