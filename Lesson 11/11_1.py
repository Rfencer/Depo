import random


class Card:
    def __init__(self):
        self.num_list = []
        self.intervals = []
        for _ in range(3):
            line = random.sample([i for i in range(1, 91) if i not in self.num_list], k=5)
            line.sort()
            self.num_list.extend(line)
            intervals = random.sample([i for i in range(0, 9)], k=5)
            intervals.sort()
            self.intervals.extend(intervals)

    def cross_number(self, num):
        if num in self.num_list:
            index = self.num_list.index(num)
            self.num_list[index] = 'x'
            return 1
        else:
            return 0

    def __str__(self):
        return_list = []
        for i in range(0, 15, 5):
            rand_ints = ((k, v) for k, v in zip(self.intervals[i:i+5], self.num_list[i: i + 5]))
            return_line = [''] * 9
            for num in rand_ints:
                return_line[num[0]] = str(num[1])
            return_list.append(return_line)
        return '-----------------------------\n' + '\n'.join(('  '.join(x) for x in return_list)) + \
               '\n-----------------------------'


class Player():
    def __init__(self, name):
        self.name = name
        self.card = Card()
        self.score = 0

    def cross(self, num):
        while True:
            answer = input(f'Would you like to cross this number: {num}. Y/N\n')
            if answer not in ['Y', 'y', 'N', 'n']:
                print('Try again: Y/N')
                continue
            elif answer.capitalize() == 'Y':
                if self.card.cross_number(num) == 1:
                    self.score += 1
                    break
                else:
                    return 0
            else:
                return 'N'


class Computer(Player):
    def cross(self, num):
        if num in self.card.num_list:
            self.card.cross_number(num)
            self.score += 1
        else:
            return 'N'


class Game():
    def __init__(self, *players):
        self.pool_list = random.sample([i for i in range(1, 91)], k=90)
        while self.pool_list:
            number = self.pool_list.pop()
            for player in players:
                print(f'{player.name} Card: \n{player.card}')
                answer = player.cross(number)
                if answer == 'N' and number in player.card.num_list:
                    print(f'{player.name} has lost')
                    break
                elif answer == 0:
                    print(f'{player.name} has lost')
                    break
                else:
                    if player.score == 15:
                        print(f'{player.name} has won!')
                        break
            else:
                continue
            break


player1 = Player('Player')
computer = Computer('Computer')
game1 = Game(player1, computer)
