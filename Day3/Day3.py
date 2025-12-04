def main():
    lines = []
    with open("input.txt") as f:
        for x in f:
            if (x != "\n"):
                lines.append(x.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    for bank in lines:
        max_jolt = 0
        for x in range(0, len(bank) - 1):
            head = bank[x]
            for y in range(x + 1, len(bank)):
                val = int(head + bank[y])
                max_jolt = max(max_jolt, val)
        acc += max_jolt
    return str(acc)

def part2(lines):
    acc = 0
    for bank in lines:
        max_jolt = ""
        sub = 11
        index = 0
        while(sub >= 0):
            bank_slice = bank[index:len(bank) - sub]
            max_digit = max([int(d) for d in bank_slice])
            max_jolt += str(max_digit)
            index = bank.find(str(max_digit)) + 1
            original_bank_size = len(bank)
            bank = bank[index:]
            diff = original_bank_size - len(bank)
            index -= diff
            sub -= 1
        acc += int(max_jolt)

    return str(acc)

if __name__=="__main__":
    main()
