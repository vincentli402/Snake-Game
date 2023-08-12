import pygame
import random

pygame.init()

# Set up display dimensions
length = 500
screen = pygame.display.set_mode((length, length))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50]]
snake_direction = 'RIGHT'

# Food properties
food_pos = [random.randrange(1, (length//10)) * 10, random.randrange(1, (length//10)) * 10]
food_spawn = True

def gameLoop():
    global snake_direction, food_spawn, food_pos, snake_body, snake_pos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for key presses
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    snake_direction = 'LEFT'
                if keys[pygame.K_RIGHT]:
                    snake_direction = 'RIGHT'
                if keys[pygame.K_UP]:
                    snake_direction = 'UP'
                if keys[pygame.K_DOWN]:
                    snake_direction = 'DOWN'

        # Update snake position
        if snake_direction == 'RIGHT':
            snake_pos[0] += 10
        if snake_direction == 'LEFT':
            snake_pos[0] -= 10
        if snake_direction == 'UP':
            snake_pos[1] -= 10
        if snake_direction == 'DOWN':
            snake_pos[1] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (length // 10)) * 10,
                        random.randrange(1, (length // 10)) * 10]
        food_spawn = True

        # Draw background
        screen.fill(black)

        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw food
        pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        pygame.display.update()

        # Control game speed
        pygame.time.Clock().tick(15)

if __name__ == "__main__":
    gameLoop()
