# Python列表

## sort函数与sorted函数的区别与使用

我们对List进行排序，Python提供了两个方法：
- 用List的成员函数sort进行排序；
- 用内建函数sorted进行排序（从python 2.4开始）

**sort函数定义**：sort(cmp=None, key=None, reverse=False)  
**sorted函数定义**：sorted(iterable, cmp=None, key=None, reverse=False)

**参数解析**  

iterable：是可迭代类型;  
cmp：用于比较的函数（大于时返回1，小于时返回-1，等于时返回0），比较什么由key决定,有默认值，迭代集合中的一项;  
key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;  
reverse：排序规则. reverse = True 或者 reverse = False，有默认值。  

> 注：sort( )函数与sorted( )函数最大的区别是， sort()函数是对已存在的列表进行操作，调用没有返回值；而sorted()函数是返回一个新的list,不在原来的list上进行操作，调用返回一个排好序的list。

示例：
```bash
a = [2,1,3,7,4,9]
a.sort()

b = [2,1,3,7,4,9]
c = sorted(b)

print(a)
print(b)
print(c)
```

