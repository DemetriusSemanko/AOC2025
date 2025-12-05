def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    return str(acc)

def part2(lines):
    acc = 0
    return str(acc)

if __name__=="__main__":
    main()
