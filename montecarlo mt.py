import pygame
import random
import threading

# Initialize pygame
pygame.init()

# Set the width and height of the window
width = 440
height = 600
size = (width, height)

# Create the window
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Pygame Window")

points = []
points_lock = threading.Lock()

# Create a font object for the counter
font = pygame.font.Font(None, 36)

# Create a start-stop button
start_stop_button = pygame.Rect(10, 430, 100, 50)

# Create a flag to track if the start-stop button is clicked
start_clicked = False

# Create a counter for the points placed
points_placed = 0

# Create a counter for the iterations
iteration_count = 0

# Create a counter for the points inside the circle
points_inside_circle = 0

def generate_points():
    global points_placed, points_inside_circle
    while True:
        if start_clicked:
            for _ in range(2**16):
                random_x = random.uniform(20, width-20)
                random_y = random.uniform(20, 420)

                random_point = (random_x, random_y)
                with points_lock:
                    points.append(random_point)
                    points_placed += 1

                distance = ((random_x - center_x) ** 2 + (random_y - center_y) ** 2) ** 0.5
                if distance <= radius:
                    points_inside_circle += 1

def game_loop():
    global start_clicked, points_placed, points_inside_circle, iteration_count, points
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_stop_button.collidepoint(event.pos):
                    start_clicked = not start_clicked

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the points as circles
        with points_lock:
            for point in points:
                distance = ((point[0] - center_x) ** 2 + (point[1] - center_y) ** 2) ** 0.5
                if distance <= radius:
                    pygame.draw.circle(screen, (0, 255, 0), point, 2)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), point, 2)

        # Draw the start-stop button
        if start_clicked:
            pygame.draw.rect(screen, (255, 0, 0), start_stop_button)
            start_stop_text = font.render("Stop", True, (255, 255, 255))
        else:
            pygame.draw.rect(screen, (0, 255, 0), start_stop_button)
            start_stop_text = font.render("Start", True, (255, 255, 255))
        screen.blit(start_stop_text, (20, 440))

        # Draw the counter
        counter_text = font.render("Points Placed: " + str(points_placed), True, (255, 255, 255))
        screen.blit(counter_text, (10, 490))

        in_circle_text = font.render("Points Inside Circle: " + str(points_inside_circle), True, (255, 255, 255))
        screen.blit(in_circle_text, (10, 530))

        # Calculate the value of pi
        if points_placed > 0:
            pi = 4 * points_inside_circle / points_placed
        else:
            pi = 0
        pi_text = font.render("Pi: " + str(pi), True, (255, 255, 255))
        screen.blit(pi_text, (250, 440))

        # Calculate the radius of the circle
        radius = 200

        # Calculate the center of the circle
        center_x = width / 2
        center_y = 440 / 2

        # Draw the circle
        pygame.draw.circle(screen, (0, 0, 255), (int(center_x), int(center_y)), int(radius), 1)

        # Update the display
        pygame.display.flip()

        # Remove points after 1 iterations
        iteration_count += 1
        if iteration_count >= 1:
            with points_lock:
                points = []

# Create and start the threads
point_generation_thread = threading.Thread(target=generate_points)
game_loop_thread = threading.Thread(target=game_loop)

point_generation_thread.start()
game_loop_thread.start()

# Wait for the threads to finish
point_generation_thread.join()
game_loop_thread.join()

# Quit pygame
pygame.quit()
