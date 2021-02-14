import socket
import threading


class HttpWebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 8000))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket


    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()


    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)

        print(recv_data)

        if len(recv_data) == 0:
            new_socket.close()
            return

        recv_content = recv_data.decode('utf-8')
        print(recv_content)

        request_list = recv_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        print('request_path:', request_path)
        print('request_list:', request_list)

        if request_path == '/':
            request_path = '/index.html'

        print(request_path)

        # 判断文件存在不存在
        # os.path.exists('static' + request_path)

        try:
            with open('static' + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'Server: PWS/1.0\r\n'

            with open('static/error.html', 'rb') as file:
                file_data = file.read()

            response_body = file_data
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: PWS/1.0\r\n'
            response_body = file_data
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response)
        finally:
            new_socket.close()


def main():
    web_server = HttpWebServer()
    web_server.start()


if __name__ == '__main__':
    main()