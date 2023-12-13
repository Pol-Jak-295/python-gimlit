#python 3.2.3
# -*- coding: utf-8 -*-
#Made by Pol-Jak-295
#check if both libraries are installed, if not, install them
try:
    import pygame
except ImportError:
    import pip
    pip.main(['install', 'pygame'])
    import pygame

try:
    import random
except ImportError:
    import pip
    pip.main(['install', 'random'])
    import random

# Initialize pygame
pygame.init()

# Set the width and height of the window
width = 640
height = 800
size = (width, height)

# Create the window
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Pygame Window")

points = []

# Create a font object for the counter
font = pygame.font.Font(None, 36)

# Create a start-stop button
start_stop_button = pygame.Rect(10, 630, 100, 50)

# Create a flag to track if the start-stop button is clicked
start_clicked = False

# Create a counter for the points placed
points_placed = 0

# Create a counter for the iterations
iteration_count = 0

# Create a counter for the points inside the circle
points_inside_circle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_stop_button.collidepoint(event.pos):
                start_clicked = not start_clicked

    # Generate a random point on the top area of the screen
    if start_clicked:
        for _ in range(8192):
            random_x = random.uniform(20, width-20)
            random_y = random.uniform(20, 620)

            random_point = (random_x, random_y)
            points.append(random_point)
            points_placed += 1

            distance = ((random_x - center_x) ** 2 + (random_y - center_y) ** 2) ** 0.5
            if distance <= radius:
                points_inside_circle += 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the points as circles
    for point in points:
        distance = ((point[0] - center_x) ** 2 + (point[1] - center_y) ** 2) ** 0.5
        if distance <= radius:
            pygame.draw.circle(screen, (0, 255, 0), point, 3)
        else:
            pygame.draw.circle(screen, (255, 0, 0), point, 3)

    # Draw the start-stop button
    if start_clicked:
        pygame.draw.rect(screen, (255, 0, 0), start_stop_button)
        start_stop_text = font.render("Stop", True, (255, 255, 255))
    else:
        pygame.draw.rect(screen, (0, 255, 0), start_stop_button)
        start_stop_text = font.render("Start", True, (255, 255, 255))
    screen.blit(start_stop_text, (20, 640))

    # Draw the counter
    counter_text = font.render("Points Placed: " + str(points_placed), True, (255, 255, 255))
    screen.blit(counter_text, (10, 690))

    in_circle_text = font.render("Points Inside Circle: " + str(points_inside_circle), True, (255, 255, 255))
    screen.blit(in_circle_text, (10, 730))

    # Calculate the value of pi
    if points_placed > 0:
        pi = 4 * points_inside_circle / points_placed
    else:
        pi = 0
    pi_text = font.render("Pi: " + str(pi), True, (255, 255, 255))
    screen.blit(pi_text, (300, 640))

    # Calculate the radius of the circle
    radius = 300

    # Calculate the center of the circle
    center_x = width / 2
    center_y = 640 / 2

    # Draw the circle
    pygame.draw.circle(screen, (0, 0, 255), (int(center_x), int(center_y)), int(radius), 1)

    # Update the display
    pygame.display.flip()

    # Remove points after 1 iterations
    iteration_count += 1
    if iteration_count >= 1:
        points = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()


# Quit pygame
pygame.quit()
