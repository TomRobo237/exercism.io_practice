class Matrix(object):
    def __init__(self, matrix_string):
        '''Split string into 2d list of intgers'''
        rows = matrix_string.split('\n')
        matrix = [x.split() for x in rows]
        self.matrix = [[int(y) for y in x] for x in matrix]

    def row(self, index):
        '''return row of 2d matrix as list'''
        return self.matrix[index - 1]

    def column(self, index):
        '''return column of 2d matrix as list'''
        return [self.matrix[x][index - 1] for x in range(0, len(self.matrix))]
