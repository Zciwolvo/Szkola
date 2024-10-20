import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
from plyer import gps
import random

class RouteApp(App):
    def build(self):
        self.user_id = 'user123'  # Simple user ID
        layout = BoxLayout(orientation='vertical')

        self.mapview = MapView(zoom=15, lat=0, lon=0)
        layout.add_widget(self.mapview)

        self.status_label = Label(text="Choose a route...")
        layout.add_widget(self.status_label)

        # Button to fetch and display a random route
        self.route_button = Button(text="Select Random Route")
        self.route_button.bind(on_press=self.get_random_route)
        layout.add_widget(self.route_button)

        # Start GPS tracking button
        self.start_button = Button(text="Start Tracking")
        self.start_button.bind(on_press=self.start_tracking)
        layout.add_widget(self.start_button)

        return layout

    def get_random_route(self, instance):
        # Fetch routes from the server
        response = requests.get('http://127.0.0.1:5000/routes')
        routes = response.json()
        
        # Select random route
        route = random.choice(routes)
        self.selected_route = requests.get(f"http://127.0.0.1:5000/route?name={route['name']}").json()

        # Show route description
        self.status_label.text = f"Route: {self.selected_route['description']}"

    def start_tracking(self, instance):
        # Start GPS tracking
        try:
            gps.configure(on_location=self.update_location)
            gps.start(minTime=1000, minDistance=1)
            self.status_label.text = "Tracking GPS..."
        except NotImplementedError:
            # PC mode: simulate a nearby location
            self.simulate_location()

    def simulate_location(self):
        # Simulate location when GPS isn't supported
        first_point = self.selected_route['points'][0]
        self.update_location(lat=first_point['lat'] + 0.001, lon=first_point['lon'] + 0.001)

    def update_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')

        first_point = self.selected_route['points'][0]
        point_lat = first_point['lat']
        point_lon = first_point['lon']

        # Check if user arrived at the point
        if abs(lat - point_lat) < 0.001 and abs(lon - point_lon) < 0.001:
            self.status_label.text = first_point['description']
            # Display media or extra material
            media_url = first_point['media']
            print(f"Watch this video: {media_url}")

            # Quiz: Ask user a question
            question = first_point['quiz']['question']
            options = first_point['quiz']['options']
            self.status_label.text = f"Quiz: {question} Options: {options}"

            # Simulate answering a quiz
            user_answer = options[0]  # Assume user picks first option
            if user_answer == first_point['quiz']['answer']:
                self.submit_quiz_score(1)
            else:
                self.submit_quiz_score(0)
        else:
            self.status_label.text = f"Current location: {lat}, {lon}"

    def submit_quiz_score(self, score):
        # Submit quiz score to the server
        response = requests.post('http://127.0.0.1:5000/quiz', json={'user_id': self.user_id, 'score': score})
        result = response.json()
        print(f"Score updated. Total score: {result['total_score']}")

if __name__ == "__main__":
    RouteApp().run()
