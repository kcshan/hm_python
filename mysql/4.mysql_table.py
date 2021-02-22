# create database python_test charset=utf8;
# use python_test;

# 查看当前数据库中所有表
# show tables;

# 创建表
# create table students(
# id int unsigned primary key auto_increment not null,
# name varchar(20) not null,
# age tinyint unsigned default 0,
# height decimal(5, 2),
# gender enum("男", "女", "人妖", "保密")
# );

# 修改表 - 添加birthday字段
# alter table 表名 add 列名 类型 约束;
# 例：
# alter table students add birthday datetime;

# 修改表 - 修改字段类型
# alter table 表名 modify 列名 类型 约束;
# 例：
# alter table students modify birthday date not null;
# modify 只能修改字段类型和约束，不能修改字段名

# 修改表 - 修改字段名和字段类型
# alter table 表名 change 原名 新名 类型及约束;
# 例：
# alter table students change birthday birth datetime not null;
# 说明：
# change: 既能对字段重命名又能修改字段类型还能修改约束

# 修改表 - 删除birthday字段
# alter table 表名 drop 列名;
# 例：
# alter table students drop birthday;

# 查看表结构
# desc students;

# 查看创建表的SQL语句
# show create table 表名;
# 例：
# show create table students;

# 查看创建库的SQL语句
# show create database 数据库名;
# 例：
# show create database python_test;

# 删除表
# drop table 表;
# 例：
# drop table students;