from random import randint

from vertex import Vertex

#TODO: Graphical desktop interface using Tkinter or web interface using Django, PyScript or niceGUI

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

def create_vertices(matrix: list[int]) -> list[Vertex]:
    """Creates list of vertices and based on given argument [matrix] assigns it's neighbours indexes"""
    Vertices: list[Vertex] = []
    for v in range(n):
        Vertices.append(Vertex(v))
        Vertices[v].get_neighbours(matrix)
    return Vertices

def save_as_txt(matrix: list[int], deg: dict) -> None:
    """Generates txt filled based on given matrix"""
    with open("./Szkola/MD/output.txt", "w") as f:
        f.write("") #Clears file
    with open("./Szkola/MD/output.txt", "a") as f:
        for a in matrix:
            f.writelines(str(a))
            f.write("\n")
        f.write(str(deg))
        f.write("\n")
        f.write(str(sorted(deg.items(), reverse=True, key=lambda x: x[1])))
    


if __name__ == "__main__":
    n = int(input("Matrix size: "))
    p = float(input("Chance: "))
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    deg = {}
    for v in Vertices:
        deg[("index: " + str(v.index))] = v.degrees
    print("Edges:", deg)
    print("Edges sorted:", sorted(deg.items(), reverse=True, key=lambda x: x[1]))
    save_as_txt(A, deg)
    for i in A:
        print(i)
    for i in range(n):
        print("Vertex:", i)
        print(Vertices[i].neighbours)
        print(Vertices[i].degrees)
        print("=====================")
