import threading
import time


def sing():
    print("sing:", threading.current_thread())
    for i in range(2):
        print("正在唱歌 %d" %i)
        time.sleep(0.2)


def dance():
    print("dance:", threading.current_thread())
    for i in range(2):
        print("正在跳舞 %d" %i)
        time.sleep(0.2)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()
