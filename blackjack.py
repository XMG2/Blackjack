import random
import re
from enum import Enum, auto

import numpy as np


class Actions(Enum):
    HIT = auto()
    STAND = auto()


class Deck:
    posible_decks = (
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
        random.shuffle(self.posible_decks)

    def get_card(self) -> str:
        return self.posible_decks.pop()

    def get_ini_cards(self) -> list:
        return [self.get_card(), self.get_card()]


class Player:
    def __init__(self, cards: list):
        self.cards = cards
        self.sort_cards()

    def get_card_integer(self, card: str) -> int:
        return int(re.findall("(\\d+|[A-Za-z]+)", card)[0])

    def add_card(self, card: str) -> None:
        self.cards.append(card)
        self.sort_cards()

    def print_cards(self) -> list:
        return self.cards

    def get_cards_value(self) -> int:
        value = 0
        for card in self.cards:
            card_value = self.get_card_integer(card)
            if 2 <= card_value <= 9:
                value += card_value
            elif 10 <= card_value:
                value += 10
            else:  # El As
                if (value + card_value) >= 21:
                    value += 1
                else:
                    value += 11
        return value

    def sort_cards(self):
        self.cards.sort(key=self.get_card_integer, reverse=True)


class Dealer(Player):
    def dealer_play(self, deck: Deck):
        while self.get_cards_value() < 17:
            card = deck.get_card()
            print(f"Dealers new card {card}")
            self.add_card(card)
            print(f"Dealers new value {self.get_cards_value()}")


class Game:
    THUMBS_UP = """
    ░░░░░░░░░░░░░░░░░░░░░░█████████
    ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
    ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
    ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
    ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
    ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
    ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
    ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
    ░░████████████░░░█████████████████
    """
    LOSER = """
    888                                
    888                                
    888                                
    888 .d88b. .d8888b  .d88b. 888d888 
    888d88""88b88K     d8P  Y8b888P"   
    888888  888"Y8888b.88888888888     
    888Y88..88P     X88Y8b.    888     
    888 "Y88P"  88888P' "Y8888 888
    """

    def __init__(self):
        self.deck = Deck()

    def play(self):
        print("Game starts")
        player = Player(self.deck.get_ini_cards())
        dealer = Dealer(self.deck.get_ini_cards())
        print(f"Your cards{player.print_cards()}\nValue: {player.get_cards_value()}")
        print(f"Dealers cards{dealer.print_cards()}\nValue: {dealer.get_cards_value()}")
        turn_pass = True
        while player.get_cards_value() <= 21 and turn_pass:
            action = self.hit_or_stand()
            if action == Actions.STAND:
                turn_pass = False
            else:
                self.get_new_card(player)
        if self.over_21(player):
            print("Sry over 21")
            self.print_loser()
        else:
            print(f"You have {player.get_cards_value()}")
            dealer.dealer_play(self.deck)
            if self.over_21(dealer) or self.less_value(player, dealer):
                self.print_win()
            else:
                self.print_loser()

    def hit_or_stand(self):
        more = "_"
        while more != "Y" and more != "N":
            more = str(input("Do you want more cards? (Y/N): ").upper())
        if more == "N":
            return Actions.STAND
        else:
            return Actions.HIT

    def get_new_card(self, player):
        card = self.deck.get_card()
        print(f"New card {card}")
        player.add_card(card)
        print(f"New value {player.get_cards_value()}")

    def over_21(self, player):
        return player.get_cards_value() > 21

    def less_value(self, player, dealer):
        return dealer.get_cards_value() < player.get_cards_value()

    def print_win(self):
        print("You won")
        print(self.THUMBS_UP)

    def print_loser(self):
        print("You are a LOSER")
        print(self.LOSER)


game = Game()
game.play()
