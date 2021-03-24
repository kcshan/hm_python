# 连接查询－左连接
# 能够写出左连接查询的SQL语句

# 左连接查询
# 以左表为主根据条件查询右表数据，如果根据条件查询右表数据不存在使用null值填充

# 左连接查询语法格式
# select 字段 from 表1 left join 表2 on 表1.字段1 = 表2.字段2;

# left join 就是左连接查询关键字
# on　就是连接查询条件
# 表1是左表
# 表2是右表

# 使用左连接查询学生表与班级表
# select * from students as s left join classes as c on s.c_id = c.id;
