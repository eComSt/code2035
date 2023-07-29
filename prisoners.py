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


class Detective(player):
    def step(self):
        ans= [True,False,True,True]
        if len(self.history)<4: 
            return ans[len(self.history)]
        else:
            return False if all(self.history[:4]) else self.history[-1]


class Mirror(player):
    def __init__(self,model):
        super().__init__(model)
        self.matches = 0 # счетчик матчей
    def step(self):
        #self.matches += 1 # можно раскомментить и закомментить счётчик вконце, чтобы посмотреть на другой результат 
        if not self.history: return True
        elif self.history[-1]==True and self.matches%2==0: return False
        elif self.history[-1]==True and self.matches%2!=0: return True
        elif self.history[-1]==False and self.matches%2==0: return True
        elif self.history[-1]==False and self.matches%2!=0: return False
        self.matches += 1

class Game(object):
    def __init__(self,mathes=1000):
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
g.play(Mirror("Mirror"),Copycat("Copycat"))
print(g.reg)