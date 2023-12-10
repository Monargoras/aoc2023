import re


def partOne():
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    types = ['five', 'four', 'fullHouse', 'three', 'twoPair', 'onePair', 'highCard']
    typeMap = {
        'five': [],
        'four': [],
        'fullHouse': [],
        'three': [],
        'twoPair': [],
        'onePair': [],
        'highCard': [],
    }
    result = 0
    with open('input.txt') as input:
        rank = sum(1 for _ in input)
        
    with open('input.txt') as input:
        for line in input:
            cardCount = {}
            cardTuples = []
            hand = line.split(' ')[0]
            bid = line.split(' ')[1]
            for card in cards:
                cardCount[card] = hand.count(card)
            for card in cards:
                cardTuples.append((card, cardCount[card]))
            cardTuples = sorted(cardTuples, key=lambda x: x[1])
            highestNrOfCards = cardTuples[-1]
            secondHighestNrOfCards = cardTuples[-2]
            if highestNrOfCards[1] == 5:
                typeMap['five'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 4:
                typeMap['four'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 3 and secondHighestNrOfCards[1] == 2:
                typeMap['fullHouse'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 3:
                typeMap['three'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 2 and secondHighestNrOfCards[1] == 2:
                typeMap['twoPair'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 2:
                typeMap['onePair'].append((hand, int(bid)))
            else:
                typeMap['highCard'].append((hand, int(bid)))
        for t in types:
            sortedList = sorted(typeMap[t], key=lambda x: (cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]), cards.index(x[0][4])))
            for handTuple in sortedList:
                result += handTuple[1] * rank
                rank -= 1
        print(result)


def partTwo():
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    types = ['five', 'four', 'fullHouse', 'three', 'twoPair', 'onePair', 'highCard']
    typeMap = {
        'five': [],
        'four': [],
        'fullHouse': [],
        'three': [],
        'twoPair': [],
        'onePair': [],
        'highCard': [],
    }
    result = 0
    with open('input.txt') as input:
        rank = sum(1 for _ in input)

    with open('input.txt') as input:
        for line in input:
            cardCount = {}
            cardTuples = []
            hand = line.split(' ')[0]
            bid = line.split(' ')[1]
            for card in cards:
                cardCount[card] = hand.count(card)

            # get joker cards and cards with highest count            
            nrJokers = cardCount['J']
            cardCount['J'] = 0
            for card in cards:
                cardTuples.append((card, cardCount[card]))
            cardTuples = sorted(cardTuples, key=lambda x: x[1])
            highestNrOfCards = cardTuples[-1]
            secondHighestNrOfCards = cardTuples[-2]

            # redistribute card counts with joker cards
            cardTuples = []
            if nrJokers > 0 and highestNrOfCards[0] != 'J':
                cardCount[highestNrOfCards[0]] = cardCount[highestNrOfCards[0]] + nrJokers
            elif nrJokers > 0 and secondHighestNrOfCards[0] != 'J':
                cardCount[secondHighestNrOfCards[0]] = cardCount[secondHighestNrOfCards[0]] + nrJokers
            for card in cards:
                cardTuples.append((card, cardCount[card]))
            
            # calculate type
            cardTuples = sorted(cardTuples, key=lambda x: x[1])
            highestNrOfCards = cardTuples[-1]
            secondHighestNrOfCards = cardTuples[-2]
            if highestNrOfCards[1] == 5:
                typeMap['five'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 4:
                typeMap['four'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 3 and secondHighestNrOfCards[1] == 2:
                typeMap['fullHouse'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 3:
                typeMap['three'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 2 and secondHighestNrOfCards[1] == 2:
                typeMap['twoPair'].append((hand, int(bid)))
            elif highestNrOfCards[1] == 2:
                typeMap['onePair'].append((hand, int(bid)))
            else:
                typeMap['highCard'].append((hand, int(bid)))
        
        # calculate winnings
        for t in types:
            sortedList = sorted(typeMap[t], key=lambda x: (cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]), cards.index(x[0][4])))
            for handTuple in sortedList:
                result += handTuple[1] * rank
                rank -= 1
        print(result)


if __name__ == '__main__':
    partTwo()
