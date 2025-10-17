import pygame
import time
import random

# Initialize the pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 600
dis_height = 400

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Qwen')

# Define the clock
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    player1_x1 = dis_width / 2
    player1_y1 = dis_height / 2

    player2_x1 = dis_width / 4
    player2_y1 = dis_height / 2

    player1_x1_change = 0
    player1_y1_change = 0

    player2_x1_change = 0
    player2_y1_change = 0

    snake1_List = []
    Length_of_snake1 = 1

    snake2_List = []
    Length_of_snake2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    powerup_x = random.randint(snake_block, dis_width - snake_block)
    powerup_y = random.randint(snake_block, dis_height - snake_block)
    powerup_radius = 15
    powerup_active = True

    def draw_powerup():
        pygame.draw.circle(dis, red, (powerup_x, powerup_y), powerup_radius)

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Player 1 controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1_x1_change = -snake_block
                    player1_y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    player1_x1_change = snake_block
                    player1_y1_change = 0
                elif event.key == pygame.K_UP:
                    player1_y1_change = -snake_block
                    player1_x1_change = 0
                elif event.key == pygame.K_DOWN:
                    player1_y1_change = snake_block
                    player1_x1_change = 0

            # Player 2 controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player2_x1_change = -snake_block
                    player2_y1_change = 0
                elif event.key == pygame.K_d:
                    player2_x1_change = snake_block
                    player2_y1_change = 0
                elif event.key == pygame.K_w:
                    player2_y1_change = -snake_block
                    player2_x1_change = 0
                elif event.key == pygame.K_s:
                    player2_y1_change = snake_block
                    player2_x1_change = 0

        # Player 1 movement and boundaries
        if player1_x1 >= dis_width or player1_x1 < 0 or player1_y1 >= dis_height or player1_y1 < 0:
            game_close = True
        player1_x1 += player1_x1_change
        player1_y1 += player1_y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        draw_powerup()
        snake1_Head = []
        snake1_Head.append(player1_x1)
        snake1_Head.append(player1_y1)
        snake1_List.append(snake1_Head)
        if len(snake1_List) > Length_of_snake1:
            del snake1_List[0]

        for x in snake1_List[:-1]:
            if x == snake1_Head:
                game_close = True

        # Player 2 movement and boundaries
        if player2_x1 >= dis_width or player2_x1 < 0 or player2_y1 >= dis_height or player2_y1 < 0:
            game_close = True
        player2_x1 += player2_x1_change
        player2_y1 += player2_y1_change
        draw_powerup()
        snake2_Head = []
        snake2_Head.append(player2_x1)
        snake2_Head.append(player2_y1)
        snake2_List.append(snake2_Head)
        if len(snake2_List) > Length_of_snake2:
            del snake2_List[0]

        for x in snake2_List[:-1]:
            if x == snake2_Head:
                game_close = True

        # Check for collision with food
        if player1_x1 == foodx and player1_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake1 += 1

        if player2_x1 == foodx and player2_y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake2 += 1

        # Check for powerup collision
        if (player1_x1 < powerup_x + powerup_radius and player1_x1 > powerup_x - powerup_radius
                and player1_y1 < powerup_y + powerup_radius and player1_y1 > powerup_y - powerup_radius):
            Length_of_snake1 += 5
            powerup_active = False

        if (player2_x1 < powerup_x + powerup_radius and player2_x1 > powerup_x - powerup_radius
                and player2_y1 < powerup_y + powerup_radius and player2_y1 > powerup_y - powerup_radius):
            Length_of_snake2 += 5
            powerup_active = False

        # Powerup respawn
        if not powerup_active:
            powerup_x = random.randint(snake_block, dis_width - snake_block)
            powerup_y = random.randint(snake_block, dis_height - snake_block)
            powerup_radius = 15
            powerup_active = True

        our_snake(snake_block, snake1_List)
        our_snake(snake_block, snake2_List)

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()