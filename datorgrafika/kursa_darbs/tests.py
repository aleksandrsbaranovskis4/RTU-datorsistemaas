import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class BezierAnimation:
    def __init__(self, control_points, object_position, object_size):
        self.control_points = np.array(control_points)
        self.object_position = np.array(object_position)
        self.object_size = object_size
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.line, = self.ax.plot([], [], marker='o')
        self.object = plt.Circle(self.object_position, self.object_size, fc='red')
        self.ax.add_patch(self.object)
        self.anim = animation.FuncAnimation(self.fig, self.animate, frames=100, interval=50, blit=True)

    def animate(self, i):
        t = i / 100.0
        b_point = self.calculate_bezier_point(t)
        self.object.center = b_point
        return self.object,

    def calculate_bezier_point(self, t):
        n = len(self.control_points) - 1
        point = np.zeros(2)
        for i, p in enumerate(self.control_points):
            point += self.compute_binomial(n, i) * ((1 - t) ** (n - i)) * (t ** i) * p
        return point

    def compute_binomial(self, n, i):
        return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

    def show(self):
        plt.show()

# Example usage:
control_pts = [(0, 0), (0, 10), (10, 10)]
object_start_pos = (1, 1)
object_radius = 0.1

bezier_anim = BezierAnimation(control_pts, object_start_pos, object_radius)
bezier_anim.show()