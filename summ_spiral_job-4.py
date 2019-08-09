NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # направление
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # старое -> новое направление

def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # Стартуем заполнение с центра
    dx, dy = NORTH # Направление куда двигаемся
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count #счетчик 
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # прямое движение
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # завершение заполнение

def print_matrix(matrix):
    # рисуем в матрицу в консоли
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

# print_matrix(spiral(7, 7))
n = 1001 # размер
matrix = spiral(n, n)
summ_arr = []
for _id, item in enumerate(matrix):
    # находим элемент с минимальным значением, добавляем в list
    summ_arr.append(min(item))
    if min(item):
        # смещаемся от краю к центру
        n -= 1
        for __id, i in enumerate(item):
            if min(item) == i:
                # Добавляем элемент в list и смещаемся еще раз
                summ_arr.append(matrix[_id][__id + n])
                n -= 1
print(sum(set(summ_arr)))
# Результат выполнения 669171001