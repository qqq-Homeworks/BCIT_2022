import json
import sys

from labs.lab_03.src.cm_timer import cm_timer_1
from labs.lab_03.src.gen_random import gen_random
from labs.lab_03.src.unique import Unique
from labs.lab_03.src.print_result import print_result

path = '/Users/qqq/Documents/University/2course/3term/BCIT/BCIT_2022/notebooks/fp/files/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(Unique([record['job-name'] for record in arg]))


@print_result
def f2(arg):
    return list(filter(lambda s: s.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
