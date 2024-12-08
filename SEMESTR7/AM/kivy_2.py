from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests
from webview import WebView  # Import the Android WebView

# Replace with your OpenRouteService API key
API_KEY = 'YOUR_OPENROUTESERVICE_API_KEY'

# Function to get the route URL from OpenRouteService
def get_route_url(start_lat, start_lon, end_lat, end_lon):
    url = f"https://api.openrouteservice.org/v2/directions/foot-walking?api_key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    params = {
        "coordinates": [[start_lon, start_lat], [end_lon, end_lat]],
        "instructions": False,
    }
    response = requests.post(url, json=params, headers=headers)
    data = response.json()

    # Extracting the geometry for the route
    if 'routes' in data:
        geometry = data['routes'][0]['geometry']
        map_url = f"https://maps.openrouteservice.org/directions?n1={start_lat}&n2={start_lon}&n3=15&b=0&c=0&k1=en-US&k2=km&g1={geometry}"
        return map_url
    else:
        return None

# Kivy layout definition
Builder.load_string("""
<MyWebView>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Target Location"
            size_hint_y: 0.1
        TextInput:
            id: lat_input
            hint_text: "Enter Target Latitude"
            size_hint_y: 0.1
        TextInput:
            id: lon_input
            hint_text: "Enter Target Longitude"
            size_hint_y: 0.1
        Button:
            text: "Get Route"
            size_hint_y: 0.2
            on_press: root.get_route()
""")

class MyWebView(MDScreen):
    def get_route(self):
        try:
            # Get user input for target location
            end_lat = float(self.ids.lat_input.text)
            end_lon = float(self.ids.lon_input.text)

            # Example coordinates for the user's location (replace with actual GPS data if available)
            start_lat, start_lon = 37.7749, -122.4194  # Example coordinates (San Francisco, CA)

            # Get route URL
            route_url = get_route_url(start_lat, start_lon, end_lat, end_lon)
            if route_url:
                # Open the WebView with the generated route URL
                WebView(route_url)
            else:
                print("Could not find route.")
        except ValueError:
            print("Invalid input. Enter valid coordinates.")

class MyWebApp(MDApp):
    def build(self):
        return MyWebView()

if __name__ == "__main__":
    MyWebApp().run()
