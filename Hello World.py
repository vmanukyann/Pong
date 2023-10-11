import pygame
pygame.init()

# Get the screen dimensions
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h

# Pong Game Display in Fullscreen
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Pong Game")


# Colors
white = (255, 255, 255)
blue = (0, 0, 255)  # Define the blue color

# Pong Ball Dimensions
ball_width = 50
ball_height = 50

# Create the ball (a rectangular surface)
ball = pygame.Surface((ball_width, ball_height))
ball.fill(blue)  # Fill the ball with the blue color

# Position of the ball
ball_x, ball_y = 600, 250  # Initial position of the ball

# Dimensions of Slide A
Slide1_width = 30
Slide1_height = 250

# Create Slide A (a rectangular surface)
Slide = pygame.Surface((Slide1_width, Slide1_height))
Slide.fill(blue)  # Fill Slide A with the blue color

# Initial position of Slide A for motion
Slide_x, Slide_y = 20, 150

# Dimensions of Slide B
Slide2_width = 30
Slide2_height = 250

# Create Slide B (a rectangular surface)
Slide2 = pygame.Surface((Slide2_width, Slide2_height))
Slide2.fill(blue)  # Fill Slide B with the blue color

# Initial position of Slide B for motion
Slide2_x, Slide2_y = 1220, 150

# Running the Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Event handling for motion of Slides
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Slide A goes up
        Slide_y -= 0.5
    if keys[pygame.K_s]:  # Slide A goes down
        Slide_y += 0.5
    if keys[pygame.K_UP]:  # Slide B goes up
        Slide2_y -= 0.5
    if keys[pygame.K_DOWN]:  # Slide B goes down
        Slide2_y += 0.5

    #Motion of Ball
    

    # Ensure that the slides stay within the screen boundaries
    Slide_y = max(0, min(Slide_y, height - Slide1_height))
    Slide2_y = max(0, min(Slide2_y, height - Slide2_height))

    # Clear the screen
    screen.fill(white)

    # Draw the ball on the screen
    screen.blit(ball, (ball_x, ball_y))

    # Draw Slide A on the screen
    screen.blit(Slide, (Slide_x, Slide_y))

    # Draw Slide B on the screen
    screen.blit(Slide2, (Slide2_x, Slide2_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
