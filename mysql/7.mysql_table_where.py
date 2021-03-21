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

# 排序查询语法
# select * from 表名 order by 列1 asc|desc [,列2 asc|desc, ...];

# 语法说明
# 先按照列１进行排序，如果列１的值相同时，则按照列２排序，以此类推
# asc从小到大排列，即升序
# desc从大到小排列，即降序
#　默认按照列值从小到大排列（即asc关键字）

# 查询未删除男生信息, 按学号降序
# select * from students where gender=1 and is_del=0 order by id desc;

# 显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时，按照身高从高-->矮排序
# select * from students order by age desc, height desc;

# 分页查询
# 能够使用limit关键字实现分页查询

# 分页查询的语法
# select * from 表名 limit start, count;

# 说明
# limit是分页查询关键字
# start表示开始行索引,默认是0
# count表示查询条数

# 查询前３行男生信息
# select * from students where gender=1 limit 0,3;
# 简写
# select * from students where gender=1 limit 3;

# 查询学生表，获取第n页数据的SQL语句
# select * from students limit (n-1) * m,m;

# 聚合函数
# 能够写出查询总行数的ＳＱＬ语句
# 聚合函数又叫组函数，通常是对表中的数据进行统计和计算，一般结合分组(group by)来使用，用于统计和计算分组数据
# 常用的聚合函数:
# count(col): 表示求指定列的总行数
# max(col): 表示求指定列的最大值
# min(col): 表示求指定列的最小值
# sum(col): 表示求指定列的和
# avg(col): 表示求指定列的平均值

# 清屏
# system clear

# 查询学生的个数
# select count(height) from students;
# 聚合函数不对空值进行统计
# select count(*) from students;

# 查询女生的编号最大值
# select max(id) from students where gender = '女';

# 查询未删除的学生最小编号
# select min(id) from students where id_del = 0;

# 查询男生的总身高
# select sum(height) from students where gender='男';

# 平均身高
# select avg(height) from students where gender='男';

# 求男生的平均身高
# select sum(height) / count(*) from students where gender='男';
# select avg(height) from students where gender='男';

# 查询性别的种类
#

# 根据name和gender字段进行分组，查看name和gender的分组信息
#

# 根据gender字段进行分组，查询每个分组的姓名信息
#

# 统计不同性别的平均年龄

