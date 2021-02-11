import threading
import time


def show_info():
    time.sleep(1)
    print(threading.current_thread())


if __name__ == '__main__':
    for i in range(20):
        sub_thread = threading.Thread(target=show_info)
        sub_thread.start()