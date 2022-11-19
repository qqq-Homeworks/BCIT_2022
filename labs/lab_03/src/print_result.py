def print_result(func_to_print):
    def decorated_func(*args, **kwargs):
        print(func_to_print.__name__)
        res = func_to_print(*args, **kwargs)
        if type(res) == list:
            for value in res:
                print(value)
        elif type(res) == dict:
            for key, value in res.items():
                print("{0} = {1}".format(key, value))
        else:
            print(res)
        return res

    return decorated_func


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
    test_1()
    test_2()
    test_3()  # ??
    test_4()
