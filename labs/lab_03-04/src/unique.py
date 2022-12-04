# Нужно реализовать конструктор
# В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
# в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
# Например: ignore_case = True, Aбв и АБВ - разные строки
#           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
# По-умолчанию ignore_case = False

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
                if not self.ignore_case:
                    if current.lower() not in self.used_elements:
                        self.used_elements.add(current.lower())
                        return current
                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current

    def __iter__(self):
        return self
