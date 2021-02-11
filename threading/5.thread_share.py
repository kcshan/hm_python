import threading
import time


g_list = []


def add_data():
    for i in range(3):
        time.sleep(0.3)
        g_list.append(i)
        print("add: ", i)
    print('添加数据完成:', g_list)


def read_data():
    print(g_list)


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()
    read_thread.start()