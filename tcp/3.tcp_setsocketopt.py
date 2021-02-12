import socket


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9090))
    tcp_server_socket.listen(128)
    new_client, ip_port = tcp_server_socket.accept()
    print("客户端的ip和端口号为：", new_client, ip_port)
    recv_data = new_client.recv(1024)
    print("接收的数据长度为：", len(recv_data))
    recv_content = recv_data.decode("gbk")
    print("接收客户端的数据为：", recv_content)

    send_content = "问题正在处理中。。。"
    send_data = send_content.encode('gbk')
    new_client.send(send_data)
    new_client.close()

    tcp_server_socket.close()