import multiprocessing
import time


def task():
    for i in range(5):
        print("任务执行中...")
        time.sleep(0.2)


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=task)
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(0.5)
    sub_process.terminate()
    print('over')