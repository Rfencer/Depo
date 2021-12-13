class Matrix:

    def __init__(self, input_list):
        self.matrix = input_list

    def __str__(self):
        return '\n'.join((' '.join(map(str, x)) for x in self.matrix))

    def __add__(self, m2):
        new_m = []
        if len(self.matrix) == len(m2.matrix) and len(self.matrix[0]) == len(m2.matrix[0]):
            for line1, line2 in zip(self.matrix, m2.matrix):
                new_m.append([x + y for x, y in zip(line1, line2)])
            return Matrix(new_m)
        else:
            return 'Addition not possible'


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[2, 5, 8], [3, 8, 1], [6, 3, 4]])
matrix3 = Matrix([[2, 5, 8], [3, 8, 1]])

print(matrix1+matrix2)
print(matrix1 + matrix3)