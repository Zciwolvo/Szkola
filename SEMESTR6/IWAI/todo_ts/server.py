from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://skapiec.4ju5ocq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Skapiec"
client = MongoClient(uri, tls=True, tlsCertificateKeyFile='./certs/X509-cert-3621885173140152299.pem')
db = client['todo']
collection = db['task']

@app.route('/api/todos', methods=['GET'])
def get_todos():
    daily_todos = list(collection.find({"isDaily": True}))
    single_time_todos = list(collection.find({"isDaily": False}))
    for todo in daily_todos + single_time_todos:
        todo['id'] = str(todo['_id'])
        del todo['_id']
    return jsonify({"dailyTodos": daily_todos, "singleTimeTodos": single_time_todos})


@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    new_todo = data['newTodo']
    new_todo['isDaily'] = data['isDaily']
    new_todo['done'] = False
    result = collection.insert_one(new_todo)
    new_todo['id'] = str(result.inserted_id)
    return jsonify(new_todo)

@app.route('/api/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    result = collection.delete_one({"_id": ObjectId(todo_id)})
    return jsonify({"success": result.deleted_count > 0})

@app.route('/api/todos/<todo_id>', methods=['PUT'])
def update_todo_status(todo_id):
    data = request.json
    result = collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"done": data['done']}})
    return jsonify({"success": result.modified_count > 0})

if __name__ == '__main__':
    app.run(debug=True)
