import pygame
import sys

from assets import *
from settings import *
from projectile import *
from player import *
from graphic import *

player1_score, player2_score = 0, 0
player1 = Player(x=0, y=280, width=64, height=64, vel=5, jumpcount=7, walkCount=0, side="H")
player2 = Player(x=557, y=280, width=64, height=64, vel=7, jumpcount=7, walkCount=0, side="P")

bullets = []
bullets1 = []
bullets2 = []

clock = pygame.time.Clock()
start_ticks = None
player_names = get_player_names()
start_ticks = pygame.time.get_ticks()

turn = 1

running = True

while running:
    clock.tick(30)
    WIN.blit(game_bg, (0, 0))

    if start_ticks is not None:
        time_passed = (pygame.time.get_ticks() - start_ticks) // 1000

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and turn == 1:
                shoot(player1, player2, bullets)
                
            elif event.key == pygame.K_RSHIFT and turn == 2:
                shoot(player2, player1, bullets)
                
            elif turn == 3:
                if event.key == pygame.K_SPACE:
                    shoot_dm(player1, player2, bullets1, bullets2)
                if event.key == pygame.K_RSHIFT:
                    shoot_dm(player2, player1, bullets1, bullets2)

    if time_passed == 51:
        turn = 2
        display_message("Round change!", duration=2000)
        player1.side, player2.side = "P1", "H1"
        player1.vel, player2.vel = 7, 5
        player1.x, player2.x = 0, 557
        bullets = []      
    elif time_passed == 103 and player1_score > player2_score:
        display_message(f"{player_names[0]} Wins!", duration=5000)
        running = False
    elif time_passed == 103 and player1_score < player2_score:
        display_message(f"{player_names[1]} Wins!", duration=5000)
        running = False
    elif time_passed == 103 and player1_score == player2_score:
        turn = 3
        display_message("Deathmatch!", duration=2000)
        player1.side, player2.side = "H", "H1"
        player1.vel = player2.vel = 5
        player1.x, player2.x = 0, 557
        bullets = []
    
    if turn == 1:   
        if collision_check(player2, bullets, turn):
            player1_score += 10
        draw_scores(player_names[0], player1_score, time_passed, player_names[1], player2_score)
    elif turn == 2:
        time_passed -=2
        if collision_check(player1, bullets, turn):
            player2_score += 10
        draw_scores(player_names[0], player1_score, time_passed, player_names[1], player2_score)
    elif turn == 3:
        collision_check(player1, bullets2, turn)
        collision_check(player2, bullets1, turn)
        health = draw_shared_health_bar()
        if health == 0:
            display_message(f"{player_names[1]} Wins!", duration=5000)
            running = False
        elif health == 100:
            display_message(f"{player_names[0]} Wins!", duration=5000)
            running = False
    if turn == 1 or turn == 2:   
        update_projectile(WIN_WIDTH, bullets)  
        draw_bullets(WIN, bullets)
    else:
        update_projectile(WIN_WIDTH, bullets1, bullets2)  
        draw_bullets(WIN, bullets1, bullets2)
   
    player1.action(keys, player2.x, turn)
    player2.action(keys, player1.x, turn)

    pygame.display.update()