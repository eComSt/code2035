from collections import Counter

class player:
    def __init__(self,model):
        self.model = model
        self.history = []

class Cheater(player):
    def step(self):
        return False

class Cooperator(player):
    def step(self):
        return True

class Copycat(player):
    def step(self):
        return True if not self.history else self.history[-1]


class Game(object):
    def __init__(self,mathes=10):
        self.mathes=mathes
        self.reg = Counter()

    def play(self,player1,player2):
        for _ in range(self.mathes):
            ans1 = player1.step()
            ans2 = player2.step()
            if ans1 and ans2:
                self.reg[player1.model]+=2
                self.reg[player2.model]+=2
            elif ans1 and not ans2:
                self.reg[player1.model]-=1
                self.reg[player2.model]+=3
            if not ans1 and ans2:
                self.reg[player2.model]-=1
                self.reg[player1.model]+=3
            player1.history.append(ans2)
            player2.history.append(ans1)
        player1.history = []
        player2.history = []


g = Game()
g.play(Cooperator("Cheater"),Copycat("Copycat"))
print(g.reg)