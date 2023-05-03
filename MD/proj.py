from random import randint
from collections import deque

from vertex import Vertex

# TODO: Graphical web interface using Flask


def generate_matrix(n: int, p: float) -> list[int]:
    """Generates [n]x[n] matrix with [p] chance of its elements being 1 and (1-[p]) chance of it being 0

    Returns:
        list[int]: Matrix describing graph
    """
    A = []
    p = p * 100
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            elif j > i:
                r = randint(0, 100)
                if r <= p:
                    row.append(1)
                else:
                    row.append(0)
            else:
                row.append(A[j][i])
        A.append(row)
    return A



def generate_path(vertices: list[Vertex], source: int, destination: int, path=[]) -> list[int]:
    queue = deque([[source]])
    visited = set([source])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == destination:
            return path

        for neighbor in vertices[node].neighbours:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

def generate_paths(vertices: list[Vertex], source):
    paths = []
    for vertex in vertices:
        if vertex.final == True:
            paths.append(generate_path(vertices, source, vertex.index))
    return paths

def generate_neighbours(vertices: list[Vertex]):
    neighbours = {}
    for i in range(len(vertices)):
        neighbours[i] = vertices[i].neighbours
    return neighbours

def generate_tree(vertices: list[Vertex], source: int):
    neighbours = generate_neighbours(vertices)
    tree = {0: [source]}
    curr = source
    i = 1
    for v in vertices[curr].neighbours:
        tree[i] += neighbours[curr]

    return tree
    
     



def create_vertices(matrix: list[int]) -> list[Vertex]:
    """Creates list of vertices and based on given argument [matrix] assigns it's neighbours indexes"""
    Vertices: list[Vertex] = []
    for v in range(n):
        Vertices.append(Vertex(v))
        Vertices[v].get_neighbours(matrix)
    return Vertices


def save_as_txt(matrix: list[int], deg: dict) -> None:
    """Generates txt filled based on given matrix"""
    with open("./output.txt", "w") as f:
        f.write("")  # Clears file
    with open("./output.txt", "a") as f:
        for a in matrix:
            f.writelines(str(a))
            f.write("\n")
        f.write(str(deg))
        f.write("\n")
        f.write(str(sorted(deg.items(), reverse=True, key=lambda x: x[1])))


if __name__ == "__main__":
    # n = int(input("Matrix size: "))
    # p = float(input("Chance: "))
    # s = int(input("Choose initial point: "))
    n = 6
    p = 0.4
    s = 0
    A = generate_matrix(n, p)
    A = [
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0],
    ]
    Vertices = create_vertices(A)

    paths = generate_paths(Vertices, s)
    print(paths)

    neigh = generate_neighbours(Vertices)
    print(neigh)



    #deg = {}
    #for v in Vertices:
    #    deg[("index: " + str(v.index))] = v.degrees
    # print("Vertices:", deg)
    # print("Vertices sorted:", sorted(deg.items(), reverse=True, key=lambda x: x[1]))
    #save_as_txt(A, deg)
    # for i in A:
    #    print(i)
    #for i in range(n):
    #    print("Vertex:", i)
    #   print(Vertices[i].neighbours)
    #    print(Vertices[i].degrees)
    #    print("=====================")
