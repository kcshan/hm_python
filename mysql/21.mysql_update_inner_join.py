# 使用连接更新表中某个字段数据
# 能够知道使用连接更新表中某个字段数据的SQL语句

# 更新goods表中的商品分类信息
# 上一节课我们已经创建了一个商品分类表(good_cates)，并完成了商品分类信息的插入
# 现在需要更新goods表中的商品分类信息，把商品分类名称改成商量分类id。

#　-- 查看goods表中的商品分类名称对应的商品分类id
# select * from goods inner join good_cates on goods.cate_name = good_cates.name;

# 把该语句中from 后的语句理解为一张虚表
# update goods g inner join good_cates gc on g.cate_name=gc.name set g.cate_name=gc.id;
# select cate_name from goods;