import pygame
import threading
from pygame.locals import USEREVENT

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
    screen.fill(background_color)

    # Set red color
    red = (255, 0, 0)

    # Pong Ball Dimensions
    ball_width = 50
    ball_height = 50

    # Create the ball (a rectangular surface)
    ball = pygame.Surface((ball_width, ball_height))
    ball.fill(red)  # Fill the ball with red

    # Position of the ball
    ball_x, ball_y = 600, 250  # Initial position of the ball

    # Dimensions of Slide A
    Slide1_width = 30
    Slide1_height = 250

    # Create Slide A (a rectangular surface)
    Slide = pygame.Surface((Slide1_width, Slide1_height))
    Slide.fill(red)  # Fill Slide A with red

    # Initial position of Slide A for motion
    Slide_x, Slide_y = 20, 150

    # Dimensions of Slide B
    Slide2_width = 30
    Slide2_height = 250

    # Create Slide B (a rectangular surface)
    Slide2 = pygame.Surface((Slide2_width, Slide2_height))
    Slide2.fill(red)  # Fill Slide B with red

    # Initial position of Slide B for motion
    Slide2_x, Slide2_y = 1220, 150

    running = True  # Initialize the running variable for the game loop

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == audio_end_event.type:
                # The audio has ended; restart it
                pygame.mixer.music.play()

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

        # Ensure that the slides stay within the screen boundaries
        Slide_y = max(0, min(Slide_y, height - Slide1_height))
        Slide2_y = max(0, min(Slide2_y, height - Slide2_height))

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
