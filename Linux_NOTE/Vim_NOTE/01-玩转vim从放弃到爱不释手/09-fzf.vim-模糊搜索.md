# fzf.vim 模糊搜索
https://github.com/junegunn/fzf.vim

## 安装
```
Plugin 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plugin 'junegunn/fzf.vim'
```
> fzf是用go语言编写的高性能的命令行搜索工具，fzf.vim则是把fzf加载到vim中的一个实现。所以fzf.vim需要依赖fzf。

## 用法

- Files [PATH] 模糊搜索目录
- Ag [PATTERN] 模糊搜索字符串

```
:Files . <回车> 列出当前目录下的所有文件
:Files . <回车> NameFile 模糊搜索文件
```

