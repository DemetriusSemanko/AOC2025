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

    # If a coord was visited, then it must
    # belong to a circuit already

    # We don't care about the distance, since we've
    # sorted the list of distance-coord triples on distance,
    # and we will iterate through them from closest
    # to furthest distances.
    max_conns = 10
    if (len(lines) == 1000):
        max_conns = 1000
    conns = 1
    #pre_conns = 0
    for (_, coord_a, coord_b) in distances:
        conns += 1
        if (coord_a not in visited):
            visited.append(coord_a)
            if (coord_b not in visited):
                # If we reached here, that's because neither of the coords
                # belong to a circuit, and since they are the currently
                # closest pair of junction boxes, they must be connected
                # together into a circuit of their own
                visited.append(coord_b)
                circuit = []
                circuit.append(coord_a)
                circuit.append(coord_b)
                circuits.append(circuit.copy())
            else: # coord_b in visited
                # If we reach here, then that means
                # coord_a does NOT belong to a circuit
                # coord_b DOES belong to a circuit

                # Find the circuit coord_b belongs to
                # and add coord_a to that circuit
                for circuit in circuits:
                    if (coord_b in circuit):
                        circuit.append(coord_a)
        else: # coord_a in visited
            if (coord_b not in visited):
                # If we reach here, then that means
                # coord_a DOES belong to a circuit
                # coord_b does NOT belong to a circuit
                visited.append(coord_b)
                
                # Find the circuit coord_a belongs to
                # and add coord_b to that circuit
                for circuit in circuits:
                    if (coord_a in circuit):
                        circuit.append(coord_b)
            else:
                # If both were visited, let's see if they are in the same
                # circuit. If they are NOT in the same circuit, then let us
                # combine them
                done = False
                for circuit_a in circuits:
                    if (done):
                        break
                    if (coord_a in circuit_a):
                        # We found the circuit which has coord_a
                        for circuit_b in circuits:
                            if (coord_b in circuit_b):
                                if (circuit_a != circuit_b):
                                    circuit_a.extend(circuit_b)
                                    circuits.remove(circuit_b)
                                    done = True
                                    break
        if (conns == max_conns):
            break
    
    circuit_sizes = [len(x) for x in circuits]
    circuit_sizes.sort(reverse=True)
    # Checking my visited list, I called set() on it,
    # to see if I have any duplicate visitations, which
    # I do not. I have exactly 1000; the length of input
    # 1000 too low
    acc += math.prod(circuit_sizes[:3])

    return str(acc)

def distance( x1, y1, z1, x2, y2, z2 ):
    d = (math.pow(x2 - x1, 2) +
        math.pow(y2 - y1, 2) +
        math.pow(z2 - z1, 2))
    return d

def part2(lines):
    acc = 0
    return str(acc)

if __name__=="__main__":
    main()
