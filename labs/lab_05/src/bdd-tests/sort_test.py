from functions import my_sort1, my_sort2
from pytest_bdd import scenario, given, when, then


@scenario('f1.feature', 'Data need to be sorted by abs with function sorted')
def testing_my_sort1():
    pass


@scenario('f2.feature', 'Data need to be sorted by abs with lambda expression')
def testing_my_sort2():
    pass


@given('some data', target_fixture='data')
def data():
    return [4, -30, 100, -100, 123, 1, 0, -1, -4]


@when('data get sorted with my_sort1', target_fixture='sorted_data')
def sorted_data(data):
    return my_sort1(data)


@then('data is sorted')
def sorted_data(sorted_data):
    assert sorted_data == [123, 100, -100, -30, 4, -4, 1, -1, 0]


@when('data get sorted with my_sort2', target_fixture='sorted_data')
def sorted_data(data):
    return my_sort2(data)
