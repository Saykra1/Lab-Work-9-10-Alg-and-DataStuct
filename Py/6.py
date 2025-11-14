def ternary_search_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Делим диапазон на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Проверяем граничные точки
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Определяем в какой трети продолжать поиск
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


# Рекурсивная версия тернарного поиска
def ternary_search_recursive(arr, target, left, right):
    """
    Рекурсивная версия тернарного поиска
    """
    if left > right:
        return -1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

def test_exponential_search():
    arr = [2, 3, 4, 10, 15, 18, 20, 23, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    targets = [10, 35, 100, 5, 95]

    print("\nМассив:", arr)
    print("Экспоненциальный поиск:")
    for target in targets:
        index = ternary_search_array(arr, target)
        if index != -1:
            print(f"Элемент {target} найден на позиции {index}")
        else:
            print(f"Элемент {target} не найден")

test_exponential_search()