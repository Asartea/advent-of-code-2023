in_file = open("day-4-input.txt")
data = in_file.readlines()
total = 0
matches = []
for line in data:
    _, numbers = line.split(":")
    winning_numbers, my_numbers = numbers.split("|")
    winners = set(map(int, winning_numbers.split()))
    numbers = set(map(int, my_numbers.split()))
    matches.append(len(numbers & winners))


score = sum(int(2**(n - 1)) for n in matches)
print('Part 1:', score)

copies = [1] * len(matches)

for i, n in enumerate(matches):
	for j in range(i + 1, i + n + 1):
		copies[j] += copies[i]

total = sum(copies)
print('Part 2:', total)
