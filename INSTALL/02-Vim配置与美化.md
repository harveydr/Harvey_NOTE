## vim-instant-markdown
> 参考教程：https://blog.csdn.net/Demorngel/article/details/69036044?utm_source=blogxgwz1

- 安装
```
sudo apt-get install nodejs npm
sudo npm -g install instant-markdown-d
```
如果你不想自动打开预览窗口的话，你可以在/etc/vim/vimrc中写入:
```
let g:instant_markdown_autostart = 0
```
当你想要预览的时候，在vim的普通模式下输入
```
:InstantMarkdownPreview
```
当然也可以将上面的命令映射到其他键位，比如下面将其映射到F11

> map \<F11\> :InstantMarkdownPreview\<CR\>

## 模糊搜索器ctrlp
> 参考文档：https://github.com/ctrlpvim/ctrlp.vim

安装
```
Plugin 'ctrlpvim/ctrlp.vim'
```
## 配置vimrc，实现自动补全与快捷映射
```
set nu
syntax on
" ,w实现保存
let mapleader=','
inoremap <leader>w <Esc>:w<cr>
" 自动补全
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
```
## 安装Vundle
> 官方教程：https://github.com/VundleVim/Vundle.vim

克隆文件：
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```
配置vimrc文件：
```
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
```
执行：
```
:PluginInstall
```
## 安装Vim美化插件
- vim-startity： https://github.com/mhinz/vim-startify
- vim-airline： https://github.com/vim-airline/vim-airline
- indentline： https://github.com/yggdroot/indentline

配置vimrc文件：
```
Plugin 'mhinz/vim-startify'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'Yggdroot/indentLine'
```
执行：
```
:PluginInstall
```


## autojump、zsh-autosuggestion和zsh-syntax-highlighting

> 参考文档：https://www.zrahh.com/archives/167.html
