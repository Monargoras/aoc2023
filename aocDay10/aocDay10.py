from shapely.geometry import Polygon, Point


connections = {
    'right': ['J', '-', '7'],
    'left': ['L', '-', 'F'],
    'up': ['|', 'F', '7'],
    'down': ['J', 'L', '|']
}

allowedConnections = {
    'J': ['left', 'up'],
    'L': ['right', 'up'],
    'F': ['right', 'down'],
    '7': ['left', 'down'],
    '-': ['right', 'left'],
    '|': ['up', 'down']
}

directionMap = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}


def getNextCoords(curCoords, coordsList, lines):
    for direction in allowedConnections[lines[curCoords[0]][curCoords[1]]] if lines[curCoords[0]][curCoords[1]] != 'S' else connections:
        # skip if out of bounds
        if curCoords[0] + directionMap[direction][0] < 0 or curCoords[0] + directionMap[direction][0] >= len(lines):
            continue
        if curCoords[1] + directionMap[direction][1] < 0 or curCoords[1] + directionMap[direction][1] >= len(lines[curCoords[0]]):
            continue
        if lines[curCoords[0] + directionMap[direction][0]][curCoords[1] + directionMap[direction][1]] in connections[direction]:
            res = (curCoords[0] + directionMap[direction][0], curCoords[1] + directionMap[direction][1])
            if res not in coordsList:
                return res
    return coordsList[0]


def partOne():
    with open('input.txt') as input:
        coords = []
        lines = [line.rstrip() for line in input.readlines()]
        # find line and column of letter S
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'S':
                    coords.append((i, j))
                    break
            if len(coords) > 0:
                break
        nextCoords = getNextCoords(coords[0], coords, lines)
        while nextCoords != coords[0]:
            coords.append(nextCoords)
            nextCoords = getNextCoords(nextCoords, coords, lines)
        print(len(coords) // 2)


def partTwo():
    with open('input.txt') as input:
        coords = []
        lines = [line.rstrip() for line in input.readlines()]
        # find line and column of letter S
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'S':
                    coords.append((i, j))
                    break
            if len(coords) > 0:
                break
        nextCoords = getNextCoords(coords[0], coords, lines)
        while nextCoords != coords[0]:
            coords.append(nextCoords)
            nextCoords = getNextCoords(nextCoords, coords, lines)
        # calc area enclosed by coords
        poly = Polygon(coords)
        insidePoints = []
        for i in range(int(poly.bounds[0]), int(poly.bounds[2]) + 1):
            for j in range(int(poly.bounds[1]), int(poly.bounds[3]) + 1):
                if poly.contains(Point(i, j)):
                    insidePoints.append((i, j))
        print(len(insidePoints))


if __name__ == '__main__':
    partTwo()
