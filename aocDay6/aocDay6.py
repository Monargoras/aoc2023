import re
from functools import reduce


def partOne():
    with open('input.txt') as input:
        result = 1
        numbers = re.findall(r'\d+', input.read())
        raceTimes = [int(n) for n in numbers[:len(numbers) // 2]]
        records = [int(n) for n in numbers[len(numbers) // 2:]]
        for raceTime in raceTimes:
            newRecordOptions = 0
            record = records.pop(0)
            for i in range(raceTime):
                if (raceTime - i) * i > record:
                    newRecordOptions += 1
            result *= newRecordOptions
        print(result)


def partTwo():
    with open('input.txt') as input:
        result = 1
        numbers = re.findall(r'\d+', input.read())
        raceTime = int(reduce(lambda x, y: x+y, numbers[:len(numbers) // 2]))
        record = int(reduce(lambda x, y: x+y, numbers[len(numbers) // 2:]))
        newRecordOptions = 0
        for i in range(raceTime):
            if (raceTime - i) * i > record:
                newRecordOptions += 1
        result *= newRecordOptions
        print(result)


if __name__ == '__main__':
    partTwo()
