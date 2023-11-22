def count_possible_pairs(n, pairs):
    # Створення пустого словника для зберігання кількості хлопців і дівчат у кожному племені
    tribes = {}

    # Заповнення словника на основі вхідних даних
    for pair in pairs:
        for person in pair:
            if person not in tribes:
                tribes[person] = {'boys': 0, 'girls': 0}

    for pair in pairs:
        tribes[pair[0]]['boys'] += 1
        tribes[pair[1]]['girls'] += 1

    # Підрахунок кількості можливих пар
    possible_pairs = 0
    for pair in pairs:
        possible_pairs += (tribes[pair[0]]['girls'] - 1) + (tribes[pair[1]]['boys'] - 1)

    return possible_pairs

# Зчитування вхідних даних
n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]

# Вивід результату
result = count_possible_pairs(n, pairs)
print(-result)
