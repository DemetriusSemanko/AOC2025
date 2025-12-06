import math

def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append([x for x in line.strip().split(" ") if x != ""])
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    runs = len(lines[0])
    for i in range(0, runs):
        nums = []
        for x in range(0, len(lines) - 1):
            nums.append(int(lines[x][i]))
        if (lines[len(lines) - 1][i] == "+"):
            acc += sum(nums)
        else:
            acc += math.prod(nums)
    return str(acc)

def part2(lines):
    acc = 0
    return str(acc)

if __name__=="__main__":
    main()
