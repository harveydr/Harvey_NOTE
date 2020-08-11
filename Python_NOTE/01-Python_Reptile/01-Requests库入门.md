## requests库的安装
```bash
pip install requests
```
- 安装测试
```python
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
r.text
```
## requests库的7个主要方法

方法 | 说明
--- | ---
requests.request() | 构造一个请求，支持以下各方法的基础方法

