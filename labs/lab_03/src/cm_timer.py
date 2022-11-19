import datetime
from time import sleep
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        pass

    def __enter__(self):
        self.time_start = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: {}'.format(datetime.datetime.now() - self.time_start))


@contextmanager
def cm_timer_2():
    time_start = datetime.datetime.now()
    yield
    print('time: {}'.format(datetime.datetime.now() - time_start))


#
with cm_timer_1():
    sleep(1.5)

with cm_timer_2():
    sleep(1.5)
