def partOne():
    with open('input.txt') as input:
        result = 0
        for line in input:
            readings = [int(r) for r in line.rstrip().split(' ')]
            seriesList = [readings]
            # get differences between adjacent numbers until all 0
            while not all([r == 0 for r in seriesList[-1]]):
                # generate list of differences between adjacent numbers
                seriesList.append([seriesList[-1][i + 1] - seriesList[-1][i] for i in range(len(seriesList[-1]) - 1)])
            # add one predicted number to each list in seriesList reversed seriesList
            seriesList.reverse()
            index = 0
            for series in seriesList:
                if index == 0:
                    series.append(0)
                else:
                    series.append(series[-1] + seriesList[index - 1][-1])
                index += 1
            result += seriesList[-1][-1]
        print(result)


def partTwo():
    with open('input.txt') as input:
        result = 0
        for line in input:
            readings = [int(r) for r in line.rstrip().split(' ')]
            seriesList = [readings]
            # get differences between adjacent numbers until all 0
            while not all([r == 0 for r in seriesList[-1]]):
                # generate list of differences between adjacent numbers
                seriesList.append([seriesList[-1][i + 1] - seriesList[-1][i] for i in range(len(seriesList[-1]) - 1)])
            # add one predicted number to each list in seriesList reversed seriesList
            seriesList.reverse()
            index = 0
            for series in seriesList:
                if index == 0:
                    series.insert(0, 0)
                else:
                    series.insert(0, series[0] - seriesList[index - 1][0])
                index += 1
            result += seriesList[-1][0]
        print(result)


if __name__ == '__main__':
    partTwo()
