# 玩转vim-从放弃到爱不释手
---
> 课程地址：（慕课网）https://www.imooc.com/learn/1129

## Vim的下载与安装
- Linux/Unix(mac)：自带Vim

---

## Vim快速增删改查

### 增：
- 使用a/i/o或者A/I/O进入插入模式，然后增加字符。

### 删：
- 使用x快速删除一个字符
- 使用d（delete）配合文本对象快速删除：daw（删除一个单词，包括单词周围的空格）、diw（删除一个单词，不包括空格）、dw（即daw）。
- d和x都可以搭配数字来执行多次。
- dd删除一行
- dt)：删除光标到本行“)”之间的所用内容。
- d$：删除到行尾。
- d0：删除到行首。
- 2dd：删除两行。
- 4x：删除4个字符。
- （visual模式下）v+移动选择+d或者x（删除选中字符）、V+移动选择+d/x（删除选中的行）。

### 改：
- 常用的有三个，r(replace)、c(change)、s(substitute)。
- (normal模式)使用r替换一个字符：ra（将光标所在字符替换成a）、rs、rb；使用R（大写的R）直接向后进行替换，即边输入边替换。
- (normal模式)使用s删除当前字符并进入插入模式：s；使用S（大写S）删除整行并进入插入模式。
- 使用c配合文本对象，进行快速修改：caw(删除一个单词并进入插入模式)、C(删除光标后面的内容并进入插入模式)、ct)（类似dt)，但会进入插入模式）。
- 配合数字进行使用：4s。

### 查：
- 使用/或者?进行前向或反向搜索
- 使用n/N跳转到下一个或上一个匹配
- 使用\*或者#进行当前单词的前向或后向匹配

> 假如你忘记了上面某个vim命令的用法，可以在vim下输入“:help XX”查看这个命令的帮助文档，比如“:help s” 查看s命令的帮助文档。

---

## Vim替换文本
- :% s/self/this/g  全局下将self全部替换成this
- :1,6 s/self/this/g  范围内将self替换成this
- :1,6 s/self//n  统计范围内self这个单词出现的次数

---

## Vim多文件操作
[概念]
- Buffer是指打开的一个文件的内存缓冲区
- 窗口是Buffer可视化的分割区域
- Tab可以组织窗口为一个工作区

[Buffer切换]
- 使用:ls列举当前缓冲区，使用:b n(数字)跳转到第n个缓冲区
- :bpre、:bnext、:bfirst、:blast
- 或者用:b buffer_name 加上Tab补全来跳转

[Window窗口]
- 一个缓冲区可以分割成多个窗口，每个窗口也可以打开不同的缓冲区。
- :sp或:vs，还可以使用:vs+file 或者 :sp+file的方式分屏打开文件。
- <C-w>w窗口切换、<C-w>h/j/k/l移动到窗口
- <C-w>=使所有窗口等宽等高、<C-w>\_最大化活动窗口的高度、<C-w>|最大化活动窗口的宽度、[N]<C-w>\_把活动窗口的高度设为[N]行、[N]<C-w>|把活动窗口的宽度设为[N]列

[Tab标签页](:h tabpage)
- :tabnew file_name  新建一个Tab标签页
- gt 切换标签页
- :tabe[dit] {filename} 在新标签页中打开{filename}
- <C-w>T 把当前窗口移到一个新的标签页
- :tabc[lose] 关闭当前标签页及其中的所有窗口
- :tabo[nly] 只保留活动标签页，关闭其他所有标签页

Ex命令|普通模式命令|用途
---|---|---
:tabn[ext] {N} | {N}gt | 切换到编号为{N}的标签页
:tabn[ext] | gt | 切换到下一标签页
:tabp[revious] | gT | 切换到上一标签页

---

## Vim的文本对象（Text Object）
[文本对象]：在Vim里面指，一个单词、句子或者段落，相比较于操作单个字符来修改文本，使用文本对象的方式更加高效。
- [number]<command>[text object]：number表示次数，command是命令，d(delete)、c(change)、	y(yank)，text object是要操作的文本对象，比如单词w，句子s，段落p。

![文本对象-示例](./img/text-object.png)

> [Linux终端]\<C>-减小终端字体大小；\<C-Shift>=增大终端字体大小

---

## Vim复制粘贴于寄存器的使用
- (normal模式)复制粘贴使用y(yank)和p(put)，剪贴使用d和p。
- 使用v(visual)选中要复制的地方，然后使用p粘贴
- 配合文本对象：yiw复制一个单词，yy复制一行

[寄存器的使用]
- "ay 复制到a寄存器；"ap 粘贴a寄存器的内容
- "by 复制到b寄存器；"bp 粘贴b寄存器的内容
- "+y 复制到系统剪贴板；"+p 粘贴系统剪贴板里的内容。
- :set clipboard=unnamed 将系统剪贴板的内容添加到无名寄存器，这样就可以直接复制粘贴系统剪贴板的内容。
- Vim如果设置了自动缩进，那么如果向Vim粘贴Python代码可能会引起格式错乱，这时候可以使用以下3中方式解决：
1. :set paste，i，<C-V>粘贴
2. "+p 直接粘贴系统剪贴板的内容
3. 设置:set clipboard=unnamed，然后粘贴到Vim

> :e! 重新加载，并且不保存当前文件

---

## Vim宏
- 批量添加双引号的案例
- 另一种方式：VG: normal I",wx    :normal A",wx

