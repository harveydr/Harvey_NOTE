## 卸载Python2，将python指向python3
```
update-alternatives --install /usr/bin/python python /usr/bin/python3.6.9
```
> 参考文档：https://blog.csdn.net/qq_43184146/article/details/97819393

## 多个Python版本切换python命令指向
```
# root用户下输入，建立python可选项

update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2

update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

# 切换python版本

sudo update-alternatives --config python
# 选择python指向版本，并回车
```
> 参考文档：https://blog.csdn.net/qq_43184146/article/details/97819393
