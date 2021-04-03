# 连接查询－右连接
# 能够写出右连接查询的SQL语句

# 右连接查询
# 以右表为主根据条件查询左表数据，如果根据条件查询右表数据不存在使用null值填充

# 右连接查询语法格式
# select 字段 from 表1 right join 表2 on 表1.字段1 = 表2.字段2;

# right join 就是右连接查询关键字
# on　就是连接查询条件
# 表1是左表
# 表2是右表

# 使用右连接查询学生表与班级表
# select * from students s right join classes c on s.c_id = c.id;

