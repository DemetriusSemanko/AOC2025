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
    
    beam_cols = { (lines[0].index("S")): 1 }
    line_length = len(lines[0])

    for x in range(1, len(lines)): # For each remaining line
        splitter_cols = [i for i, val in enumerate(lines[x]) if val == "^"]
        new_beam_dicts = []
        seen_set = []

        if (splitter_cols != []): # We have split and possibly made new timelines
            for beam in beam_cols.keys(): # For each key in beam_cols
                if (beam in splitter_cols): # If that beam hits a splitter
                    seen_set.append(beam) # Add this beam so it can be removed later
                    if (beam > 0): # If that beam can go Left
                        new_dict = { beam - 1: beam_cols.get(beam)}
                        new_beam_dicts.append(new_dict)
                    if (beam < line_length - 1): # If that beam can go Right
                        new_dict = { beam + 1: beam_cols.get(beam) }
                        new_beam_dicts.append(new_dict)
        
            # Let's update beam_cols
            seen_set = set(seen_set)
            for beam in seen_set:
                beam_cols.pop(beam)
            # Let's add/update new beams
            for new_beam_dict in new_beam_dicts:
                keys = new_beam_dict.keys()
                for key in keys:
                    if (beam_cols.get(key) == None):
                        beam_cols[key] = new_beam_dict.get(key)
                    else:
                        beam_cols[key] = beam_cols.get(key) + new_beam_dict.get(key)
        acc = sum(beam_cols.values())

    return str(acc)

if __name__=="__main__":
    main()
