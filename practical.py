
import pygame
import random

pygame.init()

# Game window
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooting Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK = (10, 10, 25)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 60, 60)
YELLOW = (255, 230, 50)

# Player
player = pygame.Rect(275, 610, 50, 40)
player_speed = 6

# Bullets and enemies
bullets = []
enemies = []
score = 0
game_over = False

def draw_text(text, x, y, color=WHITE):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append(
                    pygame.Rect(player.centerx - 4, player.top, 8, 18)
                )

            if event.key == pygame.K_r and game_over:
                player.x = 275
                bullets.clear()
                enemies.clear()
                score = 0
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:
        # Move player
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= 9
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # Spawn enemies
        if random.randint(1, 30) == 1:
            enemy = pygame.Rect(
                random.randint(0, WIDTH - 40), -40, 40, 40
            )
            enemies.append(enemy)

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += 3

            if enemy.top > HEIGHT:
                enemies.remove(enemy)

            elif enemy.colliderect(player):
                game_over = True

        # Bullet collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

    # Draw everything
    screen.fill(BLACK)

    # Stars
    for _ in range(30):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        screen.set_at((x, y), WHITE)

    # Player spaceship
    pygame.draw.polygon(
        screen, BLUE,
        [
            (player.centerx, player.top),
            (player.left, player.bottom),
            (player.centerx, player.bottom - 10),
            (player.right, player.bottom)
        ]
    )

    # Bullets
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy, border_radius=8)

    draw_text(f"Score: {score}", 15, 15)

    if game_over:
        draw_text("GAME OVER!", 210, 300, RED)
        draw_text("Press R to Restart", 180, 350)

    pygame.display.flip()

pygame.quit()

