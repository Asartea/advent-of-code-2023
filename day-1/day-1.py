def main():
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digit_words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total_sum = 0
    in_file = open("day-1-input.txt")
    data = in_file.readlines()
    in_file.close()
    for line in in_file:
        found_digits = []
        for i, char in enumerate(line):
            if char in digits:
                found_digits.append(int(char))
            for word, digit in digit_words.items():
                if line[i:].startswith(word):
                    found_digits.append(digit)
        calibration_value = found_digits[0] * 10 + found_digits[-1]
        total_sum += calibration_value
    print(total_sum)

main()
