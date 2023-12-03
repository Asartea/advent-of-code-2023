from collections import defaultdict

def get_symbol(x, y, lines):
    Rows = len(lines)
    Columns = len(lines[0])
    if 0 <= x < Columns and 0 <= y < Rows and lines[y][x] != "." and not lines[y][x].isdigit():
        return (lines[y][x], (x, y))
    else:
        return None

def day_3():
    gear_nums = defaultdict(list)
    part_1_total = 0
    part_2_total = 0
    lines = open("day-3-input.txt").read().splitlines()


    for y, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                left_edge = i - 1

                right_edge = i
                while right_edge < len(line) and line[right_edge].isdigit():
                    right_edge += 1

                number = int(line[left_edge + 1 : right_edge])

                symbol_pos = get_symbol(left_edge, y, lines) or get_symbol(right_edge, y, lines)

                for pos in range(left_edge, right_edge + 1):
                    symbol_pos = (
                        symbol_pos or get_symbol(pos, y - 1, lines) or get_symbol(pos, y + 1, lines)
                    )

                if symbol_pos:
                    part_1_total += number

                    symbol, pos = symbol_pos
                    if symbol == "*":
                        gear_nums[pos].append(number)

                i = right_edge
            else:
                i += 1

    for ds in gear_nums.values():
        if len(ds) == 2:
            part_2_total += ds[0] * ds[1]



    print("Part 1:",part_1_total)
    print("Part 2:", part_2_total)

if __name__ == "__main__":
    day_3()
