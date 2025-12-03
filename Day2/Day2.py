def main():
    lines = []
    with open("input.txt") as f:
        for x in f:
            if (x != "\n"):
                lines.append(x)
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    for item in lines:
        ranges = item.split(",")
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

def part2(lines):
    acc = 0
    for item in lines:
        ranges = item.split(",")
        for x in ranges:
            range_vals = x.split("-")
            for x in range(int(range_vals[0]), int(range_vals[1]) + 1): # This indexes thru all values in the range
                val = str(x) # Get each value in the range
                for size in range(1, len(val) // 2 + 1): # Builds the size of the window
                    master_slice = val[:size]
                    if ("".join(val.split(master_slice)) == ""):
                        acc += x
                        break
    return str(acc)

if __name__=="__main__":
    main()
