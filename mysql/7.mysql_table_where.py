# where条件查询
# 学习目标
#　能够写出模糊查询的SQL语句

# where条件查询可以对表中的数据进行筛选，条件成立的记录会出现在结果里．
# where语句支持的运算符
# 比较运算符
# 逻辑运算符
# 模糊查询
# 范围查询
# 空判断

# where条件查询语法格式如下
# select * from 表名 where 条件;
# 例：
# select * from students where id = 1;

# 比较运算符查询
# 等于: =
# 大于: >
# 大于等于: >=
# 小于: <
# 小于等于: <=
# 不等于: !=　或 <>

# 查询编号大于３的学生
# select * from students where id > 3;

# 查询编号不大于４的学生
# select * from students where id <= 4;

# 查询姓名不是＂黄蓉＂的学生
# select * from students where name != '黄蓉';
# select * from students where name <> '黄蓉';

# 查询没被删除的学生
# select * from students where is_del = 0;

# 逻辑运算符查询
# and
# or
# not

# 查询编号大于３的女同学
# select * from students where id > 3 and gender = 0;

# 查询编号小于４或没被删除的学生
# select * from students where id < 4 and is_del = 0;

# 查询年龄不在１０岁到１５岁之间的学生
# select * from students where not (age >= 10 and age <= 15);

# 模糊查询
# like是模糊查询关键字
# %表示任意多个任意字符
# _表示一个任意字符

# 查询姓黄的学生
# select * from students where name like '黄%';

# 查询姓黄并且＂名＂是一个字的学生
# select * from students where name like '黄_';

# 查询姓黄并且＂名＂是俩个字的学生
# select * from students where name like '黄__';

# 查询姓黄或叫婧的学生
# select * from students where name like '黄%' or name like '%靖';

# 范围查询
# between .. and .. 表示在一个连续的范围内的查询
# in 表示在一个非连续的范围内查询

# 查询编号为３至８的学生
#　select * from students where id between 3 and 8;

# 查询编号不是３至８的男生
# select * from students where not (id between 3 and 8) and gender='男';

# 查询编号是3 5 7的学生
# select * from students where id in (3, 5, 7);

# 查询编号不是3 5 7的学生
# select * from students where id not in (3, 5, 7);

# 空判断查询
# 判断为空使用: is null
# 判断非空使用: is not null

# 查询没有填写身高的学生
# select * from students where height is null;

# 查询身高不是填写为空的学生
# select * from students where height is not null;

# 查询未删除男生信息, 按学号降序
#

# 显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时，按照身高从高-->矮排序
#

# 查询前３行男生信息


