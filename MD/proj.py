from random import randint

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


def generate_main_path(vertices: list[Vertex], start: int) -> list[int]:
    """Generates a path of vertices starting from the given vertex"""
    path = [start]
    current = start
    vertices[current].flag = 1
    path = [start]
    while any(vertices[vertex].flag == 0 for vertex in vertices[current].neighbours):
        for neighbour in vertices[current].neighbours:
            if vertices[neighbour].flag == 0:
                disable_neighbours(current)
                current = neighbour
                path.append(current)
    return path


def generate_paths(main_path) -> list[list[int]]:
    print(main_path)
    paths: list[list[int]] = [main_path]
    for i in range(1, len(main_path) + 1):
        enable_path(paths)
        path: list[int] = []
        if any(
            Vertices[vertex].flag == 0 for vertex in Vertices[main_path[-i]].neighbours
        ):
            print(paths)
            for v in Vertices[main_path[-i]].neighbours:
                if Vertices[v].flag == 0 and main_path[-i] != main_path[0]:
                    if Vertices[main_path[-i - 1]].index not in Vertices[v].neighbours:
                        temp_path = generate_main_path(Vertices, v)
                        print(temp_path)
                        path = main_path[0 : len(main_path) - i + 1]
                        for e in temp_path:
                            path.append(e)
                    paths.append(path)
                elif main_path[-i] != main_path[0]:
                    path = generate_main_path(Vertices, main_path[0])
    return paths


def disable_neighbours(vertex: int) -> None:
    for neighbour in Vertices[vertex].neighbours:
        Vertices[neighbour].flag = 1


def enable_path(exception: list[list[int]]):
    flat_list = [item for sublist in exception for item in sublist]
    for vertex in Vertices:
        if vertex.index not in flat_list:
            vertex.flag = 0


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
    p = 0.6
    s = 1
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
    main_path = generate_main_path(Vertices, s)
    paths = generate_paths(main_path)
    print(paths)
    deg = {}
    for v in Vertices:
        deg[("index: " + str(v.index))] = v.degrees
    # print("Vertices:", deg)
    # print("Vertices sorted:", sorted(deg.items(), reverse=True, key=lambda x: x[1]))
    save_as_txt(A, deg)
    # for i in A:
    #    print(i)
    for i in range(n):
        print("Vertex:", i)
        print(Vertices[i].neighbours)
        print(Vertices[i].degrees)
        print("=====================")
