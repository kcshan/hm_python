# 求男生的平均身高
# select sum(height) / count(*) from students where gender='男';
# select avg(height) from students where gender='男';

# 求平均值
# 求男生的平均身高，聚合函数不统计null值, 平均身高有误
# select avg(height) from students where gender=1;
# 求男生的平均身高，包含身高是null的
# select avg(ifnull(height, 0)) from students where gender=1;
# 注意点：聚合函数不会对空值进行统计
# ifnull函数判断指定的字段是否是空值，如果是空值使用默认值0
