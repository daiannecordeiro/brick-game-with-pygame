import pygame

# init
pygame.init()

screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Brick Breaker")

ball_size = 15
ball = pygame.Rect(100, 500, ball_size, ball_size)

player_size = 100
player = pygame.Rect(0, 750, player_size, 15)

bricks_per_line = 8
lines = 5
total_blocks = bricks_per_line * lines

def create_bricks(bricks_per_line, lines, total_blocks):
    bricks = []
    # criar blocos
    return bricks

colors = {
    "white": (255,255,255),
    "black": (0,0,0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}

game_over = False

score = 0

ball_speed = [1, 1]

# game functions



# draw objects
