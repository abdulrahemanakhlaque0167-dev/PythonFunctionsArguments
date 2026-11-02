import pygame
import random
import sys

pygame.init()

# -------------------- WINDOW --------------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG - YOU vs BOT")
clock = pygame.time.Clock()

# -------------------- COLOURS --------------------
BLACK = (15, 18, 30)
WHITE = (245, 245, 245)
CYAN = (50, 220, 230)
ORANGE = (255, 160, 70)
GREY = (110, 120, 140)
GREEN = (90, 220, 130)

# -------------------- GAME SETTINGS --------------------
PADDLE_W, PADDLE_H = 15, 110
BALL_SIZE = 18
PLAYER_SPEED = 7
BOT_SPEED = 5.2          # Increase this to make the bot harder
WIN_SCORE = 5

font = pygame.font.SysFont("arial", 32, bold=True)
small_font = pygame.font.SysFont("arial", 22)
big_font = pygame.font.SysFont("arial", 54, bold=True)

player = pygame.Rect(35, HEIGHT // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
bot = pygame.Rect(WIDTH - 35 - PADDLE_W, HEIGHT // 2 - PADDLE_H // 2,
                  PADDLE_W, PADDLE_H)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2,
                   HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

player_score = 0
bot_score = 0
ball_dx = random.choice([-5, 5])
ball_dy = random.choice([-4, 4])
started = False
game_over = False
winner_text = ""


def reset_ball(direction):
    global ball_dx, ball_dy, started
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx = 5 * direction
    ball_dy = random.choice([-4, -3, 3, 4])
    started = False


def reset_game():
    global player_score, bot_score, game_over, winner_text
    player_score = 0
    bot_score = 0
    game_over = False
    winner_text = ""
    player.centery = HEIGHT // 2
    bot.centery = HEIGHT // 2
    reset_ball(random.choice([-1, 1]))


def draw_text(text, font_obj, colour, center):
    image = font_obj.render(text, True, colour)
    screen.blit(image, image.get_rect(center=center))


def move_bot():
    # The bot follows the ball, but its speed is limited so it can be beaten.
    target_y = ball.centery
    difference = target_y - bot.centery

    if abs(difference) > 9:
        if difference > 0:
            bot.y += min(BOT_SPEED, difference)
        else:
            bot.y -= min(BOT_SPEED, -difference)

    bot.y = max(0, min(HEIGHT - PADDLE_H, bot.y))


def update_ball():
    global ball_dx, ball_dy, player_score, bot_score, game_over, winner_text

    ball.x += round(ball_dx)
    ball.y += round(ball_dy)

    # Top and bottom walls
    if ball.top <= 0:
        ball.top = 0
        ball_dy *= -1
    elif ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        ball_dy *= -1

    # Player paddle
    if ball.colliderect(player) and ball_dx < 0:
        ball.left = player.right
        ball_dx = abs(ball_dx) * 1.04
        hit_position = (ball.centery - player.centery) / (PADDLE_H / 2)
        ball_dy = max(-7, min(7, hit_position * 6))

    # Bot paddle
    if ball.colliderect(bot) and ball_dx > 0:
        ball.right = bot.left
        ball_dx = -abs(ball_dx) * 1.04
        hit_position = (ball.centery - bot.centery) / (PADDLE_H / 2)
        ball_dy = max(-7, min(7, hit_position * 6))

    # Keep the ball speed under control
    ball_dx = max(-9, min(9, ball_dx))

    # Scoring
    if ball.right < 0:
        bot_score += 1
        if bot_score >= WIN_SCORE:
            game_over = True
            winner_text = "BOT WINS!"
        else:
            reset_ball(1)

    elif ball.left > WIDTH:
        player_score += 1
        if player_score >= WIN_SCORE:
            game_over = True
            winner_text = "YOU WIN!"
        else:
            reset_ball(-1)


def draw_game():
    screen.fill(BLACK)

    # Centre line
    for y in range(0, HEIGHT, 28):
        pygame.draw.rect(screen, GREY, (WIDTH // 2 - 2, y, 4, 14))

    pygame.draw.rect(screen, CYAN, player, border_radius=7)
    pygame.draw.rect(screen, ORANGE, bot, border_radius=7)
    pygame.draw.ellipse(screen, WHITE, ball)

    draw_text(str(player_score), big_font, CYAN, (WIDTH // 4, 55))
    draw_text(str(bot_score), big_font, ORANGE, (3 * WIDTH // 4, 55))
    draw_text("YOU", small_font, CYAN, (WIDTH // 4, 95))
    draw_text("BOT", small_font, ORANGE, (3 * WIDTH // 4, 95))

    if not started and not game_over:
        draw_text("Press SPACE to serve", small_font, WHITE,
                  (WIDTH // 2, HEIGHT // 2 + 75))

    if game_over:
        draw_text(winner_text, big_font, GREEN if winner_text == "YOU WIN!" else ORANGE,
                  (WIDTH // 2, HEIGHT // 2 - 20))
        draw_text("Press R to play again  |  ESC to quit", small_font, WHITE,
                  (WIDTH // 2, HEIGHT // 2 + 35))

    pygame.display.flip()


# -------------------- MAIN LOOP --------------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and not game_over:
                started = True
            elif event.key == pygame.K_r:
                reset_game()

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += PLAYER_SPEED

        player.y = max(0, min(HEIGHT - PADDLE_H, player.y))
        move_bot()

        if started:
            update_ball()

    draw_game()

pygame.quit()
sys.exit()
