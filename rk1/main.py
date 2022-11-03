from operator import itemgetter


class Programming_language:
    """Сотрудник"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Development_tool:
    """Отдел"""

    def __init__(self, id, name, users_count, programming_language_id):
        self.id = id
        self.name = name
        self.users_count = users_count
        self.programming_language_id = programming_language_id


class Programming_languageDevelopment_tool:
    """
    'Сотрудники отдела' для реализации
    связи многие-ко-многим
    """

    def __init__(self, Programming_language_id, Development_tool_id):
        self.Development_tool_id = Development_tool_id
        self.Programming_language_id = Programming_language_id


# Отделы
Development_tools = [
    Development_tool(1, 'CLion', 75000, 1),
    Development_tool(2, 'gdb', 100000, 1),

    Development_tool(3, 'Visual Studio', 85000, 2),
    Development_tool(4, '.NET core', 50000, 2),
    Development_tool(5, 'ASP.NET', 45000, 2),
    Development_tool(6, 'Entity Framework', 35000, 2),

    Development_tool(7, 'Angular', 100000, 3),
    Development_tool(8, 'React', 120000, 3),
    Development_tool(9, 'NodeJS', 150000, 3),
    Development_tool(10, 'WebStorm', 75000, 3),

    Development_tool(11, 'PyCharm', 87500, 4),
    Development_tool(12, 'Django', 50000, 4),
    Development_tool(13, 'Tensor Flow', 35000, 4),

    Development_tool(14, 'Visual Studio Code', 187000, 1),

    Development_tool(15, 'A+ PROGRAMMING IDE', 10, 5),
]

# Сотрудники
Programming_languages = [
    Programming_language(1, 'C++', ),
    Programming_language(2, 'C#', ),
    Programming_language(3, 'JavaScript', ),
    Programming_language(4, 'Python', ),
    Programming_language(5, 'A+', ),

]

Programming_languages_Development_tools = [
    Programming_languageDevelopment_tool(1, 1),
    Programming_languageDevelopment_tool(1, 2),
    Programming_languageDevelopment_tool(1, 14),

    Programming_languageDevelopment_tool(2, 3),
    Programming_languageDevelopment_tool(2, 4),
    Programming_languageDevelopment_tool(2, 5),
    Programming_languageDevelopment_tool(2, 6),
    Programming_languageDevelopment_tool(2, 14),

    Programming_languageDevelopment_tool(3, 7),
    Programming_languageDevelopment_tool(3, 8),
    Programming_languageDevelopment_tool(3, 9),
    Programming_languageDevelopment_tool(3, 10),
    Programming_languageDevelopment_tool(3, 14),

    Programming_languageDevelopment_tool(4, 11),
    Programming_languageDevelopment_tool(4, 12),
    Programming_languageDevelopment_tool(4, 13),
    Programming_languageDevelopment_tool(4, 14),

    Programming_languageDevelopment_tool(5, 14),
    Programming_languageDevelopment_tool(5, 15),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(d.name, e.name, e.users_count)
                   for d in Programming_languages
                   for e in Development_tools
                   if e.programming_language_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, pl.Programming_language_id, pl.Development_tool_id)
                         for d in Programming_languages
                         for pl in Programming_languages_Development_tools
                         if d.id == pl.Programming_language_id]

    many_to_many = [(programming_language_name, e.name)
                    for programming_language_name, Programming_language_id, Development_tool_id in many_to_many_temp
                    for e in Development_tools if e.id == Development_tool_id]

    print('Задание В1')
    res_11 = list(filter(lambda i: (i[0][0] == 'A' or i[0][0] == 'a'), one_to_many))
    print(res_11)

    print('\nЗадание В2')
    res_2 = []
    for pl in Programming_languages:
        d_tmp = list((pl.name, d.users_count) for d in Development_tools if d.programming_language_id == pl.id)
        if len(d_tmp) > 0:
            res_2.append(min(d_tmp, key=lambda i: i[1]))
    tmp = sorted(res_2, key=itemgetter(1))
    print(tmp)

    print('\nЗадание В3')
    res_13 = {}
    # Перебираем все отделы
    many_to_many.sort(key=lambda i: i[1])
    print(many_to_many)


if __name__ == '__main__':
    main()
