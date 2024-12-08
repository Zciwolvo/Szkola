from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
import json
from geopy.distance import geodesic
import requests
from datetime import datetime

app = Flask(__name__)

GRAPHHOPPER_API_KEY = "51117b28-cce9-416a-a23d-d72f25d505ae"
GRAPHHOPPER_ROUTE_API_URL = "https://graphhopper.com/api/1/route"

# Load locations
with open("locations.json", "r") as file:
    locations = json.load(file)

# Load scores
try:
    with open("scores.json", "r") as file:
        scores = json.load(file)
except FileNotFoundError:
    scores = {}

def save_scores():
    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)

def find_nearest_location(user_coords, visited_routes):
    nearest_location = None
    min_distance = float("inf")

    for location in locations:
        if location["name"] in visited_routes:
            continue  # Skip already visited locations

        location_coords = (location["latitude"], location["longitude"])
        distance = geodesic(user_coords, location_coords).meters

        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location

@app.route('/', methods=['GET', 'POST'])
def index():
    username = request.cookies.get('username')
    if username:
        return redirect(url_for('game'))  # Redirect to game if username exists

    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return render_template('index.html', error="Username is required")

        # Create user entry if not exists
        if username not in scores:
            scores[username] = {}

        # Start a new game attempt
        new_attempt_timestamp = datetime.utcnow().isoformat()
        scores[username][new_attempt_timestamp] = {
            "visited_routes": [],
            "score": 0
        }
        #save_scores()

        response = make_response(redirect(url_for('game')))
        response.set_cookie('username', username)  # Save username in cookies
        response.set_cookie('current_attempt', new_attempt_timestamp)  # Save current attempt timestamp
        return response

    return render_template('index.html')

@app.route('/game', methods=['GET'])
def game():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))  # Ensure username is set before accessing the game

    current_attempt = request.cookies.get('current_attempt')
    if not current_attempt:
        # If no current attempt, start a new game
        new_attempt_timestamp = datetime.utcnow().isoformat()
        scores[username][new_attempt_timestamp] = {
            "visited_routes": [],
            "score": 0
        }
        #save_scores()

        response = make_response(redirect(url_for('game')))
        response.set_cookie('current_attempt', new_attempt_timestamp)  # Save current attempt timestamp
        return response

    return render_template('game.html')

def get_route(start_coords, end_coords):
    params = {
        'point': [start_coords, end_coords],
        'profile': 'foot',
        'locale': 'pl',
        'points_encoded': 'false',
        'instructions': 'true',
        'key': GRAPHHOPPER_API_KEY
    }
    response = requests.get(GRAPHHOPPER_ROUTE_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "paths" in data:
            return data["paths"][0]["points"]["coordinates"]
    return []

@app.route('/get_route', methods=['POST'])
def route():
    data = request.json
    start_address = data['start_address'].split(",")
    start_address = [float(address) for address in start_address]
    end_address = data['end_address'].split(",")
    end_address = [float(address) for address in end_address]
    start_lat, start_lng = start_address[0], start_address[1]
    end_lat, end_lng = end_address[0], end_address[1]
    if start_lat and start_lng and end_lat and end_lng:
        start_coords = f"{start_lat},{start_lng}"
        end_coords = f"{end_lat},{end_lng}"
        route_coordinates = get_route(start_coords, end_coords)
        return jsonify(route_coordinates)
    else:
        return jsonify({"error": "Could not geocode addresses"}), 400


@app.route('/check_location', methods=['POST'])
def check_location():
    username = request.cookies.get('username')
    current_attempt = request.cookies.get('current_attempt')
    
    # Validate user and current attempt
    if not username or not current_attempt:
        return jsonify({"error": "User not logged in or no active attempt"}), 401

    # Check if user exists in scores
    if username not in scores:
        scores[username] = {}

    # Check if the current attempt exists for the user
    if current_attempt not in scores[username]:
        scores[username][current_attempt] = {
            "visited_routes": [],
            "score": 0
        }
        #save_scores()

    # Load user and attempt data
    user_score_data = scores[username][current_attempt]
    visited_routes = user_score_data["visited_routes"]

    user_data = request.json
    user_coords = (user_data["latitude"], user_data["longitude"])

    # Find the nearest location that hasn't been visited yet
    nearest_location = find_nearest_location(user_coords, visited_routes)
    if nearest_location:
        visited_routes.append(nearest_location["name"])  # Mark location as visited

        # Check if all routes are completed
        if len(visited_routes) == len(locations):
            end_time = datetime.utcnow()
            start_time = datetime.fromisoformat(current_attempt)
            elapsed_time = (end_time - start_time).total_seconds()  # Time in seconds

            scores[username][current_attempt] = {
                "visited_routes": visited_routes,
                "score": len(visited_routes),
                "elapsed_time": elapsed_time
            }
            #save_scores()
            return jsonify({
                "message": "Congratulations! You've completed all routes.",
                "score": len(visited_routes),
                "elapsed_time": elapsed_time,
                "place_name": nearest_location["name"],
                "description": nearest_location["description"],
                "quiz": nearest_location["quiz"],
                "latitude": nearest_location["latitude"],
                "longitude": nearest_location["longitude"],
                "game_over": True  # Indicate that the game is over
            })

        # Save progress
        scores[username][current_attempt] = {
            "visited_routes": visited_routes,
            "score": len(visited_routes)
        }
        #save_scores()

        return jsonify({
            "place_name": nearest_location["name"],
            "description": nearest_location["description"],
            "quiz": nearest_location["quiz"],
            "latitude": nearest_location["latitude"],
            "longitude": nearest_location["longitude"],
            "game_over": False  # Indicate that the game is ongoing
        })
    else:
        # No more locations to visit
        return jsonify({"message": "No nearby locations or all visited. Game over.", "game_over": True}), 404


if __name__ == '__main__':
    app.run(debug=True)
