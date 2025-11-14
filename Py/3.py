def bead_sort(arr):
    if not arr:
        return arr

    # Находим максимальное значение
    max_val = max(arr)

    # Создаем "абак" - матрицу бусин
    beads = [[0] * len(arr) for _ in range(max_val)]

    # Располагаем бусины на абаке
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1

    # Моделируем падение бусин под действием гравитации
    for i in range(max_val):
        # Считаем количество бусин в каждом ряду
        bead_count = sum(beads[i])
        # Опускаем бусины вниз
        for j in range(len(arr)):
            if j < bead_count:
                beads[i][j] = 1
            else:
                beads[i][j] = 0

    # Восстанавливаем отсортированный массив
    result = []
    for j in range(len(arr)):
        # Считаем количество бусин в каждом столбце
        column_sum = sum(beads[i][j] for i in range(max_val))
        result.append(column_sum)

    return result


# Пример использования
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Исходный массив:", arr)
sorted_arr = bead_sort(arr)
print("Отсортированный массив:", sorted_arr)