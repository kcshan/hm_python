import multiprocessing
import os
import time


def dance():
    print("dance:", os.getpid())
    print("dance:", multiprocessing.current_process())
    print("dance的父进程编号:", os.getppid())
    for i in range(3):
        print('跳舞中...')
        time.sleep(0.2)


def sing():
    print("sing:", os.getpid())
    print("sing:", multiprocessing.current_process())
    print("sing的父进程编号:", os.getppid())
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)
        os.kill(os.getpid(), 9)


dance_process = multiprocessing.Process(target=dance)
singe_process = multiprocessing.Process(target=sing)


if __name__ == '__main__':
    print("main:", os.getpid())
    print("main:", multiprocessing.current_process())
    dance_process.start()
    singe_process.start()