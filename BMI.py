import pprint

# users = {'Serg': {'возраст': 20, "пол": "м", "вес": 75, "рост": 160}}

try:
    users
except NameError:
    users = {}


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


# функция, которая создает рекомендацию о пользователе. Принимает пользователя
def recomendation(user):
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
    weight = users[user]['вес']
    height = users[user]['рост']
    sex = users[user]['пол']
    age = users[user]['возраст']
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
                                                                                                       'Ваш BMI: {}'.format(
        round(bmi, 2)))

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


# функция для вывода на экран ключей словаря (пользователей). Принимает словарь.
def list_users(users):
    users_list = []
    [users_list.append(key) for key in users.keys()]
    print('\n--Пользователи--\n' + ', '.join(users_list) + '\n')


# функция добавления пользователя. Принимает словарь и в зависимости
# от того, пустой он или нет, добавляет или обновляет информацию
# возвращает обновленный словарь
def add_user(users):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    sex = input('Пол М/Ж: ').upper()
    while True:
        if sex == 'М' or sex == 'Ж':
            break
        else:
            print('Поле "Пол" должно содержать либо "м" либо "ж"')
            sex = input('Пол М/Ж: ').upper()
    weight = int(input('Введите вес в кг: '))
    height = int(input('Введите рост в см: '))
    if len(users) == 0:
        users = {
            name: {
                'возраст': age,
                'пол': sex,
                'вес': weight,
                'рост': height
            }
        }
        print('Пользователь {} успешно добавлен'.format(name))
        return users
    else:
        users.update({name: {'возраст': age, 'пол': sex, 'вес': weight, 'рост': height}})
        print('\nПользователь {} успешно добавлен\n'.format(name))
        return users


# функция удаления пользователя. Принимает словарь. Возвращает обновленный словарь
def del_user(users):
    selected_users = input('\nвведите имя пользователя, которого необходимо удалить\n'
                           'или нажмите Enter для выхода в главное меню: ')
    if selected_users == '':
        return
    try:
        del users[selected_users]
        print('\nПользователь ' + str(selected_users) + ' успешно удален\n')
    except KeyError:
        print('\nПользователя ' + str(selected_users) + ' не существует\n')
    return users


# Функция редактирования пользователя. На вход принимает словарь
# возвращает обновленный словарь
def edit_user(users):
    # Вывод на экран существующий пользователей
    users_list = []
    [users_list.append(key) for key in users.keys()]
    print('\n--Пользователи--\n' + ', '.join(users_list) + '\n')

    # выход в главное меню, добавление рекомендации, и обновление данных пользователя
    selected_users = input('введите имя пользователя для просмотра информации о нем: ')
    for key in users.keys():
        if key == selected_users:
            print()
            pprint.pprint(users.get(selected_users))
            print('\n1. Расчитать BMI пользователя'
                  '\n2. Обновить информацию о пользователе\n'
                  '0. Выход в главное меню\n')
            local_choice = int(input())

            if local_choice == 0:
                break

            elif local_choice == 1:
                recomendation(selected_users)

            elif local_choice == 2:
                age = int(input('Введите возраст: '))
                sex = input('Пол М/Ж: ').upper()
                while True:
                    if sex == 'М' or sex == 'Ж':
                        break
                    else:
                        print('Поле "Пол" должно содержать либо "м" либо "ж"')
                        sex = input('Пол М/Ж: ').upper()
                weight = int(input('Введите вес в кг: '))
                height = int(input('Введите рост в см: '))
                users.update({selected_users: {'возраст': age, 'пол': sex, 'вес': weight, 'рост': height}})
                print('\nПользователь {} успешно отредактирован\n'.format(selected_users))

    return users


# цикл для работы программы
while True:
    choice = menu()

    if choice == 1:
        list_users(users)

    if choice == 2:
        users = add_user(users)

    if choice == 3:
        users = del_user(users)

    if choice == 4:
        users = edit_user(users)

    if choice == 0:
        break
