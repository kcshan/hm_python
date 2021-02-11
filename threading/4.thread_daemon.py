import threading
import time


def task():
    while True:
        print('任务执行中...')
        time.sleep(0.3)


if __name__ == '__main__':
    # sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print('over')