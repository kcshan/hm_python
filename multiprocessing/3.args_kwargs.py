import multiprocessing


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    sub_process_args = multiprocessing.Process(target=show_info, args=('李四', 20))
    sub_process_kwargs = multiprocessing.Process(target=show_info, kwargs={"name": '李四', "age": 12})
    sub_process_args_kwargs = multiprocessing.Process(target=show_info, args=('李四',), kwargs={"age": 12})
    sub_process_args.start()
    sub_process_kwargs.start()
    sub_process_args_kwargs.start()