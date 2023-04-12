class Vertex:
    def __init__(self, index):
        self.index = index
        self.neighbours = set()
        
    def add_neighbour(self, v):
        self.neighbours.add(v)
        
    def get_neighbours(self, matrix):
        for i, weight in enumerate(matrix[self.index]):
            if weight == 1:
                self.add_neighbour(i)