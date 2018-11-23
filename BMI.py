import json


# функция, которая проверяет есть ли в дирректории с файлом программы
# текстовый файл. Если его не существует - создает его
def is_file():
    try:
        print('Проверка наличия файла для корректной работы программы...')
        with open('list.txt', 'r'):
            print('Все хорошо, файл найден. Начнем работу)')
            return
    except FileNotFoundError:
        with open('list.txt', 'w'):
            print('Создан пустой файл "list.txt". Давайте начнем)')


# функция для отображения главного меню. Возвращает выбранный пункт меню
def menu():
    main_menu = '\n1. Просмотреть всех пользователей\n' \
                '2. Добавить пользователя\n' \
                '3. Удалить пользователя\n' \
                '4. Редактировать пользователя\n' \
                '0. Выход'
    print(main_menu)
    choice = int(input('\nВыберете пункт меню: '))
    return choice


# функция, которая создает рекомендацию о пользователе.
# Принимает словарь и ключ
def recomendation(users, user):
    greeting = ''
    RECOMENDATION_BAD = 'Все очень плохо. И тут даже не до шуток. ' \
                        'Рекомендуем повышение веса и лечение анерексии. ' \
                        'ВЫСОКИЙ риск угрозы здоровью.'
    RECOMENDATION_NOT_BAD = 'ОТСУТСТВУЕТ риск для здоровья. ' \
                            'Однако все же непобходимо чуть-чуть больше кушать.'
    RFECOMENDATION_NORM = 'Все прекрасно. Можете сосредоточиться ' \
                          'для достижения других жизненных целей)'
    RECOMENDATION_INCREASED = 'ПОВЫШЕННЫЙ риск для здоровья. ' \
                              'Рекомендуется похудение.'
    RECOMENDATION_HIGHT = 'ВЫСОКИЙ риск для здоровья. ' \
                          'Настоятельно рекомендуется снижение веса.'
    RECOMENDATION_VERY_HIGHT = 'ОЧЕНЬ ВЫСОКИЙ риск для здоровья. ' \
                               'Крайне необходимо снижение веса.'
    RECOMENDATION_EXTREMELY_HIGHT = 'ЧРЕЗВЫЧАЙНО ВЫСОКИЙ риск для здоровья. ' \
                                    'Необходимо немедленное снижение массы тела.'
    RECOMENDATION_FOR_MALE = 'Молодой человек, перестаньте играть в игры'
    RECOMENDATION_FOR_FEMALE = 'Юная леди, Вам еще детей рожать'

    # формула для расчета ИМТ (делим рост на 100, что бы расчеты были верны)
    weight = users[user]['weight']
    height = users[user]['height']
    sex = users[user]['sex']
    age = users[user]['age']
    bmi = weight / ((height / 100) ** 2)

    # Обращение по полу
    if sex.upper() == 'М':
        greeting = 'Уважаемый {}'
    elif sex.upper() == 'Ж':
        greeting = 'Уважаемая {}'

    # вывод на экран с помощью .format
    print('\n\n' + greeting.format(user), '\n'
          'Ваш рост: {}'.format(height), '\n'
          'Ваш вес: {}'.format(weight), '\n'
          'Ваш BMI: {}'.format(round(bmi, 2)))

    # вывод на экран просто переменных
    print('\n====Рекомендация====\n'
          ' - пол:', sex, '\n'
          ' - возраст:', age, '\n'
          ' - рост', height, '\n'
          ' - вес', weight, '\n\n')

    # рекомендации-константы;)
    if 18 <= age < 26:
        if 0 < bmi < 16:
            if sex == 'М':
                print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_MALE))
            else:
                print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_FEMALE))
        elif 16 < bmi < 18.5:
            print(RECOMENDATION_NOT_BAD)
        elif 18.5 < bmi < 22.9:
            print(RFECOMENDATION_NORM)
        elif 23 < bmi < 29.9:
            print(RECOMENDATION_INCREASED)
        elif 30 < bmi < 34.9:
            print(RECOMENDATION_HIGHT)
        elif 35 < bmi < 39.9:
            print(RECOMENDATION_VERY_HIGHT)
        elif bmi > 40:
            print(RECOMENDATION_EXTREMELY_HIGHT)
    elif age >= 26:
        if 0 < bmi < 16:
            if sex == 'М':
                print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_MALE))
            else:
                print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_FEMALE))
        elif 16 < bmi < 18.5:
            print(RECOMENDATION_NOT_BAD)
        elif 18.5 < bmi < 25.9:
            print(RFECOMENDATION_NORM)
        elif 26 < bmi < 30.9:
            print(RECOMENDATION_INCREASED)
        elif 31 < bmi < 35.9:
            print(RECOMENDATION_HIGHT)
        elif 36 < bmi < 40.9:
            print(RECOMENDATION_VERY_HIGHT)
        elif bmi > 41:
            print(RECOMENDATION_EXTREMELY_HIGHT)
    else:
        print('Вы еще слишком малы для таких забот\n')

    # Построение псевдографика
    graph = '0' + '_' * 18 + '18' + '-' * 12 + '30' + '=' * 10 + '40'
    graph = list(graph)
    if int(bmi) > 40:
        graph.append('Х')
    else:
        graph.insert(int(bmi), 'X')
    print("\nПсевдографик:",
          ''.join(graph), '\n')


# функция для вывода на экран списка ключей словаря
def list_users():
    with open('list.txt', 'r') as my_file:
        users_list = []
        if len(my_file.readline()) != 0:
            my_file.seek(0)
            for line in my_file:
                dict_contents = json.loads(line)
                [users_list.append(key) for key in dict_contents.keys()]
    print('\n--Пользователи--\n' + ', '.join(users_list) + '\n')


# функция добавления пользователя.
def add_user():
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    sex = input('Пол М/Ж: ').upper()
    while True:
        if sex == 'M' or sex == 'F':
            break
        else:
            print('Поле "Пол" должно содержать либо "m" либо "f"')
            sex = input('Пол М/Ж: ').upper()
    weight = int(input('Введите вес в кг: '))
    height = int(input('Введите рост в см: '))

    # в каждую строчку файла добавляется словарь
    with open('list.txt', 'a+') as my_file:
        dict_contents = {name: {'age': age, 'sex': sex, 'weight': weight, 'height': height}}
        my_file.write(json.dumps(dict_contents))
        my_file.write('\n')
        print('\nПользователь {} успешно добавлен\n'.format(name))


# функция удаления пользователя
def del_user():
    selected_users = input('\nвведите имя пользователя, которого необходимо удалить\n'
                           'или нажмите Enter для выхода в главное меню: ')

    # создается пустой словарь. Заполняется значениями из файла. После чего удаляем ззначение инпута
    dict = {}
    with open('list.txt', 'r') as my_file:
        for line in my_file:
            dict_contents = json.loads(line)
            dict.update(dict_contents)
        try:
            del dict[selected_users]
            print('\nПользователь ' + str(selected_users) + ' успешно удален\n')
        except KeyError:
            print('\nПользователя ' + str(selected_users) + ' не существует\n')

    # открываем файл на запись (он пустой, соответственно).
    # Построчно заполняется оставшимся после удаления, словарем
    with open('list.txt', 'w') as my_file:
        for key, value in dict.items():
            my_file.write(json.dumps({key: value}))
            my_file.write('\n')


# Функция редактирования пользователя
def edit_user():

    # создается список ключей из каждой строчки файла (словарей)
    with open('list.txt', 'r') as my_file:
        users_list = []
        my_file.seek(0)
        for line in my_file:
            dict_contents = json.loads(line)
            [users_list.append(key) for key in dict_contents.keys()]
    print('\n--Пользователи--\n' + ', '.join(users_list) + '\n')
    selected_users = input('введите имя пользователя для просмотра информации о нем: ')

    # создается пустой словарь. Заполняется значениями из файла
    dict = {}
    with open('list.txt', 'r') as my_file:
        for line in my_file:
            dict_contents = json.loads(line)
            dict.update(dict_contents)
    if selected_users in dict.keys():
        print('\n1. Расчитать BMI пользователя'
              '\n2. Обновить информацию о пользователе\n'
              '0. Выход в главное меню\n')
        local_choice = int(input())

        if local_choice == 0:
            return

        elif local_choice == 1:
            recomendation(dict, selected_users)

        elif local_choice == 2:
            age = int(input('Введите возраст: '))
            sex = input('Пол М/Ж: ').upper()
            while True:
                if sex == 'M' or sex == 'F':
                    break
                else:
                    print('Поле "Пол" должно содержать либо "m" либо "f"')
                    sex = input('Пол М/Ж: ').upper()
            weight = int(input('Введите вес в кг: '))
            height = int(input('Введите рост в см: '))

            # обновляет словарь. После чего проходим циклом по словарю и построчно записываем в файл
            dict.update({selected_users: {'age': age, 'sex': sex, 'weight': weight, 'height': height}})
            with open('list.txt', 'w') as my_file:
                for key, value in dict.items():
                    my_file.write(json.dumps({key: value}))
                    my_file.write('\n')
    else:
        print('\nПользователя ' + str(selected_users) + ' не существует\n')
        return


# Работа программы
is_file()

while True:

    choice = menu()

    if choice == 1:
        list_users()

    if choice == 2:
        add_user()

    if choice == 3:
        del_user()

    if choice == 4:
        edit_user()

    if choice == 0:
        break
