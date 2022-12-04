def sort_1(data):
    return sorted(data, key=abs, reverse=True)


def sort_2(data):
    return sorted(data, key=lambda n: -abs(n))


def test1():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = [123, 100, -100, -30, 4, -4, 1, -1, 0]
    assert res == sort_1(data)


def test2():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = [123, 100, -100, -30, 4, -4, 1, -1, 0]
    assert res == sort_2(data)
