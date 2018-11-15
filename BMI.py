name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
sex = input('Пол М/Ж: ').upper()

while True:
    if sex == 'М' or sex == 'Ж':
        break
    else:
        print('Поле "Пол" должно содержать либо "м" либо "ж"')
        sex = input('Пол М/Ж: ').upper()

weight = int(input('Введите Ваш вес в кг: '))
height = int(input('Введите Ваш рост в см: '))
greeting = ''
recomendation = ''
graph = '__________________=======+++++++++++++++'

bmi = weight / ((height / 100) ** 2)


if 0 < bmi < 18.5:
    recomendation = 'У Вас выраженный дефицит массы тела. ' \
                    'Рекомендуем больше есть'
elif 18.5 < bmi < 25:
    recomendation = 'У Вас все ок. Так держать!!!'
elif bmi > 25:
    recomendation = 'У Вас ожирение. Начните меньше кушать,' \
                    'запишитесь в тренажерный зал' \
                    'перестаньте играть в компьютерные игры' \
                    'заведите девушку, в конце концов'

if sex == 'М':
    greeting = 'Уважаемый {}'
elif sex == 'Ж':
    greeting = 'Уважаемая {}'

print('\n\n' + greeting.format(name), '\n'
      'Ваш рост: {}'.format(height), '\n'
      'Ваш вес: {}'.format(weight), '\n'
      'Ваш BMI: {}'.format(round(bmi, 2)))

print('\n====Рекомендация====\n'
      ' - пол:', sex, '\n'
      ' - возраст:', age, '\n'
      ' - рост', height, '\n'
      ' - вес', weight, '\n\n')

print(recomendation)

graph = list(graph)
if int(bmi) > 40:
    graph.append('Х')
else:
    graph.insert(int(bmi), 'X')
print("\nПсевдографик:",
      ''.join(graph))
