## pip只下载不安装软件包
```
pip3 download -d ~/TEST request  # request是包的简写，注意不写全名
pip3 install --no-index --find-links=file:~/TEST request  # 这里也不写全名
```
或者
```
pip download -d ~/TEST request
pip install --no-index --find-links=file:./TEST request
```
