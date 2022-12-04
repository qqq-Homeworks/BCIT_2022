import pytest as pytest


def field(items, *args):
    result = {}
    assert len(args) > 0
    for d in items:
        for i,j in d.items():
            if i in args:
                result[i] = j
        if len(result) == 1:
            s = result.popitem()
            s = "'" + str(s[1]) + "'"
            yield s
        else :
            yield result

@pytest.fixture
def goods():
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
    return goods


def test_field_one_arg(goods):
    t = list(field(goods, 'title'))
    res = ["'Ковер'", "'Диван для отдыха'"]
    assert res == t


def test_field_two_arg(goods):
    t = field(goods, 'price', 'title')
    assert next(t) == {'title': 'Ковер', 'price': 2000} and next(t) == {'title': 'Диван для отдыха', 'price': 5300}
