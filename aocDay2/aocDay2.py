import re


def partOne():
    with open('input.txt') as input:
        result = 0
        for game in input:
            gameId = int(re.findall(r'Game \d+', game)[0].split(' ')[1])
            redSamples = [int(s.split(' ')[0]) for s in re.findall(r'\d+ red', game)]
            if any([r > 12 for r in redSamples]):
                continue
            greenSamples = [int(s.split(' ')[0]) for s in re.findall(r'\d+ green', game)]
            if any([g > 13 for g in greenSamples]):
                continue
            blueSamples = [int(s.split(' ')[0]) for s in re.findall(r'\d+ blue', game)]
            if any([b > 14 for b in blueSamples]):
                continue
            result += gameId
        print(result)


def partTwo():
    with open('input.txt') as input:
        result = 0
        for game in input:
            minRed = max([int(s.split(' ')[0]) for s in re.findall(r'\d+ red', game)])
            minGreen = max([int(s.split(' ')[0]) for s in re.findall(r'\d+ green', game)])
            minBlue = max([int(s.split(' ')[0]) for s in re.findall(r'\d+ blue', game)])
            result += (minRed * minGreen * minBlue)
        print(result)


if __name__ == '__main__':
    partTwo()
