import json
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated user progress storage
user_data = {}

# Load routes from a JSON file
def load_routes():
    with open('routes.json', 'r') as file:
        return json.load(file)

# Get random route
def get_random_route():
    routes = load_routes()
    return random.choice(routes)

@app.route('/routes', methods=['GET'])
def get_routes():
    # Get all routes for user to choose
    routes = load_routes()
    route_list = [{"name": route["name"], "description": route["description"]} for route in routes]
    return jsonify(route_list)

@app.route('/route', methods=['GET'])
def get_route():
    route_name = request.args.get('name')
    routes = load_routes()
    for route in routes:
        if route["name"] == route_name:
            return jsonify(route)
    return jsonify({"error": "Route not found"}), 404

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.get_json()
    user_id = data.get('user_id')
    score = data.get('score')
    
    # Save user progress
    if user_id not in user_data:
        user_data[user_id] = {'score': 0}
    
    user_data[user_id]['score'] += score
    
    return jsonify({"message": "Score updated", "total_score": user_data[user_id]['score']})

if __name__ == "__main__":
    app.run(debug=True)
