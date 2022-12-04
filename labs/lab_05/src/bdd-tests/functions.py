def my_sort1(data):
    return sorted(data, key=abs, reverse=True)


def my_sort2(data):
    return sorted(data, key=lambda n: -abs(n))


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
