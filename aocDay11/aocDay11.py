import itertools


def calculateManhattanDistance(x1, y1, x2, y2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance


def partOne():
    with open('input.txt') as input:
        lines = [line.rstrip() for line in input.readlines()]
        galaxies = {}
        nextGalaxyId = 1
        row = 0
        for line in lines:
            column = 0
            if line.find('#') != -1:
                for char in line:
                    if char == '#':
                        galaxies[nextGalaxyId] = (row, column)
                        nextGalaxyId += 1
                    column += 1
            row += 1
        nextGalaxyId = 1
        for galaxy in galaxies.values():
            lines[galaxy[0]] = lines[galaxy[0]][:galaxy[1]] + str(nextGalaxyId) + lines[galaxy[0]][galaxy[1] + 1:]
            nextGalaxyId += 1
        rowsWithoutGalaxies = [row for row in range(len(lines)) if len([galaxy for galaxy in galaxies.values() if galaxy[0] == row]) == 0]
        rowsWithoutGalaxies.reverse()
        columnsWithoutGalaxies = [column for column in range(len(lines[0])) if len([galaxy for galaxy in galaxies.values() if galaxy[1] == column]) == 0]
        columnsWithoutGalaxies.reverse()
        for dupeRow in rowsWithoutGalaxies:
            lines.insert(dupeRow, lines[dupeRow])
            for galaxyId, coords in galaxies.items():
                if coords[0] > dupeRow:
                    galaxies[galaxyId] = (coords[0] + 1, coords[1])
        for dupeColumn in columnsWithoutGalaxies:
            for i in range(len(lines)):
                lines[i] = lines[i][:dupeColumn] + '.' + lines[i][dupeColumn:]
            for galaxyId, coords in galaxies.items():
                if coords[1] > dupeColumn:
                    galaxies[galaxyId] = (coords[0], coords[1] + 1)
        visitedGalaxies = []
        pathLengths = []
        for galaxyId, coords in galaxies.items():
            visitedGalaxies.append(galaxyId)
            for secondGalaxy in [g for g in galaxies.keys() if g not in visitedGalaxies]:
                pathLengths.append(calculateManhattanDistance(coords[1], coords[0], galaxies[secondGalaxy][1], galaxies[secondGalaxy][0]))
        print(sum(pathLengths))


def partTwo():
    with open('input.txt') as input:
        lines = [line.rstrip() for line in input.readlines()]
        galaxies = {}
        nextGalaxyId = 1
        row = 0
        for line in lines:
            column = 0
            if line.find('#') != -1:
                for char in line:
                    if char == '#':
                        galaxies[nextGalaxyId] = (row, column)
                        nextGalaxyId += 1
                    column += 1
            row += 1
        nextGalaxyId = 1
        for galaxy in galaxies.values():
            lines[galaxy[0]] = lines[galaxy[0]][:galaxy[1]] + str(nextGalaxyId) + lines[galaxy[0]][galaxy[1] + 1:]
            nextGalaxyId += 1
        rowsWithoutGalaxies = [row for row in range(len(lines)) if len([galaxy for galaxy in galaxies.values() if galaxy[0] == row]) == 0]
        columnsWithoutGalaxies = [column for column in range(len(lines[0])) if len([galaxy for galaxy in galaxies.values() if galaxy[1] == column]) == 0]
        visitedGalaxies = []
        pathLengths = []
        for (x1, y1), (x2, y2) in itertools.combinations(galaxies.values(), 2):
            path = calculateManhattanDistance(x1, y1, x2, y2)
            emptyRowsBetween = sum(min(x1, x2) < x < max(x1, x2) for x in rowsWithoutGalaxies) * (1000000 - 1)
            emptyColsBetween = sum(min(y1, y2) < y < max(y1, y2) for y in columnsWithoutGalaxies) * (1000000 - 1)
            pathLengths.append(path + emptyRowsBetween + emptyColsBetween)
        print(sum(pathLengths))


if __name__ == '__main__':
    partTwo()
