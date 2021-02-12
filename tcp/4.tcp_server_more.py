import socket
import threading


def handle_client_request(new_client, ip_port):
    print("客户端的ip和端口号为：", new_client, ip_port)

    while True:
        recv_data = new_client.recv(1024)
        if recv_data:
            print("接收的数据长度为：", len(recv_data))
            recv_content = recv_data.decode("gbk")
            print("接收客户端的数据为：", recv_content, ip_port)

            send_content = "问题正在处理中。。。"
            send_data = send_content.encode('gbk')
            new_client.send(send_data)
        else:
            print("客户端下线了:", ip_port)
            break
    new_client.close()


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 9090))
    tcp_server_socket.listen(128)

    while True:
        new_client, ip_port = tcp_server_socket.accept()
        sub_thread = threading.Thread(target=handle_client_request, args=(new_client, ip_port))
        sub_thread.setDaemon(True)
        sub_thread.start()


    # tcp_server_socket.close()