import re


def partOne():
    with open('input.txt') as input:
        result = 0
        index = 0
        lines = [line.rstrip() for line in input]
        for line in lines:
            matches = re.finditer(r'\d+', line)
            for match in matches:
                startIndex = match.start()
                # exclusive
                endIndex = match.end()
                prevLine = lines[index - 1][
                           startIndex - 1 if startIndex > 0 else endIndex: endIndex + 1 if endIndex + 1 < len(
                               lines[index - 1]) else startIndex + 1] if index > 0 else ''
                nextLine = lines[index + 1][
                           startIndex - 1 if startIndex > 0 else endIndex: endIndex + 1 if endIndex + 1 < len(
                               lines[index - 1]) else startIndex + 1] if index + 1 < len(lines) else ''
                possibleTokenLocations = prevLine + nextLine + (line[startIndex - 1] if startIndex > 0 else '') + (
                    line[endIndex] if endIndex < len(line) else '')
                if len(re.findall(r'[^.\r\n\d]', possibleTokenLocations)) > 0:
                    result += int(match.group(0))

            index += 1
        print(result)


def partTwo():
    with open('input.txt') as input:
        result = 0
        index = 0
        lines = [line.rstrip() for line in input]
        for line in lines:
            matches = re.finditer(r'\*', line)
            for star in matches:
                startIndex = star.start()
                # exclusive
                endIndex = star.end()
                prevLine = lines[index - 1][
                           startIndex - 1 if startIndex > 0 else endIndex: endIndex + 1 if endIndex + 1 < len(
                               lines[index - 1]) else startIndex + 1] if index > 0 else ''
                nextLine = lines[index + 1][
                           startIndex - 1 if startIndex > 0 else endIndex: endIndex + 1 if endIndex + 1 < len(
                               lines[index - 1]) else startIndex + 1] if index + 1 < len(lines) else ''
                possibleTokenLocations = prevLine + '*' + nextLine + '*' + (
                    line[startIndex - 1] if startIndex > 0 else '') + '*' + (
                                             line[endIndex] if endIndex < len(line) else '')
                if len(re.findall(r'\d+', possibleTokenLocations)) == 2:
                    gearRatio = 1
                    if index > 0:
                        for match in re.finditer(r'\d+', prevLine):
                            digitIndex = match.start() + startIndex - 1
                            fullMatches = re.finditer(r'\d+', lines[index - 1])
                            for fullMatch in fullMatches:
                                if digitIndex >= fullMatch.start() - 1 and digitIndex < fullMatch.end():
                                    gearRatio *= int(fullMatch.group(0))
                    if index + 1 < len(lines):
                        for match in re.finditer(r'\d+', nextLine):
                            digitIndex = match.start() + startIndex - 1
                            fullMatches = re.finditer(r'\d+', lines[index + 1])
                            for fullMatch in fullMatches:
                                if digitIndex >= fullMatch.start() - 1 and digitIndex < fullMatch.end():
                                    gearRatio *= int(fullMatch.group(0))
                    fullMatches = re.finditer(r'\d+', line)
                    for fullMatch in fullMatches:
                        if endIndex == fullMatch.start() or startIndex == fullMatch.end():
                            gearRatio *= int(fullMatch.group(0))
                    result += gearRatio

            index += 1
        print(result)


if __name__ == '__main__':
    partTwo()
