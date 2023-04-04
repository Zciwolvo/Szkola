from flask import Flask, render_template
from random import randint
from vertex import Vertex

app = Flask(__name__)

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

@app.route('/')
def index():
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    vertices = [{'id': v.index} for v in Vertices]
    edges = [{'source': v.index, 'target': n} for v in Vertices for n in v.neighbours]
    return render_template('index.html', vertices=vertices, edges=edges)

if __name__ == '__main__':
    n = 10
    p = 0.5
    app.run(debug=True)
