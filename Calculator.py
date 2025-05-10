import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 400, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Калькулятор")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

input_text = ""

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

def draw_buttons():
    button_width = WIDTH // 4
    button_height = 100
    for i, row in enumerate(buttons):
        for j, text in enumerate(row):
            rect = pygame.Rect(j * button_width, 150 + i * button_height, button_width, button_height)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            txt_surface = font.render(text, True, BLACK)
            screen.blit(txt_surface, (rect.x + 30, rect.y + 25))

def calculate(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = "Error!"
    return result

running = True
while running:
    screen.fill(WHITE)
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (10, 50))

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y >= 150:
                row = (y - 150) // 100
                col = x // (WIDTH // 4)
                button = buttons[row][col]
                if button == 'C':
                    input_text = ""
                elif button == '=':
                    input_text = calculate(input_text)
                else:
                    input_text += button

    pygame.display.flip()

pygame.quit()
sys.exit()
