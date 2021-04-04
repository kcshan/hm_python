# 远程连接mysql
# 报错：navicat远程连接mysql，2003 can't connect to mysql server on 10038

# netstat -an|grep 3306
# 来查看mysql默认的端口3306是否开启，允许哪个ip使用，如果你发现，前面有127.0.0.1，就说明，3306端口只能本机ip使用

# 打开mysql配置文件vi /etc/mysql/mysql.conf.d/mysqld.cnf
# 将bind-address = 127.0.0.1注销​

# use mysql;
# select * from user\G;
# update user set host = '%' where user = 'root';
# sudo service mysql restart;

# 进行授权
# 如果想root用户使用password从任何主机连接到mysql服务器的话。
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;