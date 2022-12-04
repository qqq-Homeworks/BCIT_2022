# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    ans = []
    tempans = {}
    for item in items:
        for key in args:
            if item.get(key) is not None:
                tempans[key] = item.get(key)
        ans.append(tempans.copy())
        tempans.clear()
    return ans


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    ]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))


if __name__ == "__main__":
    main()
