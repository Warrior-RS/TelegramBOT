def get_cell_color():
    coord = input('Введите координату клетки (например, A1): ')
    letter = coord[0]
    number = int(coord[1])
    if letter in 'ACEG':
        if number % 2 == 0:
            return 'черный'
        else:
            return 'белый'
    else:
        if number % 2 == 0:
            return 'белый'
        else:
            return 'черный'
print(get_cell_color())

