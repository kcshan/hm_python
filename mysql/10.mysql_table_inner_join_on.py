# 连接查询－内连接
# 能够写出内连接查询的SQL语句

# 连接查询可以实现多个表的查询，当查询的字段数据来自不同的表就可以使用连接查询来完成
# 内连接查询
# 左连接查询
# 右连接查询
# 自连接查询

# 内连接查询
# 查询俩个表中符合条件的共有记录

# 内连接查询语法格式
# select 字段 from 表1 inner join 表2 on 表1.字段1 = 表2.字段2

# inner join 就是内连接查询关键字
# on 就是连接查询条件

# 使用内连接查询学生表与班级表
# 创建表
# create table classes(id int unsigned not null primary key auto_increment,name varchar(20) not null);
# desc classes;
# 插入数据
# insert into classes(name) values('py40'),('py41');
# 修改students表，添加c_id字段
# alter table students add c_id int unsigned;
# update students set c_id = 2 where id in (1,3,5);
# update students set c_id = 1 where id in (2,4,6);
# select * from students as s inner join classes as c on s.c_id = c.id;
# select s.name, c.name from students as s inner join classes as c on s.c_id = c.id;

# 内连接使用inner join .. on .., on表示俩个表的连接查询条件
# 内连接根据连接查询条件取出俩个表的＂交集＂