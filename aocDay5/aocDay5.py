import re
from multiprocessing import Pool


def partOne():
    with open('input.txt') as input:
        resultLocationNumbers = []
        splitInput = input.read().split(':')
        seeds = [int(x) for x in re.findall(r'\d+', splitInput[1])]
        itSeedToSoil = iter([int(x) for x in re.findall(r'\d+', splitInput[2])])
        itSoilToFertalizer = iter([int(x) for x in re.findall(r'\d+', splitInput[3])])
        itFertalizerToWater = iter([int(x) for x in re.findall(r'\d+', splitInput[4])])
        itWaterToLight = iter([int(x) for x in re.findall(r'\d+', splitInput[5])])
        itLightToTemp = iter([int(x) for x in re.findall(r'\d+', splitInput[6])])
        itTempToHumidity = iter([int(x) for x in re.findall(r'\d+', splitInput[7])])
        itHumidityToLocation = iter([int(x) for x in re.findall(r'\d+', splitInput[8])])
        mapDict = {
            'seedToSoil': list(zip(itSeedToSoil, itSeedToSoil, itSeedToSoil)),
            'soilToFertalizer': list(zip(itSoilToFertalizer, itSoilToFertalizer, itSoilToFertalizer)),
            'fertalizerToWater': list(zip(itFertalizerToWater, itFertalizerToWater, itFertalizerToWater)),
            'waterToLight': list(zip(itWaterToLight, itWaterToLight, itWaterToLight)),
            'lightToTemp': list(zip(itLightToTemp, itLightToTemp, itLightToTemp)),
            'tempToHumidity': list(zip(itTempToHumidity, itTempToHumidity, itTempToHumidity)),
            'humidityToLocation': list(zip(itHumidityToLocation, itHumidityToLocation, itHumidityToLocation))
        }
        for seed in seeds:
            curVal = seed
            for key, value in mapDict.items():
                for dst, src, length in value:
                    if src <= curVal < src + length:
                        curVal = curVal + (dst - src)
                        break
            resultLocationNumbers.append(curVal)
        print(min(resultLocationNumbers))



def partTwo():
    with open('input.txt') as input:
        minimum = 999999999999
        splitInput = input.read().split(':')
        itSeeds = iter([int(x) for x in re.findall(r'\d+', splitInput[1])])
        seedsTuples = list(zip(itSeeds, itSeeds))
        ranges = [range(x[0], x[0] + x[1]) for x in seedsTuples]
        itSeedToSoil = iter([int(x) for x in re.findall(r'\d+', splitInput[2])])
        itSoilToFertalizer = iter([int(x) for x in re.findall(r'\d+', splitInput[3])])
        itFertalizerToWater = iter([int(x) for x in re.findall(r'\d+', splitInput[4])])
        itWaterToLight = iter([int(x) for x in re.findall(r'\d+', splitInput[5])])
        itLightToTemp = iter([int(x) for x in re.findall(r'\d+', splitInput[6])])
        itTempToHumidity = iter([int(x) for x in re.findall(r'\d+', splitInput[7])])
        itHumidityToLocation = iter([int(x) for x in re.findall(r'\d+', splitInput[8])])
        mapDict = {
            'seedToSoil': list(zip(itSeedToSoil, itSeedToSoil, itSeedToSoil)),
            'soilToFertalizer': list(zip(itSoilToFertalizer, itSoilToFertalizer, itSoilToFertalizer)),
            'fertalizerToWater': list(zip(itFertalizerToWater, itFertalizerToWater, itFertalizerToWater)),
            'waterToLight': list(zip(itWaterToLight, itWaterToLight, itWaterToLight)),
            'lightToTemp': list(zip(itLightToTemp, itLightToTemp, itLightToTemp)),
            'tempToHumidity': list(zip(itTempToHumidity, itTempToHumidity, itTempToHumidity)),
            'humidityToLocation': list(zip(itHumidityToLocation, itHumidityToLocation, itHumidityToLocation))
        }
        rIndex = 0
        for r in ranges:
            rIndex += 1
            print('range ' + str(rIndex))
            for seed in r:
                curVal = seed
                for key, value in mapDict.items():
                    for dst, src, length in value:
                        if src <= curVal < src + length:
                            curVal = curVal + (dst - src)
                            break
                if curVal < minimum:
                    minimum = curVal
        print(minimum)


def partTwoParallel():
    with open('input.txt') as input:
        splitInput = input.read().split(':')
        itSeeds = iter([int(x) for x in re.findall(r'\d+', splitInput[1])])
        seedsTuples = list(zip(itSeeds, itSeeds))
        ranges = [range(x[0], x[0] + x[1]) for x in seedsTuples]
        itSeedToSoil = iter([int(x) for x in re.findall(r'\d+', splitInput[2])])
        itSoilToFertalizer = iter([int(x) for x in re.findall(r'\d+', splitInput[3])])
        itFertalizerToWater = iter([int(x) for x in re.findall(r'\d+', splitInput[4])])
        itWaterToLight = iter([int(x) for x in re.findall(r'\d+', splitInput[5])])
        itLightToTemp = iter([int(x) for x in re.findall(r'\d+', splitInput[6])])
        itTempToHumidity = iter([int(x) for x in re.findall(r'\d+', splitInput[7])])
        itHumidityToLocation = iter([int(x) for x in re.findall(r'\d+', splitInput[8])])
        mapDict = {
            'seedToSoil': list(zip(itSeedToSoil, itSeedToSoil, itSeedToSoil)),
            'soilToFertalizer': list(zip(itSoilToFertalizer, itSoilToFertalizer, itSoilToFertalizer)),
            'fertalizerToWater': list(zip(itFertalizerToWater, itFertalizerToWater, itFertalizerToWater)),
            'waterToLight': list(zip(itWaterToLight, itWaterToLight, itWaterToLight)),
            'lightToTemp': list(zip(itLightToTemp, itLightToTemp, itLightToTemp)),
            'tempToHumidity': list(zip(itTempToHumidity, itTempToHumidity, itTempToHumidity)),
            'humidityToLocation': list(zip(itHumidityToLocation, itHumidityToLocation, itHumidityToLocation))
        }
        with Pool(10) as p:
            result = p.starmap(calcSingleRangeMinimum, ranges, mapDict)

        print(result)
        print(min(result))


def calcSingleRangeMinimum(r, mapDict):
    minimum = 9999999999999
    for seed in r:
        curVal = seed
        for key, value in mapDict.items():
            for dst, src, length in value:
                if src <= curVal < src + length:
                    curVal = curVal + (dst - src)
                    break
        if curVal < minimum:
            minimum = curVal
    return minimum


if __name__ == '__main__':
    partTwo()
