import socket


if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.139.2", 9090))
    send_content = "hello, 我是小白"
    # utf-8
    send_data = send_content.encode('utf-8')
    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    recv_content = recv_data.decode('utf-8')
    print("接收服务端的数据为：", recv_content)
    tcp_client_socket.close()