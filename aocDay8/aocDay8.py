import re
from math import lcm


def partOne():
    with open('input.txt') as input:
        index = 0
        steps = 0
        directions = []
        nodes = {}
        for line in input:
            if index == 0:
                directions = [d for d in line.rstrip()]
            elif index > 1:
                lineRes = re.findall(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)[0]
                nodes[lineRes[0]] = (lineRes[1], lineRes[2])
            index += 1
        curLocation = 'AAA'
        while curLocation != 'ZZZ':
            curLocation = nodes[curLocation][0] if directions[steps % len(directions)] == 'L' else nodes[curLocation][1]
            steps += 1
        print(steps)


def partTwo():
    with open('input.txt') as input:
        index = 0
        directions = []
        nodes = {}
        for line in input:
            if index == 0:
                directions = [d for d in line.rstrip()]
            elif index > 1:
                lineRes = re.findall(r'([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)', line)[0]
                nodes[lineRes[0]] = (lineRes[1], lineRes[2])
            index += 1
        # all keys in nodes ending with A
        startLocations = [k for k in nodes.keys() if k.endswith('A')]
        cycles = []
        for node in startLocations:
            steps = 0
            curLocation = node
            while not curLocation.endswith('Z'):
                curLocation = nodes[curLocation][0] if directions[steps % len(directions)] == 'L' else nodes[curLocation][1]
                steps += 1

            cycles.append(steps)
        print(lcm(*cycles))


if __name__ == '__main__':
    partTwo()
