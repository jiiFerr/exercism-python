
class Matrix:

    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")

        for i in range(len(self.rows)):
            cols = [int(j) for j in self.rows[i].split(" ")]
            self.rows[i] = cols

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.rows]
