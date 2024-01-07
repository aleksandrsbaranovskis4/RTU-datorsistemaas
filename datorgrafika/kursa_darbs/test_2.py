import pygame
from math import comb

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Bezier curve order
ORDER = 3

# Control points
control_points = [(100, 100), (200, 100), (200, 200), (100, 200)]

# List of all Bezier curve points
bezier_points = []

# Function to calculate Bezier curve points
def bezier(t, control_points):
    n = len(control_points) - 1
    return sum([comb(n, i) * (1 - t) ** (n - i) * t ** i * control_points[i] for i in range(n + 1)])

# Function to update Bezier curve points
def update_bezier_points():
    global bezier_points
    bezier_points = []
    for t in range(0, 101, 10):
        bezier_points.append(bezier(t / 100, control_points))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Update control points if the mouse click is inside the drawing area
            if mouse_x < WIDTH and mouse_y < HEIGHT:
                for i in range(ORDER + 1):
                    for j in range(ORDER + 1 - i):
                        control_points[i * (ORDER + 1) + j] = (mouse_x, mouse_y)
                update_bezier_points()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw control points
    for point in control_points:
        pygame.draw.circle(screen, (255, 255, 255), point, 5)

    # Draw Bezier curve
    for i in range(len(bezier_points) - 1):
        pygame.draw.line(screen, (255, 255, 255), bezier_points[i], bezier_points[i + 1], 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()