import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_size = (600, 650)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Brick Breaker")

# Configurações da bola e do jogador
ball_size = 15
ball = pygame.Rect(100, 400, ball_size, ball_size)

player_size = 100
player = pygame.Rect(250, 600, player_size, 15)

# Configuração dos tijolos
bricks_per_line = 16
lines = 5
brick_gap = 10
brick_height = 30
line_gap = brick_height + 5
screen_width = screen_size[0]
brick_width = screen_width / bricks_per_line - brick_gap

# Cores
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}

# Função para criar os tijolos
def create_bricks():
    bricks = []
    for j in range(lines):
        for i in range(bricks_per_line):
            brick = pygame.Rect(i * (brick_width + brick_gap) + brick_gap / 2, j * line_gap, brick_width, brick_height)
            bricks.append(brick)
    return bricks

# Função para desenhar os tijolos
def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, colors["yellow"], brick)

# Movimentação do jogador
def move_player(keys):
    if keys[pygame.K_RIGHT] and player.x + player_size < screen_width:
        player.x += 5
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5

# Movimentação da bola
def move_ball():
    global ball_speed
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Colisão com as bordas
    if ball.x <= 0 or ball.x + ball_size >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.y <= 0:
        ball_speed[1] = -ball_speed[1]
    
    # Colisão com o jogador
    if player.colliderect(ball):
        ball_speed[1] = -ball_speed[1]
    
    # Colisão com os tijolos
    for brick in bricks:
        if brick.colliderect(ball):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]
            break  # Para evitar remoção de múltiplos blocos ao mesmo tempo

    # Se a bola cair, retorna False (fim de jogo)
    if ball.y + ball_size >= screen_size[1]:
        return False

    return True

# Tela de Game Over / Vitória
def show_end_screen(message):
    screen.fill(colors["black"])

    # Mensagem de fim de jogo
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, colors["yellow"])
    text_rect = text.get_rect(center=(screen_width // 2, screen_size[1] // 2 - 50))
    screen.blit(text, text_rect)

    # Botão de reiniciar
    button_rect = pygame.Rect(screen_width // 2 - 75, screen_size[1] // 2, 150, 50)
    pygame.draw.rect(screen, colors["blue"], button_rect)

    button_text = font.render("Reiniciar", True, colors["white"])
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()

    # Espera o clique no botão
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False  # Sai do loop e reinicia o jogo

# Função para reiniciar o jogo
def reset_game():
    global bricks, ball, ball_speed, player
    bricks = create_bricks()
    ball.x, ball.y = 100, 400
    ball_speed = [3, -3]
    player.x = 250

# Desenhar os objetos principais
def draw_game():
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["blue"], player)
    pygame.draw.ellipse(screen, colors["white"], ball)

# Inicializando o jogo
bricks = create_bricks()
ball_speed = [3, -3]

# Loop principal
game_running = True
while game_running:
    screen.fill(colors["black"])
    draw_game()
    draw_bricks(bricks)

    keys = pygame.key.get_pressed()
    move_player(keys)

    if not move_ball():
        show_end_screen("Game Over")
        reset_game()

    if len(bricks) == 0:
        show_end_screen("Você venceu!")
        reset_game()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    pygame.time.wait(10)
    pygame.display.flip()

pygame.quit()
