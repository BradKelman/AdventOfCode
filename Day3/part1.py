f = open("/Users/kelmanb/Documents/Python/Xmas/AdventOfCode/Day3/inputs.txt", "r")
wire = f.readlines()
wires = [wire.rstrip('\n').split(',') for wire in wire]
f.close()



def move_left(x, distance):
    x-=distance
    return x

def move_right(x, distance):
    x+=distance
    return x


def move_up(y, distance):
    y+=distance
    return y


def move_down(y, distance):
    y-=distance
    return y



def wire_tracker(wires):
    x_coord = 0
    y_coord = 0
    coords = []
    for direction in wires:
        if direction[0] == 'U':
            for i in range(int(direction[1:])):
                y_coord += 1
                coords.append([x_coord, y_coord])
        elif direction[0] == 'R':
            for i in range(int(direction[1:])):
                x_coord += 1
                coords.append([x_coord, y_coord])
        elif direction[0] == 'D':
            for i in range(int(direction[1:])):
                y_coord -= 1
                coords.append([x_coord, y_coord])
        elif direction[0] == 'L':
            for i in range(int(direction[1:])):
                x_coord -= 1
                coords.append([x_coord, y_coord])
    return coords



def intersections(wires):
    wire1 = wires[0]
    wire2 = wires[1]
    wire1_coords = wire_tracker(wire1)
    wire2_coords = wire_tracker(wire2)
    intersections = []
    for coord in wire1_coords:
        if coord in wire2_coords:
            intersections.append(coord)
    intersections = [abs(coord[0]) + abs(coord[1]) for coord in intersections]
    intersections.sort()
    return intersections[0]

print("Does this work?: ", intersections(wires))