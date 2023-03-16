from random import randint
from flask import Flask, request

from vertex import Vertex

def generate_matrix(n: int, p: float) -> list[int]:
    """Generates [n]x[n] matrix with [p] chance of its elements being 1 and (1-[p]) chance of it being 0

    Returns:
        list[int]: Matrix describing graph
    """
    A = []
    p = int(p)*100
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
    circle_html = """
    <form method="POST" action="/process-form">
        <label for="n">Enter n:</label>
        <input type="text" name="n" id="n">
        <label for="p">Enter p:</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    return circle_html

@app.route('/process-form', methods=['POST'])
def process_form():
    n = request.form['n']
    p = request.form['p']
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    # do something with input_value
    circle_html = """
    <form method="POST" action="/process-form">
        <label for="n">Enter n:</label>
        <input type="text" name="n" id="n">
        <label for="p">Enter p:</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    for v in Vertices:
        circle_html += f"""
            <div class="circle">{v.index+1}</div>

            <style>
            .circle {{
              width: 50px;
              height: 50px;
              border-radius: 50%;
              background-color: blue;
              display: flex;
              justify-content: center;
              align-items: center;
              font-size: 32px;
              color: white;
              margin: 20px;
            }}
            </style>
        """
    return circle_html

if __name__ == "__main__":
   app.run()


