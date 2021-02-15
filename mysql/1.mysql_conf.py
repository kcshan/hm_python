
# 安装mysql-server mysql服务端
# sudo apt-get install mysql-server

# mysql-server在ubuntu下的启动、停止、重启、查看状态
# 查看状态
# sudo service mysql status

# 停止
# sudo service mysql stop

# 启动
# sudo service mysql start

# 重启
# sudo service mysql restart

# ubuntu下mysql的配置文件地址
# /etc/mysql/mysql.conf.d/mysqld.conf

# 主要配置说明
# port表示端口号，默认为3306
#
# bind-address表示服务器绑定的ip，默认为127.0.0.1
#
# datadir表示数据库保存路径，默认为/var/lib/mysql
#
# log_error表示错误日志，默认为/var/log/mysql/error.log

# 解压navicat112_mysql_cs_x64_tar.gz
# tar zxvf navicat112_mysql_cs_x64.tar.gz
# ./start_navicat

# 打开安装程序之后，点击俩次取消，再点击试用
# 试用期过去之后再次试用的方法
# cd ~
# rm -r .navicat64

# 命令行客户端的安装
# sudo apt-get install mysql-client

