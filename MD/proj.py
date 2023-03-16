from random import randint
from flask import Flask, request

from vertex import Vertex

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
            else:
                r = randint(0,100)
                if r <= p:
                    row.append(1)
                else:
                    row.append(0)
        A.append(row)
    return A

def create_vertices(matrix: list[int]) -> list[Vertex]:
    """Creates list of vertices and based on given argument [matrix] assigns it's neighbours indexes"""
    Vertices: list[Vertex] = []
    for v in range(n):
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
    n = int(request.args.get('n', 1))
    A = generate_matrix(n, 0.6)
    Vertices = create_vertices(A)
    circle_html = """
    <form method="POST" action="/process-form">
        <label for="n">Enter something:</label>
        <input type="text" name="n" id="n">
        <input type="submit" value="Submit">
    </form>
    <form method="POST" action="/process-form">
        <label for="p">Enter something:</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    return circle_html

@app.route('/process-form', methods=['POST'])
def process_form():
    n = request.form['n']
    p = request.form['p']
    # do something with input_value
    circle_html = """
    <form method="POST" action="/process-form">
        <label for="n">Enter something:</label>
        <input type="text" name="n" id="n">
        <input type="submit" value="Submit">
    </form>
    <form method="POST" action="/process-form">
        <label for="p">Enter something:</label>
        <input type="text" name="p" id="p">
        <input type="submit" value="Submit">
    </form>
"""
    for v in Vertices:
        circle_html += f"""
            <div class="circle">{v.index+1}</div>

            <style>
            .circle {{
              width: 100px;
              height: 100px;
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
    return 'Input value: ' + input_value

if __name__ == "__main__":
    n = int(input("Matrix size: "))
    p = float(input("Chance: "))
    A = generate_matrix(n, p)
    Vertices = create_vertices(A)
    save_as_txt(A)
    for i in A:
        print(i)
    for i in range(n):
        print("Vertex:", i)
        print(Vertices[i].neighbours)
        print(Vertices[i].degrees)
        print("=====================")
    
    app.run()


