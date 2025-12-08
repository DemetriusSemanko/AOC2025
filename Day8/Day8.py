import math

def main():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line.strip())
    print("Part 1 answer: " + part1(lines.copy()))
    print("Part 2 answer: " + part2(lines.copy()))

def part1(lines):
    acc = 0
    coords = []
    for line in lines:
        coord = line.split(",")
        coord_tuple = tuple([int(x) for x in coord])
        coords.append(coord_tuple)
    
    distances = []
    for x in range(0, len(coords) - 1):
        for y in range(x + 1, len(coords)):
            distances.append((distance(*coords[x], *coords[y]), coords[x], coords[y]))
    distances.sort(key=lambda val : val[0])
    visited = []
    circuits = []
    for d_tri in distances:
        coord_a = d_tri[1]
        coord_b = d_tri[2]
        
        if (coord_a not in visited):
            visited.append(coord_a)
            if (coord_b not in visited):
                visited.append(coord_b)

                circuit = []
                circuit.append(coord_a)
                circuit.append(coord_b)
                circuits.append(circuit.copy())
            else: # coord_b in visited
                for circuit in circuits:
                    if (coord_b in circuit):
                        circuit.append(coord_a)
                        break
        else: # coord_a in visited
            if (coord_b not in visited):
                # find the list with coord_a, add coord_b to it
                visited.append(coord_b)
                for circuit in circuits:
                    if (coord_a in circuit):
                        circuit.append(coord_b)
                        break

        #for d in distances:
            #print(d)

    circuit_sizes = [len(x) for x in circuits]
    circuit_sizes.sort()
    # print(circuit_sizes)
    # 1000 too low
    acc += math.prod(circuit_sizes[-3:])
    for d in distances:
        print(d)

    return str(acc)

def distance( x1, y1, z1, x2, y2, z2 ):  
    d = math.sqrt(math.pow(x2 - x1, 2) +
                  math.pow(y2 - y1, 2) +
                  math.pow(z2 - z1, 2) * 1.0)
    return d

def part2(lines):
    acc = 0
    return str(acc)

if __name__=="__main__":
    main()
