def minEatingSpeed(piles, H):
    # Визначаємо діапазон для бінарного пошуку
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours_required = 0

        # Розраховуємо час, необхідний для з'їдання бананів з поточним значенням К
        for pile in piles:
            hours_required += (pile + mid - 1) // mid  # Округлюємо вгору

        # Порівнюємо отриманий час із H і зміщуємо діапазон
        if hours_required > H:
            left = mid + 1
        else:
            right = mid

    return left


# Приклади використання
piles1 = [3, 6, 7, 11]
H1 = 8
print(minEatingSpeed(piles1, H1))  # Результат: 4

piles2 = [30, 11, 23, 4, 20]
H2 = 5
print(minEatingSpeed(piles2, H2))  # Результат: 30

piles3 = [30, 11, 23, 4, 20]
H3 = 6
print(minEatingSpeed(piles3, H3))  # Результат: 23
