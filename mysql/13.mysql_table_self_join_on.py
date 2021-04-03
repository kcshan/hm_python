# 使用自连接查询省份和城市信息
# 创建areas表
# create table areas(
#   id varchar(30) not null primary key,
#   title varchar(30),
#   pid varchar(38)
# );
# create table area_data (
#     id varchar(30) not null primary key,
#     pid varchar(38),
#     title varchar(180)
# );
# source /home/python/Desktop/study/hm_python/mysql/area_data.sql
# select c.id, c.title, c.pid, p.title from area_data as c inner join area_data as p on c.pid = p.id where p.title = '山东';

