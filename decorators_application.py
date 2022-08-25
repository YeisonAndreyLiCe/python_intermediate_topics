""" def execution_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start}')
        return result
    return wrapper """

def execution_time(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f'Execution time: {(end - start).total_seconds()} seconds')
    return wrapper

@execution_time
def random_func():
    for _ in range(10000000):
        pass

""" @execution_time
def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1) """

if __name__ == '__main__':
    random_func()
