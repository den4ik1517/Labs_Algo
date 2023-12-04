def naive_search(haystack, needle):
    comparisons = 0
    last_index = -1

    # Проходимо по основній стрічці "haystack"
    for i in range(len(haystack) - len(needle) + 1):
        match = True

        # Порівнюємо символи з "needle" та "haystack"
        for j in range(len(needle)):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        # Якщо відбулось входження, оновлюємо останній індекс
        if match:
            last_index = i

    return last_index, comparisons

haystack = "ababcababcabc"
needle = "abc"
result_index, comparisons_count = naive_search(haystack, needle)

print(f"Останнє входження '{needle}' в '{haystack}' знаходиться на індексі {result_index}.")
print(f"Кількість порівнянь: {comparisons_count}")
