from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from webview import WebView  # Import from webview-android

# Define the Kivy language string for UI
KV = """
<MyWebView>:
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Route Finder"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10

        MDFlatButton:
            text: "Open Route Finder"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: root.open_webview()
"""

class MyWebView(MDScreen):
    def open_webview(self):
        # Open WebView with the URL of the Flask app
        WebView("http://127.0.0.1:5000")  # Replace with your Flask app URL or public IP

class MyWebApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyWebApp().run()
