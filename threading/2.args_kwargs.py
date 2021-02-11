import threading
import time


def show_info(name, age):
    print("name: %s, age: %d" %(name, age))


if __name__ == '__main__':
    sub_thread_args = threading.Thread(target=show_info, args=('李四', 20))
    sub_thread_kwargs = threading.Thread(target=show_info, kwargs={"name": '李四', "age": 12})
    sub_thread_args_kwargs = threading.Thread(target=show_info, args=('李四',), kwargs={"age": 12})
    sub_thread_args.start()
    sub_thread_kwargs.start()
    sub_thread_args_kwargs.start()
