import pygame
import random
import sys

# Inicializuojame Pygame
pygame.init()

# Langas
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Šventinis Sveikinimas")
clock = pygame.time.Clock()

# Spalvos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (10, 90, 10)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
COLORS = [RED, YELLOW, BLUE, WHITE]

# Eglutė
def draw_tree():
    pygame.draw.polygon(screen, GREEN, [(WIDTH // 2, 100), (WIDTH // 2 - 50, 300), (WIDTH // 2 + 50, 300)])
    pygame.draw.polygon(screen, GREEN, [(WIDTH // 2, 200), (WIDTH // 2 - 70, 400), (WIDTH // 2 + 70, 400)])
    pygame.draw.polygon(screen, GREEN, [(WIDTH // 2, 300), (WIDTH // 2 - 90, 500), (WIDTH // 2 + 90, 500)])
    pygame.draw.rect(screen, (100, 50, 0), (WIDTH // 2 - 20, 500, 40, 50))

    # Papuošimai
    for _ in range(15):
        x = WIDTH // 2 + random.randint(-100, 100)
        y = random.randint(150, 500)
        color = random.choice(COLORS)
        pygame.draw.circle(screen, color, (x, y), 5)

# Fejerverkai
def create_firework():
    return {
        "x": random.randint(0, WIDTH),
        "y": HEIGHT,
        "target_y": random.randint(100, HEIGHT // 2),
        "size": random.randint(3, 6),
        "color": random.choice(COLORS),
        "velocity": random.randint(6, 10)
    }

fireworks = []

# Tekstas
font = pygame.font.Font(None, 50)
greeting_text = font.render("Linksmų Kalėdų ir laimingų Naujųjų metų!", True, WHITE)
text_rect = greeting_text.get_rect(center=(WIDTH // 2, 50))

# Animacija
running = True
while running:
    screen.fill(BLACK)

    # Piešiame eglutę
    draw_tree()

    # Rodome tekstą
    screen.blit(greeting_text, text_rect)

    # Fejerverkai
    if random.random() < 0.05:
        fireworks.append(create_firework())

    for fw in fireworks[:]:
        pygame.draw.circle(screen, fw["color"], (fw["x"], fw["y"]), fw["size"])
        fw["y"] -= fw["velocity"]

        if fw["y"] < fw["target_y"]:
            fireworks.remove(fw)

    # Įvykiai
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
