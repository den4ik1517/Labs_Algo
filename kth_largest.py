def kth_largest_element(arr, k):
    # Перевіряємо, чи k є допустимим значенням
    if k <= 0 or k > len(arr):
        return None, None

    # Створюємо список кортежів, де кожен кортеж містить значення та початковий індекс
    indexed_arr = [(val, idx) for idx, val in enumerate(arr)]

    # Використовуємо алгоритм сортування зі змінними (Selection Sort)
    for i in range(k):
        max_index = i
        # Знаходимо індекс найбільшого елемента в підмасиві
        for j in range(i + 1, len(indexed_arr)):
            if indexed_arr[j][0] > indexed_arr[max_index][0]:
                max_index = j
        # Обмінюємо елементи, щоб розмістити найбільший на потрібній позиції
        indexed_arr[i], indexed_arr[max_index] = indexed_arr[max_index], indexed_arr[i]

    # Знаходимо к-тий найбільший елемент та його початковий індекс у вихідному масиві
    kth_largest = indexed_arr[k - 1][0]
    position = indexed_arr[k - 1][1]

    return kth_largest, position

if __name__ == "__main__":
    arr = [15, 7, 22, 9, 36, 2, 42, 18]
    k = 3
    kth_largest, position = kth_largest_element(arr, k)

    if kth_largest is not None:
        print(f"Заданий {k}-й найбільший елемент: {kth_largest}")
        print(f"Позиція {k}-го найбільшого елемента в масиві: {position}")
    else:
        print(f"Некоректне значення k: {k}")
