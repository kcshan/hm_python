# 表数据操作的SQL语句
# 1. 查询数据
# 1.1 查询所有列
# select * from 表名;
# 例：
# select * from students;

# 1.2 查询制定列
# select 列1,列2,。。。 from 表名;
# 例：
# select id,name from students;

# 2. 添加数据
# 2.1 全列插入，值的顺序与表结构字段的顺序完全一致
# insert into 表名 values(...)
# 例:
# insert into students values(0, 'xx', default, default, '男');

# 2.2 部分列插入： 值的顺序与给出的列顺序对应
# insert into 表名 (列1,...) values(值1,...);
# 例：
# insert into students(name, age) values('王小二', 15);

# 2.3 全列多行插入
# insert into 表名 values(...),(...)...
# 例：
# insert into students values(0, '张飞', 55, 1.75, '男'),(0, '关羽', 58, 1.85, '男');

# 2.4 部分列多行插入
# insert into 表名(列1,...) values(值1,...)(值1,...)...;
# 例：
# insert into students(name, height) values('刘备', 1.75),('曹操', 1.6);

# 说明：
# 主键列是自动增长，但是在全列插入时需要占位，通常使用空值（0或者undefined或者default）
# 在全列插入时，如果字段列有默认值可以使用default来占位，插入后的数据就是之前设置的默认值

# 3. 修改数据
# update 表名 set 列1=值1,列2=值2... where条件
# update students set age=18, gender='女' where id=6;

# 4. 删除数据
# delete from 表名 where 条件;
# 例：
# delete from students where id=6;

# 问题：
# 上面的操作称之为物理删除, 一旦删除就不容易恢复，我们可以使用逻辑删除的方式解决这个问题。



