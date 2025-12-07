def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    pointer = 50
    for instr in lines:
        dir = instr[0]
        amt = int(instr[1:])
        
        mult = 1
        if (dir == "L"):
            mult = -1    
        
        pointer += (mult * amt)
        pointer %= 100

        if (pointer == 0):
            acc += 1

    return str(acc)

def part2(lines):
    acc = 0
    pointer = 50
    for instr in lines:
        dir = instr[0]
        amt = int(instr[1:])
        
        mult = 1
        if (dir == "L"):
            mult = -1

        while (amt != 0):
            pointer += mult
            amt -= 1
            if (pointer == 0 or pointer == 100):
                acc += 1
            pointer %= 100

    return str(acc)

if __name__=="__main__":
    main()
