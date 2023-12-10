import re


def partOne():
    with open('input.txt') as input:
        result = 0
        for card in input:
            winningNumbers = [int(nr) for nr in re.findall(r'\d+', card.split(':')[1].split('|')[0])]
            myNumbers = [int(nr) for nr in re.findall(r'\d+', card.split(':')[1].split('|')[1])]
            myWinningNumbers = list(set(winningNumbers) & set(myNumbers))
            if len(myWinningNumbers) > 0:
                score = 1
                for i in range(1, len(myWinningNumbers)):
                    score *= 2
                result += score
        print(result)


def partTwo():
    with open('input.txt') as input:
        lines = [line.rstrip() for line in input]
        cardDict = {int(re.findall(r'Card\s+\d+', card)[0].split(' ')[-1]): 1 for card in lines}
        index = 0
        for card in lines:
            # immediately increment as my indexing in the dict starts at 1
            index += 1
            winningNumbers = [int(nr) for nr in re.findall(r'\d+', card.split(':')[1].split('|')[0])]
            myNumbers = [int(nr) for nr in re.findall(r'\d+', card.split(':')[1].split('|')[1])]
            myWinningNumbers = list(set(winningNumbers) & set(myNumbers))
            if len(myWinningNumbers) > 0:
                for i in range(index + 1, index + 1 + len(myWinningNumbers)):
                    cardDict[i] += cardDict[index]
        print(str(sum(cardDict.values())))


if __name__ == '__main__':
    partTwo()
