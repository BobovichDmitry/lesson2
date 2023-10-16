birth_year_pushkin = '1799' #1799
birth_year_lenin = '1984' #1984
birth_year_stalin = '1984' #1984
birth_year_putin = '1984' #1984
birth_year_bobovich = '1984' #1984
repeat = True
while repeat != False:
    count = 0
    born_year_pushkin_q = input('Введите ГОД рождения А.С. Пушкина: ')
    if born_year_pushkin_q == birth_year_pushkin:
        count += 1
    born_year_lenin_q = input('Введите ГОД рождения Ленина: ')
    if born_year_lenin_q == birth_year_lenin:
        count += 1

    born_year_stalin_q = input('Введите ГОД рождения Сталина: ')
    if born_year_stalin_q == birth_year_stalin:
        count += 1

    born_year_putin_q = input('Введите ГОД рождения Путина: ')
    if born_year_putin_q == birth_year_putin:
        count += 1

    born_year_bobovich_q = input('Введите ГОД рождения Д.А. Бобовича: ')
    if born_year_bobovich_q == birth_year_bobovich:
        count += 1
    print('Количество правильных ответов:', count)
    print('Количество правильных ответов:', 5 - count)
    print('Процент правильных ответов:', count * 100 / 5)
    print('Процент Неправильных ответов:', ((5 - count) * 100) / 5)
    vopros_repeat = input('Повторим игру? (Y/N): ')
    if vopros_repeat == 'Y' or 'y':
        repeat = True
    else:
        break
