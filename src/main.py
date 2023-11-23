def read_file(file_path):
    tribes = {}
    girls = set()
    boys = set()

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if i == 0 or not line.strip():  # Пропускаємо перший рядок та порожні рядки
                continue

            # Вилучення двох чисел з рядка та конвертація їх у цілі числа
            number1, number2 = map(int, line.split())

            if number1 % 2 == 0:
                girls.add(number1)
            else:
                boys.add(number1)

            if number2 % 2 == 0:
                girls.add(number2)
            else:
                boys.add(number2)

            if i == 0:
                tribes[number1] = 0
                tribes[number2] = 0
            else:
                if number1 in tribes:
                    tribes[number2] = tribes[number1]
                elif number2 in tribes:
                    tribes[number1] = tribes[number2]
                else:
                    tribes[number1] = i
                    tribes[number2] = i
    return tribes, boys, girls

def group_by_tribe(tribes, boys, girls):
    # Словник для збереження груп
    tribe_groups = {"boys": {}, "girls": {}}

    for boy in boys:
        tribe = tribes.get(boy)
        if tribe is not None:
            if tribe not in tribe_groups["boys"]:
                tribe_groups["boys"][tribe] = []
            tribe_groups["boys"][tribe].append(boy)

    for girl in girls:
        tribe = tribes.get(girl)
        if tribe is not None:
            if tribe not in tribe_groups["girls"]:
                tribe_groups["girls"][tribe] = []
            tribe_groups["girls"][tribe].append(girl)

    return tribe_groups

def count_possible_pairs(tribe_groups):
    possible_pairs = []
    boys_tribes = tribe_groups["boys"]
    girls_tribes = tribe_groups["girls"]

    for boy_tribe in boys_tribes:
        for girl_tribe in girls_tribes:
            if boy_tribe != girl_tribe:
                boys_list = boys_tribes[boy_tribe]
                girls_list = girls_tribes[girl_tribe]
                for boy in boys_list:
                    for girl in girls_list:
                        possible_pairs.append((boy, girl))

    count = len(possible_pairs)
    return count, possible_pairs

def write_output(file_path, count, possible_pairs):
    with open(file_path, "w") as file:
        file.write("Result: " + str(count) + "\n")
        file.write("Possible Pairs:\n")
        for pair in possible_pairs:
            file.write(f"{pair[0]} {pair[1]}\n")

# ...

if __name__ == "__main__":
    input_file = "../test/input.txt"
    output_file = "../test/output.txt"

    tribes, boys, girls = read_file(input_file)
    tribe_groups = group_by_tribe(tribes, boys, girls)
    count, possible_pairs = count_possible_pairs(tribe_groups)
    write_output(output_file, count, possible_pairs)
