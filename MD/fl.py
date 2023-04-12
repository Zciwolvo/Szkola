from flask import Flask, render_template
from random import randint
from flVertex import Vertex

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
    vertices: list[Vertex] = []
    for v in range(len(matrix)):
        vertices.append(Vertex(v))
        vertices[v].get_neighbours(matrix)
    return vertices

@app.route('/')
def index():
    n = 10
    p = 0.5
    A = generate_matrix(n, p)
    vertices = [{'id': i} for i in range(n)]
    edges = [{'source': i, 'target': j} for i in range(n) for j in range(i+1, n) if A[i][j] == 1]
    return render_template('index.html', vertices=vertices, edges=edges)

if __name__ == '__main__':
    app.run(debug=True)