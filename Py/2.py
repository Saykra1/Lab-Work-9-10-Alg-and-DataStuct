def pancake_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента
        max_idx = arr.index(max(arr[:curr_size]))

        if max_idx != curr_size - 1:
            # Переворачиваем до максимального элемента
            flip(arr, max_idx)
            # Переворачиваем весь подмассив
            flip(arr, curr_size - 1)

    return arr


def flip(arr, k):
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        left += 1
        k -= 1


# Пример использования
arr = [23, 10, 20, 11, 12, 6, 7]
print("Исходный массив:", arr)
sorted_arr = pancake_sort(arr.copy())
print("Отсортированный массив:", sorted_arr)