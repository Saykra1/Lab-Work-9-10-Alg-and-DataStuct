def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    # Если элемент в начале
    if arr[0] == target:
        return 0

    # Экспоненциально увеличиваем диапазон
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Бинарный поиск в найденном диапазоне
    return binary_search(arr, target, i // 2, min(i, n - 1))


def binary_search(arr, target, left, right):
    """
    Вспомогательная функция бинарного поиска
    """
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример использования
def test_exponential_search():
    arr = [2, 3, 4, 10, 15, 18, 20, 23, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    targets = [10, 35, 100, 5, 95]

    print("\nМассив:", arr)
    print("Экспоненциальный поиск:")
    for target in targets:
        index = exponential_search(arr, target)
        if index != -1:
            print(f"Элемент {target} найден на позиции {index}")
        else:
            print(f"Элемент {target} не найден")


test_exponential_search()