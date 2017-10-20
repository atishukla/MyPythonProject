import collections
import time
import os
from pprint import pprint
import multiprocessing

# Create a named tuple
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])


scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu yoyu', field='chemistry', born=1930, nobel=True),
    Scientist(name='Vera Radim', field='astronomy', born=1928, nobel=False),
    Scientist(name='Xin Pang', field='arts', born=1884, nobel=True),
    Scientist(name='Han Roberts', field='biology', born=1752, nobel=False)
)


def outer(func):
    def inner(x):
        print(f'Processing record {x.name}')
        time.sleep(1)
        result = func(x)
        print(f'Done Processing of record for {x.name}\n')
        return result
    return inner


def time_calculator(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f'\nTime to completion {end-start:.2f}\n')
        return result
    return inner


def _transform(x):
    print(f'Process {os.getpid()} working on processing record {x.name}')
    time.sleep(1)
    result = {'name': x.name, 'age': 2017 - x.born}
    print(f'Process {os.getpid()} Done Processing of record for {x.name}')
    return result


@time_calculator
def no_parallel():
    # start = time.time()
    result = tuple(map(_transform, scientists))
    # end = time.time()
    # print(f'\nTime to completion {end-start:.2f}\n')
    pprint(result)


def parallel():
    pool = multiprocessing.Pool(processes=len(scientists))
    result = pool.map(_transform, scientists)
    pprint(result)


if __name__ == '__main__':
    parallel()
