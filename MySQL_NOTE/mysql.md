# MySQL基础
----


## Ubuntu 18.04安装phpMyAdmin
> [参考文章](https://blog.csdn.net/gongchenyu/article/details/80481583)

#### 使用apt自动安装
```
sudo apt install phpmyadmin
```

安装完成后，创建软链接到web根目录下（我的是/var/www/html/）
```
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
```

#### 手动安装
首先去[phpmyadmin官网](https://www.phpmyadmin.net/)下载最新源码，下载完后解压到web根目录下。
```
sudo unzip -d /var/www/html phpMyAdmin-5.0.0-all-languages.zip
cd /var/www/html
mv phpMyAdmin-5.0.0-all-languages phpmyadmin
```

#### 错误修复
1. 配置文件现在需要一个短语密码：
```
sudo cp -p /var/www/html/phpmyadmin/config.sample.inc.php /var/www/html/phpmyadmin/config.inc.php
sudo vi config.inc.php
```
设定config.inc.php 文件的$cfg['blowfish_secret']参数,参数字符串长度必须在32位以上。

2. $cfg[‘TempDir’] (./tmp/) 读取失败且不能建立缓存, phpMyAdmin运行速度将受影响.
```
cd /var/www/html/phpmyadmin
sudo mkdir -m 777 ./tmp
```


----

## 创建数据库
### 创建数据库并指定编码方式
```
CREATE DATABASE db_name DEFAULT CHARACTER SET utf8;
```

----
## 创建数据表
```
CREATE TABLE <表名>(
	列名 数据类型 [列级别约束条件][默认值],
	列名2 数据类型 [列级别约束条件][默认值],
	......
	[表级别约束条件]
);
```

**举例**
```
CREATE TABLE reader(
	card_id char(18),
	name varchar(10),
	sex enum('男','女'), #注意性别要用enum类型
	age tinyint,
	telephone char(11),
	balance decimal(7,3) #钱币数值要用decimal类型
);

# show tables from book; 从数据库查询表
```
----

## 查看数据表
```
SHOW TABLES [FROM db_name]; # 查看当前表则可省略db_name
DESCRIBE <表名> 或者 DESC <表名>
SHOW CREEATE TABLE tbl_name; # 查看创建表的语法结构
```
----

## 修改数据库表
### 修改表名
```
ALTER TABLE <旧表名> RENAME [TO] <新表名>;
```

### 修改列名
```
ALTER TABLE reader CHANGE emial emal_bak varchar(30);
desc reader;
```

### 修改列的数据类型
```
ALTER TABLE reader MODIFY email varchar(25);
desc reader;
```

### 修改列的排列位置
```
ALTER TABLE reader MODIFY balance decimal(7,3) AFTER email;
desc reader;
```

### 增加列
```
ALTER TABLE reader ADD email varchar(30);
desc reader;
```
### 增加列到指定位置
```
ALTER TABLE reader ADD email varchar(30) AFTER tel;
ALTER TABLE reader ADD email varchar(30) FIRST;
desc reader;
```

### 删除列
```
ALTER TABLE <表名> DROP <列名>;
```
----

## 删除数据表
> MySQL中，使用DROP TABLE可以一次删除一个或多个没有被其他表关联的数据表。
```
DROP TABLE [IF EXISTS] 表1, 表2, ... 表n;
```

**举例**
```
DROP TABLE t1,t2;
DROP TABLE IF EXISTS t3,t4;
```

---

## 表分区
> 使用表分区的前提是你的数据库必须支持。使用以下命令查看数据库是否支持表分区。
```
show plugins; # 当partition部分为ACTIVE时，表示支持表分区
```

> 表分区一般有两种方式：水平和垂直。水平分区是将表的数据按行分割成不同的数据文件，而垂直分区则是将表的数据按列分割成不同的数据文件。

### 创建表分区
```
create table bookinfo(
	book_id int,
	book_name varchar(20)
)partition by range(book_id)(
	partition p1 values less than (20109999),
	partition p2 values less than (20159999),
	partition p3 values less than MAXVALUE
);
```

> 查看表数据的时候，可以指定表分区进行查看，这样可以提高检索效率。
```
select * from bookinfo partition(p1);
```

------

## 主键约束

> 主键分为**单字段主键**和**多字段联合主键**。

#### 单字段主键
- 在定义列的同时指定主键
```
列名 数据类型 PRIMARY KEY
```

- 在列定义的后面指定主键
```
[CONSTRAINT <约束名>] PRIMARY KEY (列名); # []中的内容可以省略，这时系统会为他分配一个约束名
```

**举例**
```
create table bookinfo(
	book_id int primary key,
	book_name varchar(20) not null
);
```

或者
```
create table bookinfo(
	book_id int,
	book_name varchar(20) not null,
	constraint pk_id primary key(book_id)
);
```

#### 多字段联合主键（复合主键）
```
PRIMARY KEY(字段1, 字段2, ...字段n);
```

**举例**
```
create table borrowinfo(
	book_id int,
	card_id char(18),
	primary key(book_id, card_id)
);
```

### 通过修改表的方式为列添加主键
```
create table bookinfo(
	book_id int,
	book_name varchar(20) not null
);

alter table bookinfo modify book_id int primary key;
alter table bookinfo add primary key(book_id);
alter table bookinfo add constraint pk_id primary key(book_id);
```

### 删除主键
```
alter table bookinfo drop primary key;
```
----

## 非空约束

### 添加非空约束
- 创建表时添加非空约束

```
列名 数据类型 NOT NULL 
```

- 通过修改表的方式添加非空约束
```
ALTER TABLE bookinfo MODIFY book_name VARCHAR(20) NOT NULL;
```

### 删除非空约束
```
ALTER TABLE bookinfo MODIFY book_name VARCHAR(20);
```
----

## 唯一约束

### 添加唯一约束
```
列名 数据类型 UNIQUE
```

或者在定义完所有列之后指定唯一约束
```
[CONSTRAINT <约束名>] UNIQUE(<列名>)
```

**举例**
```
create table bookinfo(
	book_id int primary key,
	book_name varchar(20) not null,
	contraint uk_bname UNIQUE(book_name)
);
```

### 修改表时添加唯一约束
```
ALTER TABLE bookinfo MODIFY book_name varchar(20) UNIQUE;
ALTER TABLE bookinfo ADD UNIQUE(book_name);
ALTER TABLE bookinfo ADD CONSTRAINT uk_bname UNIQUE(book_name);
```

### 删除唯一约束
```
ALTER TABLE bookinfo DROP INDEX uk_bname;
ALTER TABLE bookinfo DROP KEY uk_bname;
```

> 可以通过show create table bookinfo;命令查看列的唯一约束名称

----

## 默认约束

### 创建表的时候添加默认约束
```
列名 数据类型 DEFAULT '默认值'
```

### 修改表的时候添加默认约束
```
ALTER TABLE bookinfo MODIFY press varchar(10) DEFAULT '机械工业出版社';
ALTER TABLE bookinfo ALTER COLUMN press SET DEFAULT '机械工业出版社';
```

### 删除默认约束
```
ALTER TABLE bookinfo MODIFY press varchar(20);
ALTER TABLE bookinfo ALTER COLUMN press DROP DEFAULT;
```

----

## 外键约束

- 外键用来在两个表的数据之间建立链接，它可以是一列或者多列。一个表可以有一个或多个外键。
- 外键对应的是参照完整性，一个表的外键可以为空值，若不为空值，则每一个外键值必须等于另一个表中主键的某个值。
- 外键的作用是保持数据的一致性、完整性。
- 外键列和参照列必须具有相同的数据类型。

### 创建表时创建外键约束
```
[CONSTRAINT <外键约束名>] FOREIGN KEY (列名) references <主表名> (主键)
```

**举例**
```
CREATE TABLE bookcategory(
	category_id int primary key,
	category varchar(20),
	parent_id int
);
CREATE TABLE bookinfo(
	book_id int primary key,
	book_category_id int,
	CONSTRAINT fk_cid FOREIGN KEY(book_category_id) REFERENCES bookcategory(category_id)
);
```

### 修改表时添加外键约束
```
ALTER TABLE bookinfo
ADD FOREIGN KEY(book_category_id)
REFERENCES bookcategory(category_id);
```

### 删除外键约束
```
ALTER TABLE bookinfo DROP FOREIGN KEY fk_cid;
```

> CASCADE：从父表删除或更新且自动删除或更新子表中匹配的行，从而实现级联删除或更新的操作。

```
CREATE TABLE bookinfo(
	book_id int primary key,
	book_category_id int,
	CONSTRAINT fk_cid FOREIGN KEY(book_category_id) REFERENCES bookcategory(category_id) ON DELETE CASCADE
);
```

----

## 插入数据

### 为表的所有列插入数据
```
INSERT INTO bookcategory(category_id,category,parent_id) values(1,'计算机',0);
INSERT INTO bookcategory values(2,'医学',0);
```
> 注意这两种方式中，指定插入列的方式不会受到表结构改变的影响，而第二种方式中，如果我们改变了表的结构，那这种插入方式的values顺序也必须要改变。

### 为表的部分列插入数据
```
INSERT INTO readerinfo(card_id,name,tel) values('210210199504031476','Harvey','17718715678');
```

### 同时插入多条记录
```
INSERT INTO table_name(column_list) values(values_list1),(values_list2)...,(values_listn);
```

**举例**
```
insert into bookcategory (category_id,category_id,parent_id) values(3,'编程语言',1),(4,'数据库',1),(5,'儿科学',2);
```

### 将查询结果插入到表中
```
INSERT INTO table_name1(column_list1) SELECT(column_list2) FROM table_name2 WHERE (condition);
```

**举例**
```
insert into bookcategory select * from test_tb where id>5;
```

----

## 设置自动编号
```
列名 数据类型 AUTO_INCREMENT
```

> 注：AUTO_INCREMENT约束的字段可以是任何整数类型(tinyint,smallint,int等)。

- 设置自动增长值
```
create table bookcategory_tmp(
	category_id int primary key AUTO_INCREMENT,
	category varchar(20) not null unique,
	parent_id int not null
)AUTO_INCREMENT=5;

insert into bookcategory_tmp(category,parent_id)values('医学',0);
```

### 为已有的表添加自增列
```
ALTER TABLE bookcategory modify category_id int AUTO_INCREMENT;
```

### 修改自增列的起始值
```
# 修改AUTO_INCREMENT列起始值从x开始
ALTER TABLE bookcategory AUTO_INCREMENT = x;
```

### 去掉自增列
```
ALTER TABLE bookcategory modify category_id int;
```

---

## 单表数据记录的更新

- 更新特定的行
- 更新所有的行

语法格式
```
UPDATE table_name SET
column_name1 = value1,
column_name2 = value2,
...
column_namen = valuen
WHERE (condition);
```
> 如果没有WHERE条件，则更新所有的行。

**举例**
```
UPDATE readerinfo set balance = balance - 79.80\*0.05 WHERE card_id = '210210199901011111';
UPDATE bookinfo set store = store - a WHERE book_id = 20150201;
```

## 单表数据记录的删除
```
DELETE FROM table_name [WHERE <condition>];
```
> 如果不加WHERE条件，则删除所有数据。

**举例**
```
delete from readerinfo where card_id = '210210199901011111';
delete from readerinfo;
```

- 如果向删除表中所有记录，还可以使用TRUNCATE TABLE语句，将直接删除原来的表，并重新创建一个表，语法结构为：
```
TRUNCATE TABLE table_name # 这种删除方式更快
```

**举例**
```
truncate table readerinfo;
```

## 查找MySQL默认密码-修改登录密码
> 参考文档：https://blog.csdn.net/wto882dim/article/details/93334933

## 创建数据库
```
CREATE {DATABASE|SCHEMA} [IF NOT EXISTS] 数据库名
[
    [DEFAULT] CHARACTER SET [=]  字符集   |    [DEFAULT] COLLATE [=] 校对规则名称
];

```
> 在语法中，花括号“{}”表示必选项；中括号“[]”表示可选项；竖线“|”表示分隔符两侧的内容为“或”的关系。

## 创建指定字符集的数据库
```
CREATE DATABASE db_test
CHARACTER SET = GBK;
```

## 创建数据库前判断是否存在同名数据库
```
CREATE DATABASE IF NOT EXISTS db_test1;
```

## 查看数据库
```
SHOW {DATABASES|SCHEMAS} [LIKE '模式' WHERE 条件];
```
## 筛选以db_开头的数据库名称
```
SHOW DATABASES LIKE 'db_%';
```
## 选择数据库
```
USE 数据库名;
```
## 修改数据库
```
ALTER {DATABASE | SCHEMA} [数据库名]
 [DEFAULT] CHARACTER SET [=] 字符集
| [DEFAULT] COLLATER [=] 校对规则名称
```

