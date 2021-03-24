
# 分组查询
# 学习目标：能够写出分组查询的SQL语句
# 分组查询基本的语法格式如下
# group by 列名 [having 条件表达色][with rollup];
# 说明:
# 列名：是指按照指定字段的值进行分组
# having: 条件表达式，用来过滤分组后的数据
# with rollup: 在所有记录的最后加上一条记录，显示select查询时聚合函数的统计和计算结果

# 根据gender字段来分组
# 查询性别的种类
# select distinct gender from students;
# select gender from students group by gender;

# 如果指定了分组字段，那么查询的时候只能使用指定的分组字段
# 根据name和gender字段进行分组，查看name和gender的分组信息
# select gender, name from students group by gender, name;

# group_concat: 统计每个分组指定字段的信息集合，信息之间使用逗号进行分割
# 根据gender字段进行分组，查询每个分组的姓名信息
# select gender, group_concat(name) from students group by gender;

# 统计不同性别的平均年龄
# select gender, avg(age) from students group by gender;

# 统计不同性别的人的个数
# select gender, count(*) from students group by gender;

# 根据gender字段进行分组，统计分组条数大于2的
# select gender, count(*) from students group by gender having count(*) > 2;
# 对分组数据进行过滤使用having

# 根据gender字段进行分组，汇总总人数
# select gender, count(*) from students group by gender with rollup;

# 根据gender字段进行分组,汇总所有人的年龄
# select gender, group_concat(age) from students group by gender with rollup;


