from random import shuffle

# The program written here is the code required to play blackjack.

# The following line creates a card class used to hold details of
class Card:
# The following line creates and holds the suit details of the cards in the deck.
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

# The following line creates and holds the value details of the cards in the deck.
    values = ["2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

# The following function initializes values.
    def __init__(self, v, s):
        self.value = v
        self.suit = s

# The following function tests which of two cards is smaller.
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
# The following function tests which of two cards is larger.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v

# The following line creates the class that holds the status of and implements actions upon the deck of cards.
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# The following line creates the class that holds the details of the players.
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

# The following line creates the class that holds the details of the game of Blackjack itself.
class Game:
# The following function takes in the names of the two Blackjack players, shuffles the deck, and assigns the names to the players.
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
# The following function returns the winning player within a string printed to the console output.
    def wins(self, winner):
        w = "{} is the winner"
        w = w.format(winner)
        print(w)
# The following function returns to the console output the string that explains that the game drew.
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)
# The following function runs the game.
    def play_game(self):
        cards = self.deck.cards
        print("Let the games begin!")
# The following loop provides users with more than 2 cards the option to stop adding cards.
        while len(cards) >= 2:
            m = "Press q to stop adding card. Press any " + \
                "key to play:"
            response = input(m)
# The following if-statement stops adding cards if the user selected 'q'
            if response == 'q':
                break
# The following lines adjust the details of the players and account for the cards drawn without replacement from the deck.
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
# The following lines define the winner according to the rules of Blackjack.
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
# The winner is recorded and the information is relayed to the console output.
        win = self.winner(self.p1,
                         self.p2)
        print("The game is over.{} wins"
              .format(win))
# The following function returns the winner of the game or returns the message that the game was a tie.
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "The game tied!"
# The following lines run the game.
game = Game()
game.play_game()
