import math


def jump_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    # Определяем размер прыжка
    step = int(math.sqrt(n))

    # Находим блок, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Линейный поиск в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    # Проверяем, найден ли элемент
    if arr[prev] == target:
        return prev
    return -1


# Пример использования
def test_jump_search():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    targets = [13, 1, 144, 100]

    print("Массив:", arr)
    print("Поиск скачками:")
    for target in targets:
        index = jump_search(arr, target)
        if index != -1:
            print(f"Элемент {target} найден на позиции {index}")
        else:
            print(f"Элемент {target} не найден")


test_jump_search()