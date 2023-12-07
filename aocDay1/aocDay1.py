import re


def partOne():
    with open('input.txt') as input:
        result = 0
        for line in input:
            first = re.search(r'\d', line).group(0)
            last = re.search(r'\d', line[::-1]).group(0)
            result += int(first + last)
        print(result)


def partTwo():
    with open('input.txt') as input:
        result = 0
        for line in input:
            # replace string of digits with digits
            cleanedLine = line.replace(r'one', 'o1ne').replace(r'two', 't2wo').replace(r'three', 't3hree').replace(
                r'four', 'f4our').replace(r'five', 'f5ive').replace(r'six', 's6ix').replace(r'seven', 's7even').replace(
                r'eight', 'e8ight').replace(r'nine', 'n9ine')
            first = re.search(r'\d', cleanedLine).group(0)
            last = re.search(r'\d', cleanedLine[::-1]).group(0)
            result += int(first + last)
        print(result)


if __name__ == '__main__':
    partTwo()
