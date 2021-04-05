#　外键约束
# 能够写出删除外键约束的SQL语句

# 外键约束作用
# 外键约束：　对外键字段的值进行更新和插入时会和引用表中字段的数据进行验证，数据如果不合法则更新
# 和插入会失败，保证数据的有效性

# 对于已经存在的字段添加外键约束
# 为cls_id字段添加外键约束
# show create table students;
# select * from students;
# select * from classes;
# insert into students(name, age, c_id) values('刘芳', 20, 7);
# alter table students add foreign key(cls_id) references classes(id);
# delete from students where name = '刘芳';
# alter table students add foreign key(cls_id) references classes(id);

# 在创建数据表时设置外键约束
# 创建学校表
# create table school(
#   id int not null primary key auto_increment,
#   name varchar(10)
# );

# 创建老师表
# create table teacher(
#   id int not null primary key auto_increment,
#   name varchar(10)
# );

