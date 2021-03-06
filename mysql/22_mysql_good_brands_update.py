# 创建表并给某个字段添加数据
# 能够写出创建表并给某个字段添加数据的SQL语句

# 上一节课我们完成了商品分类表(good_cates)的创建和商品分类信息的添加以及把商品表(goods)中的商品分类名称改成了对应的商品分类id，
# 假如我们想要添加一个品牌，比如：双飞燕这个品牌信息，
# 只通过goods表无法完成品牌信息的添加，那么如何实现添加品牌信息的操作?

# 1.创建一个品牌表，把goods表中的品牌信息添加到该表中。
# 2.将goods表中的品牌名称更改成品牌表中对应的品牌id

# -- 查询品牌信息
# select brand_name from goods group by brand_name;

# -- 通过create table ...select来创建数据表并且同时插入数据
# -- 创建商品分类表，注意: 需要对brand_name 用as起别名，否则name字段就没有值
# create table good_brands (
# id int unsigned primary key auto_increment,
# name varchar(40) not null) select brand_name as name from goods group by brand_name;

# -- 将goods表中的品牌名称更改成品牌表中对应的品牌id
# update goods as g inner join good_brands gb on g.brand_name = gb.name set g.brand_name = gb.id;

# select * from good_brands;
# select * from goods;
