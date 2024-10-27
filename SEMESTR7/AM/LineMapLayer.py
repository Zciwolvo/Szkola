from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy_garden.mapview import MapLayer

class LineMapLayer(MapLayer):
    def __init__(self, mapview, points=[], **kwargs):
        super().__init__(**kwargs)
        self.mapview = mapview  # Store the reference to the MapView
        self.points = points  # List of (lat, lon) points to draw
        self.canvas_layer = Widget()  # Widget to manage the canvas
        self.add_widget(self.canvas_layer)

    def set_points(self, points):
        # Update the list of points and redraw the line
        self.points = points
        self.redraw()

    def redraw(self):
        # Clear previous drawings and draw the new line
        self.canvas_layer.canvas.clear()
        if not self.points or len(self.points) < 2:
            return

        with self.canvas_layer.canvas:
            Color(0, 0, 1, 1)  # Blue color for the route line
            line_points = []
            for lat, lon in self.points:
                x, y = self.mapview.get_window_xy_from(lat, lon, self.mapview.zoom)
                line_points.extend([x, y])
            
            Line(points=line_points, width=2)  # Draw the line
