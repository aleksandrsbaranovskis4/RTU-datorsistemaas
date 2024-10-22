import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data points
x1 = np.array([690.7, 671.6, 623.6, 612.3, 607.3, 579.0, 577.0, 567.6, 546.1, 512.1, 496.2, 491.6, 435.8, 434.7, 433.9, 407.8, 404.7])
y1 = np.array([3210, 3152, 2976, 2930, 2907, 2771, 2758, 2708, 2580, 2272, 2198, 2156, 1488, 1472, 1459, 995, 930])

y2 = np.array([2949, 2708, 2352, 2206, 1890, 938])
x2 = []

def model_func(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = curve_fit(model_func, x1, y1)
a, b, c = params

x_fit = np.linspace(min(x1), max(x1), 200)
y_fit = model_func(x_fit, *params)

def inverse_model_func(y, a, b, c):
    discriminant = b**2 - 4 * a * (c - y)
    if discriminant < 0:
        raise ValueError(f"No real roots for y = {y} with the given quadratic equation.")
    x1 = (-b + np.sqrt(discriminant)) / (2 * a)
    x2 = (-b - np.sqrt(discriminant)) / (2 * a)
    return x1 if min(x1, x2) <= max(x1, x2) else x2

for y in y2:
    x_value = inverse_model_func(y, a, b, c)
    x2.append(x_value)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x1, y1, label='Hg lampa', color='black', marker='.')
ax.plot(x_fit, y_fit, label='Grafiks', color='black')

ax.scatter(x2, y2, label='Na lampa', color='black', marker='x')
ax.set(xlabel=r'${\Lambda}, nm$', ylabel=r'$n, ^{o}$', title=r'$m = f(\Lambda)$')
ax.set_xticks(np.arange(350, 800, 50))
ax.set_yticks(np.arange(500, 3600, 500))
ax.xaxis.set_major_locator(plt.MultipleLocator(50))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_major_locator(plt.MultipleLocator(500))
ax.yaxis.set_minor_locator(plt.MultipleLocator(100))
ax.grid(which = 'minor', color = 'black', linestyle = ':', linewidth = 0.2)
ax.legend()
ax.grid(True)

plt.show()

for x_val, y_val in zip(x2, y2):
    print(f"{y_val} deg: {x_val:.2f} nm")