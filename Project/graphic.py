import pygame
import sys
from assets import *
from settings import *

def get_player_names():
    title_font = pygame.font.Font("fonts/Lobster-Regular.ttf", 60)
    input_font = pygame.font.Font("fonts/Montserrat-Regular.ttf", 25)

    input_boxes = [pygame.Rect(WIN_WIDTH/4, 135, 300, 50), pygame.Rect(WIN_WIDTH/4, 200, 300, 50)]
    player_names = ["", ""]
    active_box = 0
    typing = True
    MAX_LENGTH = 10 

    while typing:
        
        WIN.blit(menu_bg, (0, 0))
        
        title_surface = title_font.render("Hunter and Prey", True, WHITE)
        WIN.blit(title_surface, (WIN.get_width() // 2 - title_surface.get_width() // 2, 10))

        subtitle_surface = input_font.render("Enter Player Names", True, WHITE)
        WIN.blit(subtitle_surface, (WIN.get_width() // 2 - subtitle_surface.get_width() // 2, 80))

        for i, box in enumerate(input_boxes):
            box_color = ORANGE if i == active_box else DIRTY_WHITE
            pygame.draw.rect(WIN, box_color, box, border_radius=10, width=3)  
            name_surface = input_font.render(player_names[i], True, WHITE)
            WIN.blit(name_surface, (box.x + 10, box.y + 10))
            
        instructions = input_font.render("Press Tab to change box and Enter when done", True, WHITE)
        WIN.blit(instructions, (WIN.get_width() // 2 - instructions.get_width() // 2, 280))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    active_box = (active_box + 1) % len(input_boxes)
                elif event.key == pygame.K_RETURN and player_names[0] and player_names[1]:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    player_names[active_box] = player_names[active_box][:-1]
                elif len(player_names[active_box]) < MAX_LENGTH:
                    player_names[active_box] += event.unicode

    return player_names


def display_message(text, duration=2000):
    
    font = pygame.font.Font("fonts/Lobster-Regular.ttf", 70)
    text_surface = font.render(text, True, WHITE)
    WIN.blit(text_surface, (WIN_WIDTH // 2 - text_surface.get_width() // 2, WIN_HEIGHT // 2 - text_surface.get_height() // 2))
    
    pygame.display.flip()
    pygame.time.delay(duration)

def draw_scores(name1, score1, timer, name2, score2):
    
    font = pygame.font.Font("fonts/Lobster-Regular.ttf", 30)
    score_text1 = font.render(f"{name1}: {score1}", True, WHITE)
    score_text2 = font.render(f"{name2}: {score2}", True, WHITE)
    timer_text = font.render(f"{abs(100-(timer))}", True, WHITE)
    
    WIN.blit(score_text1, (10, 10))
    WIN.blit(timer_text, (((WIN_WIDTH/2) - timer_text.get_width()), 10))
    WIN.blit(score_text2, ((WIN_WIDTH - score_text2.get_width()) - 10, 10))
