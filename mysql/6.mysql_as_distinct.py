# as && distinct
# 学习目标： 能够知道去除重复数据行的关键字

# as关键字
# 在使用SQL语句显示结果的时候，往往在屏幕显示的字段名并不具备良好的可读性，此时可以使用as给字段起一个别名。

# 使用as给字段起别名
# select id as 序号, name as 名字, gender as 性别 from students;
# select name as 姓名, age as 年龄 from students;

# 可以通过as给表起别名
# -- 如果是表单查询，可以省略表名
# select id, name, gender from students;
# select name as n, age as a from students as s;

# -- 表名, 字段名
# select students.id, students.name, students.gender from students;

# -- 可以通过 as 给表起别名
# select s.id, s.name, s.gender from students as s;

# 说明：
# 在这里给表起别名看起来并没有什么意义，然而并不是这样的，我们在后期学习自连接的时候，必须要对表起别名。

# distinct关键字
# select distinct gender from students;
# select distinct age, gender from students;

