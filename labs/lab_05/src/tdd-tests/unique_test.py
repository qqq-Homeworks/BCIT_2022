import random

import pytest as pytest


def gen_random(num_count, begin, end):
    for i in range(0, num_count, 1):
        yield (random.randint(begin, end))


class Unique(object):
    def __init__(self, items,
                 **kwargs):  # или можно def __init__(self, items, ignore_case = false, **kwargs)
        self.ignore_case = bool(kwargs.get('ignore_case'))

        self.items = list(items)
        self.used_elements = set()
        self.index = 0

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                current = self.items[self.index]
                self.index = self.index + 1
                if self.ignore_case:
                    if current.lower() not in self.used_elements:
                        self.used_elements.add(current.lower())
                        return current
                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current

    def __iter__(self):
        return self


@pytest.fixture
def data():
    d = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    return d


def test_unique_ignore_case_True(data):
    t = list(Unique(data, ignore_case=True))
    res = ['a', 'b']
    assert res == t


def test_unique_ignore_case_False(data):
    t = list(Unique(data))
    res = ['a', 'A', 'b', 'B']
    assert res == t


def test_unique_numbers():
    data = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    t = list(Unique(data))
    res = [1, 2]
    assert res == t
