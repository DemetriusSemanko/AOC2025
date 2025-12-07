def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    beam_cols = []
    beam_cols.append(lines[0].index("S"))
    line_length = len(lines[0])
    for x in range(1, len(lines)):
        # Get all splitter cols
        splitter_cols = [i for i, val in enumerate(lines[x]) if val == "^"]
        new_beam_cols = []
        if (splitter_cols != []):
            for beam in beam_cols:
                if (beam in splitter_cols):
                    acc += 1
                    go_left = beam > 0
                    go_right = beam < line_length - 1
                    if (go_left):
                        new_beam_cols.append(beam - 1)
                    if (go_right):
                        new_beam_cols.append(beam + 1)
                else:
                    new_beam_cols.append(beam)
            new_beam_cols = set(new_beam_cols)
            beam_cols = new_beam_cols.copy()

    return str(acc)

def part2(lines):
    acc = 0
    return str(acc)

if __name__=="__main__":
    main()
