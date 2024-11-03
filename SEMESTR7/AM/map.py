from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

GRAPHHOPPER_API_KEY = "51117b28-cce9-416a-a23d-d72f25d505ae"
GRAPHHOPPER_ROUTE_API_URL = "https://graphhopper.com/api/1/route"
GRAPHHOPPER_GEOCODE_API_URL = "https://graphhopper.com/api/1/geocode"

def geocode_address(address):
    response = requests.get(GRAPHHOPPER_GEOCODE_API_URL, params={
        'q': address,
        'locale': 'en',
        'limit': 1,
        'provider': 'default',
        'key': GRAPHHOPPER_API_KEY
    })
    
    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            return data['hits'][0]["point"]["lat"], data['hits'][0]["point"]["lng"]
    return None, None

def get_route(start_coords, end_coords):
    params = {
        'point': [start_coords, end_coords],
        'profile': 'car',
        'locale': 'en',
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_route', methods=['POST'])
def route():
    data = request.json
    start_address = data['start_address']
    end_address = data['end_address']
    
    # Geocode addresses using GraphHopper Geocoding API
    start_lat, start_lng = geocode_address(start_address)
    end_lat, end_lng = geocode_address(end_address)
    
    if start_lat and start_lng and end_lat and end_lng:
        start_coords = f"{start_lat},{start_lng}"
        end_coords = f"{end_lat},{end_lng}"
        route_coordinates = get_route(start_coords, end_coords)
        return jsonify(route_coordinates)
    else:
        return jsonify({"error": "Could not geocode addresses"}), 400

if __name__ == '__main__':
    app.run(debug=True)
