def main():
    line = ""
    with open("input.txt") as f:
        for x in f:
            line += x
    print("Part 1 answer: " + part1(line))
    print("Part 2 answer: " + part2(line))

def part1(lines):
    acc = 0
    ranges = lines.split(",")
    for x in ranges:
        range_vals = x.split("-")
        for x in range(int(range_vals[0]), int(range_vals[1]) + 1):
            val = str(x)
            if (len(val) % 2 == 0):
                first_half = val[0:len(val) // 2]
                sec_half = val[len(val) // 2:]
                if (first_half == sec_half):
                    acc += x
    return str(acc)

def part2(line):
    acc = 0
    ranges = line.split(",")
    for x in ranges:
        range_vals = x.split("-")
        for x in range(int(range_vals[0]), int(range_vals[1]) + 1):
            val = str(x) # Get each value in the range
            for size in range(1, len(val) // 2 + 1):
                master_slice = val[:size]
                if ("".join(val.split(master_slice)) == ""):
                    acc += x
                    break
    return str(acc)

if __name__=="__main__":
    main()
