def changeString(number, text):
    if number == 1 < 5:
        text_change = f'{number} {text}'
        return text_change
    elif number < 5 and number != 0:
        prifex = 'а'
        text_change = f'{number} {text}{prifex}'
        return text_change
    elif number < 20 or number == 0:
        prifex = 'ов'
        text_change = f'{number} {text}{prifex}'
        return text_change
    elif number > 19:
        first_num = int(str(number)[:-1])
        secend_num = int(str(number)[-1])
        text_change = f'{str(first_num)+str(changeString(secend_num, text))}'
        return text_change 


if __name__ == "__main__":
    # changeString(2, 'товар')
    count = int(input('Введите количество итераций: '))
    i = 0
    while i < count:
        print(changeString(i, 'товар'))
        i += 1