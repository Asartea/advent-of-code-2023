def parse_input(input_string: str):
    groups = input_string.split('\n\n')

    seeds = groups[0]
    rest = groups[1:]

    seeds = list(map(int, seeds.split()[1:]))

    maps = {}

    for mapping in rest:
        lines = mapping.splitlines()
        key = lines[0]
        values = []
        for line in lines[1:]:
            values.append(tuple(map(int, line.split())))

        key = key.split()[0]
        a, b = key.split('-to-')
        maps[a,b] = values

    return seeds, maps

def find_sequence(maps: dict, start_type: str, end_type:str):
    sequence = [start_type]

    while start_type != end_type:
        next_type = None
        for a, b in maps:
            if a == start_type:
                next_type = b
        sequence.append(next_type)
        start_type = next_type

    return sequence

def do_mapping(value: int, maps: dict, sequence: list):
    sequence = sequence[:]
    while len(sequence) > 1:
        a = sequence.pop(0)
        b = sequence[0]
        mapping = maps[a,b]

        new_value = None

        for dst, src, size in mapping:
            if src <= value < src+size:

                off = value - src
                new_value = dst + off

        if new_value is None:
            new_value = value

        value = new_value

    return value

def part1(input_string: str):
    seeds, maps = parse_input(input_string)

    seq = find_sequence(maps, 'seed', 'location')

    answer = min(do_mapping(val, maps, seq)
                 for val in seeds)

    print("Part 1:", answer)

def do_mapping_2_help(vals: int, mapping):
    new_vals = []

    while len(vals) > 0:
        handled = False
        best_off = len(vals)

        for dst, src, size in mapping:
            if src <= vals[0] < src+size:
                off = vals[0] - src
                new_start = dst + off
                new_len = min(size - off, len(vals))
                new_vals.append(range(new_start, new_start+new_len))
                vals = vals[new_len:]
                handled = True
                break
            elif src < vals[0]:
                off = vals[0] - src
                best_off = min(best_off, off)

        if not handled:
            new_vals.append(vals[:best_off])
            vals = vals[best_off:]

    return new_vals

def do_mapping_2(val_ranges: list[int], maps : dict, seq: list[str]):
    seq = seq[:]
    while len(seq) > 1:
        a = seq.pop(0)
        b = seq[0]
        mapping = maps[a,b]

        new_ranges = []

        for r in val_ranges:
            print(r)
            new_ranges += do_mapping_2_help(r, mapping)

        val_ranges = new_ranges

    return val_ranges

def part2(input_string: str):
    seeds, maps = parse_input(input_string)

    seq = find_sequence(maps, 'seed', 'location')

    final_sequences = []

    for a, b in zip(seeds[::2], seeds[1::2]):
        final_sequences += do_mapping_2([range(a, a+b)], maps, seq)
    answer = min(r.start for r in final_sequences)

    print("Part 2:", answer)

input_data = open("day-5-input.txt").read()

part1(input_data)
part2(input_data)
