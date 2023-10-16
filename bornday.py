born_year_pushkin=input('Введите ГОД рождения А.С. Пушкина: ')

if born_year_pushkin == '1799':
    born_day_pushkin = input('Введите ДЕНЬ рождения А.С. Пушкина: ') # 6 июня 1799 дата рождения
    if born_day_pushkin == '6':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
