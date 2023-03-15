

class Vertex:
    def __init__(self, index) -> None:
        self.index = index
        self.neighbours = []
        self.degrees = 0

    
    def get_neighbours(self, matrix: list[int]) -> None:
        for i in range(len(matrix)):
            if (matrix[self.index][i]) == 1 or (matrix[i][self.index]):
                self.neighbours.append(i)
        self.degrees = len(self.neighbours)