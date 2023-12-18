import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Function to generate the quadratic equation
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Function to plot the quadratic function
def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = quadratic_function(x, a, b, c)
    
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Quadratic Function')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Create a tkinter window
root = tk.Tk()
root.title("Quadratic Function Plotter")

# Function to handle button click event
def plot():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    plot_quadratic(a, b, c)

# Create labels and entry fields for coefficients a, b, and c
label_a = tk.Label(root, text="Enter coefficient a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Enter coefficient b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Enter coefficient c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

# Button to plot the quadratic function
plot_button = tk.Button(root, text="Plot", command=plot)
plot_button.pack()

root.mainloop()
