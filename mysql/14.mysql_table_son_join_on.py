# 子查询
# 学习目标：能够写出子查询的SQL语句

# 子查询介绍
# 在一个select语句中,嵌入了另外一个select语句，那么被嵌入的select语句称之为子查询语句，外部那个select语句则称为主查询

# 主查询和子查询的关系
# 子查询是嵌入到主查询中
# 子查询是辅助主查询的,要么充当条件，要么充当数据源
# 子查询是可以独立存在的语句，是一条完整的select语句

# 查询大于平均年龄的学生
#　select * from students where age > (select avg(age) from students);

# 查询学生在班的所有班级名字
# select c_id from students where c_id is not null;
# select * from classes where id in (select c_id from students where c_id is not null);

# 查找年龄最大，身高最高的学生
# select max(age) from students;
# select max(height) from students;
# select * from students where age = (select max(age) from students);
# select * from students where height = (select max(height) from students);
# select * from students where age = (select max(age) from students) and height = (select max(height) from students);
# select * from students where (age, height) = (select max(age), max(height) from students);
# 子查询是一个完整的查询语句，子查询的执行顺序，先执行子查询然后主查询根据子查询的结果再执行

# 为学生版的cls_id字段添加外键约束
#

# 创建学校表
#

# 创建老师表添加学校外键
#
