def part_1(array):
    sample_counts = {"red": 12, "green": 13, "blue": 14}
    possible_games_sum = 0
    def verify_game(draws_str, counts = sample_counts):
        for draw_str in draws_str.split("; "):
            for cube_count in draw_str.split(", "):
                count, color = cube_count.split()
                count = int(count)

                if count > counts.get(color, 0):
                    return False
        return True

    for line in array:
        id, draws = line.split(": ")
        id = int(id[5:])
        if verify_game(draws):
            possible_games_sum += id

    return possible_games_sum

def part_2(array):
    from functools import reduce
    from operator import mul
    power_sum = 0
    def get_min_counts(draws_str: str) -> dict[str, int]:
        counts = {}

        for draw_str in draws_str.split("; "):
            for cube_count in draw_str.split(", "):
                count, color = cube_count.split()
                count = int(count)

                if color not in counts:
                    counts[color] = count
                else:
                    counts[color] = max(counts[color], count)
        return counts

    for line in array:
        _, draws = line.split(": ")
        min_counts = get_min_counts(draws)
        print(min_counts)
        power_sum += reduce(mul, min_counts.values())

    return power_sum

def main():
    in_file = open("day-2-input.txt", "r")
    data = in_file.readlines()
    in_file.close()

    part_1_sum = part_1(data)
    print(part_1_sum)
    part_2_sum = part_2(data)
    print(part_2_sum)
main()
