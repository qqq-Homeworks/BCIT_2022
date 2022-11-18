def print_result(func_to_print):
    def decorated_func():
        print(func_to_print.__name__)
        if type(func_to_print()) == type([]):
            for value in func_to_print():
                print(value)
        elif type(func_to_print()) == type({}):
            for key, value in func_to_print().items():
                print("{0} = {1}".format(key, value))
        else:
            print(func_to_print())

    return decorated_func()


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1
    test_2
    test_3#??
    test_4()
