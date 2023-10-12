import pygame
import threading
from pygame.locals import USEREVENT
import random

# Define the file path as a variable
audio_file_path = r"C:\Users\kmanukya\Downloads\The-Weeknd-Blinding-Lights.mp3"

# Initialize the Pygame mixer and load the audio
pygame.mixer.init()
pygame.mixer.music.load(audio_file_path)

# Create a custom event to handle audio looping
audio_end_event = pygame.event.Event(USEREVENT + 1)

def play_audio():
    pygame.mixer.music.play(-1)  # Play the audio in an infinite loop

def main():
    pygame.init()

    # Get the screen dimensions
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h

    # Pong Game Display in Fullscreen
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Pong Game")

    # Set background color to black
    background_color = (0, 0, 0)

    # Set red color
    red = (255, 0, 0)

    # Pong Ball Dimensions
    ball_width = 25
    ball_height = 25

    # Create the ball (a rectangular surface)
    ball = pygame.Surface((ball_width, ball_height))
    ball.fill(red)  # Fill the ball with red

    # Initial position of the ball
    ball_x, ball_y = width // 2, height // 2  # Start in the center of the screen

    # Initial velocity for the ball
    ball_velocity_x = 1  # Slower movement (you can adjust this value)
    ball_velocity_y = 1  # Slower movement (you can adjust this value)

    # Dimensions of Slide A
    Slide1_width = 30
    Slide1_height = 150

    # Create Slide A (a rectangular surface)
    Slide = pygame.Surface((Slide1_width, Slide1_height))
    Slide.fill(red)  # Fill Slide A with red

    # Initial position of Slide A for motion
    Slide_x, Slide_y = 20, (height - Slide1_height) // 2

    # Dimensions of Slide B
    Slide2_width = 30
    Slide2_height = 150

    # Create Slide B (a rectangular surface)
    Slide2 = pygame.Surface((Slide2_width, Slide2_height))
    Slide2.fill(red)  # Fill Slide B with red

    # Initial position of Slide B for motion
    Slide2_x, Slide2_y = width - 20 - Slide2_width, (height - Slide2_height) // 2

    running = True  # Initialize the running variable for the game loop

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == audio_end_event.type:
                # The audio has ended; restart it
                pygame.mixer.music.play()

        # Event handling for motion of Slide A (keyboard input)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and Slide_y > 0:  # Slide A goes up
            Slide_y -= 1
        if keys[pygame.K_s] and Slide_y + Slide1_height < height:  # Slide A goes down
            Slide_y += 1

        # Event handling for motion of Slide B (keyboard input)
        if keys[pygame.K_UP] and Slide2_y > 0:  # Slide B goes up
            Slide2_y -= 1
        if keys[pygame.K_DOWN] and Slide2_y + Slide2_height < height:  # Slide B goes down
            Slide2_y += 1

        # Update the ball's position based on its velocity
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y

        # Check if the ball goes out of the screen on the left or right
        if ball_x < 0 or ball_x + ball_width > width:
            # Reset the ball's position to the center
            ball_x = width // 2
            ball_y = height // 2
            # Randomly choose a new direction for the ball
            ball_velocity_x = random.choice([-1, 1])  # Adjust for slower or faster movement
            ball_velocity_y = random.choice([-1, 1])  # Adjust for slower or faster movement
        elif (ball_x <= Slide_x + Slide1_width and Slide_y <= ball_y <= Slide_y + Slide1_height) or \
             (ball_x + ball_width >= Slide2_x and Slide2_y <= ball_y <= Slide2_y + Slide2_height):
            # Ball hits a slider, bounce it in the opposite direction
            ball_velocity_x = -ball_velocity_x

        # Boundary checks for the top and bottom of the screen
        if ball_y < 0 or ball_y + ball_height > height:
            ball_velocity_y = -ball_velocity_y

        # Clear the screen with the black background
        screen.fill(background_color)

        # Draw the ball on the screen in red
        screen.blit(ball, (ball_x, ball_y))

        # Draw Slide A on the screen in red
        screen.blit(Slide, (Slide_x, Slide_y))

        # Draw Slide B on the screen in red
        screen.blit(Slide2, (Slide2_x, Slide2_y))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    main()

    # Quit Pygame
    pygame.quit()
