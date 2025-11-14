def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Определяем количество корзин
    bucket_count = len(arr)
    max_val, min_val = max(arr), min(arr)
    bucket_range = (max_val - min_val) / bucket_count

    # Создаем корзины
    buckets = [[] for _ in range(bucket_count + 1)]

    # Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Сортируем каждую корзину и объединяем
    result = []
    for bucket in buckets:
        # Используем сортировку вставками для каждой корзины
        insertion_sort(bucket)
        result.extend(bucket)

    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Пример использования
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Исходный массив:", arr)
sorted_arr = bucket_sort(arr)
print("Отсортированный массив:", sorted_arr)