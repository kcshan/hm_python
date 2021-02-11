import multiprocessing
import time


g_list = list()


def add_data():
    for i in range(3):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)
    print("添加完成：", g_list)


def read_data():
    print('read:', g_list)


if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    add_process.join()
    print('main:', g_list)
    read_process.start()

