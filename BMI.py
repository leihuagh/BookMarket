# входные параметры
name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))

sex = input('Пол М/Ж: ').upper()
while True:
    if sex == 'М' or sex == 'Ж': # ждем от пользователя строго ввода "М" или "Ж"
        break
    else:
        print('Поле "Пол" должно содержать либо "м" либо "ж"')
        sex = input('Пол М/Ж: ').upper()

weight = int(input('Введите Ваш вес в кг: '))
height = int(input('Введите Ваш рост в см: '))
greeting = ''
RECOMENDATION_BAD = 'Все очень плохо. И тут даже не до шуток. ' \
                    'Рекомендуем повышение веса и лечение анерексии. ' \
                    'ВЫСОКИЙ риск угрозы здоровью.'
RECOMENDATION_NOT_BAD = 'ОТСУТСТВУЕТ риск для здоровья. '\
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
bmi = weight / ((height / 100) ** 2)

# Обращение по полу
if sex == 'М':
    greeting = 'Уважаемый {}'
elif sex == 'Ж':
    greeting = 'Уважаемая {}'

# вывод на экран с помощью .format
print('\n\n' + greeting.format(name), '\n'
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
if 18 < age < 26:
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
        if sex == 'М':
            print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_MALE))
        else:
            print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_FEMALE))
elif age > 26:
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
        if sex == 'М':
            print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_MALE))
        else:
            print(RECOMENDATION_BAD, '{}'.format(RECOMENDATION_FOR_FEMALE))


# построение псевдографика:
# строка в список. Добавляю "X" в соответствии со значением bmi
# список в строку
graph = '0' + '_' * 18 + '18' + '-' * 12 + '30' + '=' * 10 + '40'
graph = list(graph)
if int(bmi) > 40:
    graph.append('Х')
else:
    graph.insert(int(bmi), 'X')
print("\nПсевдографик:",
      ''.join(graph))
