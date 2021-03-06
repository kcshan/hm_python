# 学习目标
# 能够写出将查询结果插入到其它表中的SQL语句

# 思考
# 目前只有一个goods表，我们想要增加一个商品分类信息，比如：移动设备这个分类信息，只通过goods表无法完成商品分类的添加，那么如何实现添加商品分类信息的操作?

# 答案:
# 1. 创建一个商品分类表，把goods表中的商品分类信息添加到该表中。
# 2. 将goods表中的分类名称更改成商品分类表中对应的分类id

# 创建商品分类表
# -- 创建商品分类表
# create table good_cates(
#   id int not null primary key auto_increment,
#   name varchar(50) not null
# );

# 把goods表中的商品分类添加到商品分类表
# -- 查询goods表中商品的分类信息
# select cate_name from goods group by cate_name;

# -- 将查询结果插入到good_cates表中
# insert into good_cates(name) select cate_name from goods group by cate_name;

# -- 添加移动设备分类信息
# insert into good_cates(name) values('移动设备');
# select * from good_cates;
