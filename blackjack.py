import re
import numpy as np
import random


class Deck:
    deck = (
        np.array(
            [
                [
                    "1C",
                    "2C",
                    "3C",
                    "4C",
                    "5C",
                    "6C",
                    "7C",
                    "8C",
                    "9C",
                    "10C",
                    "11C",
                    "12C",
                    "13C",
                ],
                [
                    "1D",
                    "2D",
                    "3D",
                    "4D",
                    "5D",
                    "6D",
                    "7D",
                    "8D",
                    "9D",
                    "10D",
                    "11D",
                    "12D",
                    "13D",
                ],
                [
                    "1H",
                    "2H",
                    "3H",
                    "4H",
                    "5H",
                    "6H",
                    "7H",
                    "8H",
                    "9H",
                    "10H",
                    "11H",
                    "12H",
                    "13H",
                ],
                [
                    "1P",
                    "2P",
                    "3P",
                    "4P",
                    "5P",
                    "6P",
                    "7P",
                    "8P",
                    "9P",
                    "10P",
                    "11P",
                    "12P",
                    "13P",
                ],
            ]
        )
        .flatten()
        .tolist()
    )

    def __init__(self):
        random.shuffle(self.deck)

    def getCard(self) -> str:
        return self.deck.pop()

    def getIniCards(self) -> list:
        return [self.getCard(), self.getCard()]


class PlayerCards:
    def __init__(self, cards: list):
        self.cards = cards
        self.sortCards()

    def getCardInteger(self, card: str) -> int:
        return int(re.findall("(\\d+|[A-Za-z]+)", card)[0])

    def addCard(self, card: str) -> None:
        self.cards.append(card)
        self.sortCards()

    def printCards(self) -> list:
        return self.cards

    def getCardsValue(self) -> int:
        value = 0
        for card in self.cards:
            cardV = self.getCardInteger(card)
            if 2 <= cardV <= 9:
                value += cardV
            elif 10 <= cardV:
                value += 10
            else:  # El As
                if (value + cardV) >= 21:
                    value += 1
                else:
                    value += 11
        return value

    def sortCards(self):
        self.cards.sort(key=self.getCardInteger, reverse=True)


deck = Deck()
playerCards = PlayerCards(["1C", "10P", "11C"])
print(playerCards.printCards())
print(playerCards.getCardsValue())
