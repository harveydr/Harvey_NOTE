## 求最小公倍数

```python
while True:
	try:
		a,b = map(int, input().split())
		i,j = a,b
		m = a%b
		while m!=0:
			a,b = b,m
			m = a%b
		print(int(i*j/b))
	except:
		break
```

## 字符逆序

```python
char = input()
print(char[::-1])
```

## 求解立方根

```python
import math
while True:
	try:
		num = float(input())
		num2 = math.pow(num, 1.0/3)
		print('%.1f' % num2)
	except:
		break
```

## 记负均正II

```python
count = 0
temp = []
while True:
    try:
        n = int(input())
        if n < 0:
            count += 1
        else:
            temp.append(n)
    except:
        break
if len(temp)>0:
    average = sum(temp)/len(temp)
else :
    average = 0.0
print(count)
print('%0.1f'% average)
```

## 字符串分割

```python
while True:
    try:
        a=int(input())
        for i in range(a):
            s=input()
            while len(s)>8:
                print(s[0:8])
                s=s[8:]
            print(s.ljust(8,'0'))
    except:
        break
```

## Redraiment的走法

```python
import bisect 
while True:
    try:
        a,b = int(input()), map(int, raw_input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break
```

## 字符统计

```python
while True:
    try:
        a=input()
        s=set(a)
        d={}
        r=''
        for i in s:
            if a.count(i) not in d:
                d[a.count(i)]=[]
            d[a.count(i)] +=[i]
        t=sorted(d,reverse=True)
        for i in t:
            r+=''.join(sorted(d[i],key=ord,reverse=False))
        print(r)
    except:
        break
```

## 输入整型数组和排序标识，对其元素按照升序或降序进行排序

```python
while True:
    try:
        num = int(input())
        data = list(map(int, input().split()))
        flag = input()
        flag_dict = {"0": False, "1": True}

        data_=sorted(data, reverse=flag_dict[flag])
        print(" ".join(map(str,data_)))
    except:
        break
```

	## 等差数列

```python
while True:
	try:
		n = int(input())
		sn = n*2 + n*(n-1)*3/2
		print(int(sn))
	except:
		break
```

## 自守数

```python
while True:
	try:
		N = int(input())
		num = 0
		for i in range(N):
			if str(i*i).endswith(str(i)):
				num +=1
		print(num)
	except:
		break
```

## 记负均正

```python
while True:
	try:
		n = int(input())
		nums = list(map(int, input().split()))
		count = 0
		count_1 = 0
		sumNums = 0
		for i in nums:
			if i>0:
				sumNums += i
				count_1 += 1
			if i<0:
				count += 1
		print(count, round(sumNums/count_1, 1))
	except:
		break
```

## 表示数字

```python
while True:
    try:
        b = []
        s1 = input()
        for i in s1:
            if i.isdigit():
                i = '*'+i+'*'
                b.append(i)
            else:
                b.append(i)
        print(''.join(b).replace('**',''))
    except:
        break
```

----

> 入门

## 取近似值

```python
a = float(input())
if(a*10)%10>=5:
    print(int(a)+1)
else:
    print(int(a))
```

## 求int型正整数在内存中存储为1的个数

```python
a = int(input())
b = str(bin(a))
c = 0
for i in b:
    if i=='1':
        c+=1
print(c)
```

> 简单

## 数字颠倒

```python
a = int(input())
b = str(a)
print(b[::-1])
```

## 字符串反转

```python
a = input()
print(a[::-1])
```

## 四则运算

```python
a = input()
print(eval(a))
```

## 表达式求值

```python
a = input()
print(eval(a))
```

## 整数二进制中1的个数

```python
while True:
    try:
        a = int(input())
        print(bin(a).count('1'))
    except:
        break
```

 ## 计算日期到天数转换

```python
while True:
    try:
        year, month, day = map(int, input().strip().split())
        day_of_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
         
        day_num = 0
        for i in range(month-1):
            day_num += day_of_each_month[i]
        day_num =day_num + day
        # 不是整百年，能被4整除的是闰年，整百年，能被400整除是闰年
        if (year % 100 == 0 and year % 400 == 0) or year % 4 == 0:
            day_num += 1
        print(day_num)
    except:
        break
```

## 参数解析

```python
while True:
    try:
        a = input().split()
        print(len(a))
        for i in a:
            if '"' in i: print(i.strip('"'))
            else: print(i)
    except:
        break
```

## 公共字串计算

```python
while True:
    try:
        a = input().upper()
        b = input().upper()
        n = 0
        for i in range(len(a)):
            if a[i-n: i+1] in b:
                n += 1
        print(n)
    except:
        break
```

## 大写字母的个数

```python
while True:
    try:
        str = input()
        count = 0
        for i in str:
            if i.isupper():
                count +=1
        print(count)
    except:
        break
```

## 杨惠三角中的偶数位置

```python
dic = {
    0: 3,
    1: 2,
    2: 4,
    3: 2
}
while True:
    try:
        n = int(input())
        if n <= 2:
            print(-1)
        else:
            print(dic[n%4])
    except:
        break
```

## 

