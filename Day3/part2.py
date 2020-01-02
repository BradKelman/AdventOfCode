from pickle import LIST

f = open("/Users/kelmanb/Documents/Python/Xmas/AdventOfCode/Day3/inputs.txt", "r")
wire = f.readlines()
wires = [wire.rstrip('\n').split(',') for wire in wire]
f.close()

def wire_tracker(wires):
    x_coord = 0
    y_coord = 0
    coords = []
    for direction in wires:
        if direction[0] == 'U':
            for i in range(int(direction[1:])):
                y_coord += 1
                coords.append((x_coord, y_coord))
        elif direction[0] == 'R':
            for i in range(int(direction[1:])):
                x_coord += 1
                coords.append((x_coord, y_coord))
        elif direction[0] == 'D':
            for i in range(int(direction[1:])):
                y_coord -= 1
                coords.append((x_coord, y_coord))
        elif direction[0] == 'L':
            for i in range(int(direction[1:])):
                x_coord -= 1
                coords.append((x_coord, y_coord))
    return coords

# def change_to_rounded_brackets(wires_coords):
#     return str(wires_coords).replace('[', '(').replace(']', ')')

def intersections(wires):
    wire1 = wires[0]
    wire2 = wires[1]
    wire1_coords = wire_tracker(wire1)
    wire2_coords = wire_tracker(wire2)
    print(wire2_coords)
    tup_wire2_coords = tuple(wire2_coords)
    print(tup_wire2_coords)
    intersections ={}
    for coord in wire1_coords:
        if coord in wire2_coords:
            intersections[coord] = wire1_coords.index(coord) + wire2_coords.index(coord) +2

    return min(intersections.items(),key=lambda x:x[1])[1]

print("Does this work?: ", intersections(wires))