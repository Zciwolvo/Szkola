from random import randint

from vertex import Vertex

#TODO: Graphical web interface using Flask

def generate_matrix(n: int, p: float) -> list[int]:
    """Generates [n]x[n] matrix with [p] chance of its elements being 1 and (1-[p]) chance of it being 0

    Returns:
        list[int]: Matrix describing graph
    """
    A = []
    p = p*100
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            elif j > i:
                r = randint(0,100)
                if r <= p:
                    row.append(1)
                else:
                    row.append(0)
            else:
                row.append(A[j][i])
        A.append(row)
    return A

def generate_path(vertices: list[Vertex], start: int) -> list[int]:
    """Generates a path of vertices starting from the given vertex"""
    path = []
    visited = set()  # keep track of visited vertices
    stack = [start]  # initialize stack with starting vertex
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            path.append(v)
            stack.extend(vertices[v].neighbours)
    return path


def create_vertices(matrix: list[int]) -> list[Vertex]:
    """Creates list of vertices and based on given argument [matrix] assigns it's neighbours indexes"""
    Vertices: list[Vertex] = []
    for v in range(n):
        Vertices.append(Vertex(v))
        Vertices[v].get_neighbours(matrix)
    return Vertices

def save_as_txt(matrix: list[int], deg: dict) -> None:
    """Generates txt filled based on given matrix"""
    with open("./MD/output.txt", "w") as f:
        f.write("") #Clears file
    with open("./MD/output.txt", "a") as f:
        for a in matrix:
            f.writelines(str(a))
            f.write("\n")
        f.write(str(deg))
        f.write("\n")
        f.write(str(sorted(deg.items(), reverse=True, key=lambda x: x[1])))    

if __name__ == "__main__":
    #n = int(input("Matrix size: "))
    #p = float(input("Chance: "))
    #s = int(input("Choose initial point: "))
    n = 55
    p = 0.6
    s = 0
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    print(generate_path(Vertices, s))
    deg = {}
    for v in Vertices:
        deg[("index: " + str(v.index))] = v.degrees
    #print("Vertices:", deg)
    #print("Vertices sorted:", sorted(deg.items(), reverse=True, key=lambda x: x[1]))
    save_as_txt(A, deg)
    #for i in A:
    #    print(i)
    for i in range(n):
        print("Vertex:", i)
        print(Vertices[i].neighbours)
        print(Vertices[i].degrees)
        print("=====================")
