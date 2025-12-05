def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    range_tuples = []
    for x in range(0, lines.index("")):
        vals = lines[x].split("-")
        range_tuples.append((int(vals[0]), int(vals[1])))
    
    avail_ids = []
    for x in range(lines.index("") + 1, len(lines)):
        avail_ids.append(int(lines[x]))
    for avail_id in avail_ids:
        for (lower, higher) in range_tuples:
            if (avail_id >= lower and avail_id <= higher):
                acc += 1
                break

    return str(acc)

def part2(lines):
    acc = 0
    range_tuples = []
    for x in range(0, lines.index("")):
        vals = lines[x].split("-")
        range_tuple = (int(vals[0]), int(vals[1]))
        range_tuples.append(range_tuple)

    changes = 0
    old_changes = -1
    while (old_changes != changes):
        old_changes = changes
        range_tuples = sorted(range_tuples)
        for i in range(0, len(range_tuples) - 1):
            tuple_l = range_tuples[i]
            tuple_r = range_tuples[i + 1]
            
            if (tuple_r[0] <= tuple_l[1]):
                range_tuples[i] = (min(tuple_l[0], tuple_r[0]), max(tuple_l[1], tuple_r[1]))
                del range_tuples[i + 1]
                changes += 1
                break
    for (lower, higher) in range_tuples:
        print(lower, higher)
        acc += ((higher - lower) + 1)
    # 319856290749062 too low
    # 326897330961684 too low
    # 326897330961757 wrong
    # 333025403601939 TODO: Test
    # 333060480948284 wrong
    # 351410652124351 wrong
    # 352716206375531 wrong 
    # 352716206375546 wrong
    # 352716206375547 TODO: Test
    # 352716206375569 wrong
    # 352716206375570 wrong
    return str(acc)

if __name__=="__main__":
    main()
