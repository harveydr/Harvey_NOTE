# JavaScript基础

# 变量命名

## 命名规则

JS中的变量是弱类型可以保存所有类型的数据，即变量没有类型而值有类型。变量名以字母、$、_ 开始，后跟字母、数字、_。

JS语言关键字不能用来做变量名，比如 `true、if、while、class` 等。

## 变量声明

- 使用var声明
- 使用let声明

可以同时声明多个变量，变量也可以更换不同类型的数据。

```javascript
let hd = 'houdunren';
console.log(typeof hd);

hd = 18;
console.log(typeof hd);
```

## 变量提升

```javascript
console.log(a); //undefined.这里应该报错的，可是却是undefined——变量提升
var a = 1;
console.log(a);  //1
```

解析器会先解析代码，然后把声明的变量的声明提升到最前，这就叫做变量提升。

## TDZ

使用`let/const` 声明的变量在声明前存在临时性死区（TDZ）使用会发生错误。

```
console.log(x); // Cannot access 'x' before initialization
let x = 1;
```

函数中的TDZ情景：

```javascript
let web = "houdunren.com";
function func() {
	console.log(web);
    // 如果在函数内部再声明一个web，则console.log会报错，(TDZ)。
	// let web = "hdcms.com"; 
}
func();
```



# 块作用域

