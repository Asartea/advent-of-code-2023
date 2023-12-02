def part_1(data):
    total_sum = 0
    for line in data:
        found_digits = []
        for char in line.split(""):
            if char.isdigit():
                found_digits.append(int(char))
        calibration_value = found_digits[0] * 10 + found_digits[-1]
        total_sum += calibration_value

    return total_sum

def part_2(data):
    digit_words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total_sum = 0
    for line in data:
        found_digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                found_digits.append(int(char))
            for word, digit in digit_words.items():
                if line[i:].startswith(word):
                    found_digits.append(digit)
        calibration_value = found_digits[0] * 10 + found_digits[-1]
        total_sum += calibration_value
    print(total_sum)

def main():
    in_file = open("day-1-input.txt")
    data = in_file.readlines()
    in_file.close()
    part_1_sum = part_1(data)
    print(part_1_sum)
    part_2_sum = part_2(data)
    print(part_2_sum)


main()
