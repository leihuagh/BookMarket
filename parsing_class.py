import os


class Parser:
    def __init__(self, file_name, delim):
        self.file_name = file_name
        self.delim = delim

    def parsing(self):
        result = {}
        file_name = self.file_name
        try:
            route = os.path.abspath(self.file_name)
            with open(route, 'r') as my_file:
                for line in my_file:
                    new_str = line.strip('\n')
                    split = new_str.split(self.delim)
                    new_lst = split
                    result[new_lst[0]] = new_lst[1:len(new_lst)]
                return print(result)
        except FileNotFoundError:
            print('Файла {}'.format(file_name) + ' не существует')

    def __repr__(self):
        return 'Pars("{}", "{}")'.format(self.file_name, self.delim)

    def __str__(self):
        return 'Парсим файл "{}" с разделителем "{}"'.format(self.file_name, self.delim)

    def abspath(self):
        route = os.path.abspath(self.file_name)
        return route

    @property
    def file_len(self):
        route = os.path.abspath(self.file_name)
        with open(route, 'r') as my_file:
            len_chars = sum(len(word) for word in my_file)
            return len_chars


class Only2StrParse(Parser):

    FILE_STR_COUNT = 2

    def parsing(self):
        count = 0
        result = {}
        file_name = self.file_name
        try:
            route = os.path.abspath(self.file_name)
            with open(route, 'r') as my_file:
                for line in my_file:
                    if count <= Only2StrParse.FILE_STR_COUNT:
                        new_str = line.strip('\n')
                        split = new_str.split(self.delim)
                        new_lst = split
                        result[new_lst[0]] = new_lst[1:len(new_lst)]
                        count += 1
                    else:
                        print("этот парсер предназначен для работы с двумя строчками файла")
                        return
                return print(result)
        except FileNotFoundError:
            print('Файла {}'.format(file_name) + ' не существует')


pars_1 = Parser('list.csv', ';')
pars_1.parsing()
print('В файле {}'.format(pars_1.file_name), pars_1.file_len, 'символа')

r = pars_1.abspath()
print('Файл для парсинга находится по пути:', r)
print(pars_1.__repr__())
print(pars_1.__str__())

pars_2 = Only2StrParse('list.csv', ';')
pars_2.parsing()

