from random import randint
import math
from flask import Flask, request, render_template

from vertex import Vertex

def generate_matrix(n: int, p: float) -> list[int]:
    """Generates [n]x[n] matrix with [p] chance of its elements being 1 and (1-[p]) chance of it being 0

    Returns:
        list[int]: Matrix describing graph
    """
    A = []
    p = float(p)*100
    for i in range(int(n)):
        row = []
        for j in range(int(n)):
            if i == j:
                row.append(0)
            else:
                r = randint(0,100)
                if r <= int(p):
                    row.append(1)
                else:
                    row.append(0)
        A.append(row)
    return A

def create_vertices(matrix: list[int]) -> list[Vertex]:
    """Creates list of vertices and based on given argument [matrix] assigns it's neighbours indexes"""
    Vertices: list[Vertex] = []
    for v in range(len(matrix)):
        Vertices.append(Vertex(v))
        Vertices[v].get_neighbours(matrix)
    return Vertices

def save_as_txt(matrix: list[int]) -> None:
    """Generates txt filled based on given matrix"""
    with open("./output.txt", "w") as f:
        f.write("") #Clears file
    with open("./output.txt", "a") as f:
        for a in matrix:
            f.writelines(str(a))
            f.write("\n")

app = Flask(__name__)

@app.route('/')
def home():
    input_settings = """
    <form method="POST" action="/process-settings">
        <label for="n">Enter number of edges 'n':</label>
        <input type="text" name="n" id="n">
        <label for="p">Enter probability 'p':</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    return input_settings

@app.route('/process-settings', methods=['POST'])
def process_form():
    n = int(request.form['n'])
    p = float(request.form['p'])
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    angles = [360/n*i for i in range(n)]
    coordinates = [(50 + 40*math.cos(math.radians(angle)), 50 + 40*math.sin(math.radians(angle))) for angle in angles]
    
    # do something with input_value
    circle_html = """
    <form method="POST" action="/process-settings">
        <label for="n">Enter number of edges 'n':</label>
        <input type="text" name="n" id="n">
        <label for="p">Enter probability 'p':</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    circle_html += render_template('body.html', n=n, coordinates=coordinates)
    return circle_html

if __name__ == "__main__":
   app.run()


