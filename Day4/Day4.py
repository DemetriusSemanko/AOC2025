def main():
    lines = []
    with open("input.txt") as f:
        for x in f:
            lines.append(list(x.rstrip()))
    
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    for row in range(0, len(lines)):
        for col in range(0, len(lines[row])):
            if (lines[row][col] == '@'):
                # Do position check
                if (validRoll(row, col, lines)):
                    acc += 1

    return str(acc)

def validRoll(row, col, lines):
    adjRolls = 0
    # N (row - 1, col)
    if (validIndex(row - 1, col, lines)):
        if (lines[row - 1][col] == '@'):
            adjRolls += 1

    # E (row, col + 1)
    if (validIndex(row, col + 1, lines)):
        if (lines[row][col + 1] == '@'):
            adjRolls += 1

    # S (row + 1, col)
    if (validIndex(row + 1, col, lines)):
        if (lines[row + 1][col] == '@'):
            adjRolls += 1

    # W (row, col - 1)
    if (validIndex(row, col - 1, lines)):
        if (lines[row][col - 1] == '@'):
            adjRolls += 1

    # NE (row - 1, col + 1)
    if (validIndex(row - 1, col + 1, lines)):
        if (lines[row - 1][col + 1] == '@'):
            adjRolls += 1

    # SE (row + 1, col + 1)
    if (validIndex(row + 1, col + 1, lines)):
        if (lines[row + 1][col + 1] == '@'):
            adjRolls += 1

    # SW (row + 1, col - 1)
    if (validIndex(row + 1, col - 1, lines)):
        if (lines[row + 1][col - 1] == '@'):
            adjRolls += 1

    # NW (row - 1, col - 1)
    if (validIndex(row - 1, col - 1, lines)):
        if (lines[row - 1][col - 1] == '@'):
            adjRolls += 1

    if (adjRolls < 4):
        return True
    else:
        return False

def validIndex(row, col, lines):
    validRow = row >= 0 and row < len(lines)
    if (validRow):
        return (col >= 0 and col < len(lines[row]))
    else:
        return False

def part2(lines):
    acc = 0
    done = False
    while(not done):
        oldAcc = acc
        for row in range(0, len(lines)):
            for col in range(0, len(lines[row])):
                if (lines[row][col] == '@'):
                    # Do position check
                    if (validRoll(row, col, lines)):
                        lines[row][col] = 'x'
                        acc += 1
        done = oldAcc == acc


    return str(acc)

if __name__=="__main__":
    main()
