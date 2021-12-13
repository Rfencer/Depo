class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __str__(self):
        return str(self.num)

    def __sub__(self, other):
        if self.num > other.num:
            return Cell(self.num + other.num)
        else:
            print("Operation not possible")

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        if other.num == 0:
            print("Operation not possible")
        else:
            return Cell(round(self.num // other.num))

    def __floordiv__(self, other):
        return self/other

    def make_order(self, order):
        rows = self.num//order
        return '\n'.join(['*'*order for i in range(rows)])+'\n'+'*'*(self.num-rows*order)



cell1 = Cell(27)
cell2 = Cell(9)
cell3 = cell1 / cell2
print(cell3)
print(cell1.make_order(5))