import pygame
from assets import *
from settings import *

health_progress = 50

class Projectile:
    def __init__(self, x, y, radius, color, facing, shoot_by = None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.shoot_by = shoot_by

    def draw(self, WIN): 
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

def shoot(hunter, prey, bullets):
    if hunter.side == 'H':
        if hunter.x >= prey.x and not hunter.left:
            facing = -1
        elif hunter.x <= prey.x and not hunter.right:
            facing = 1
        if hunter.left:
            facing = -1
        elif hunter.right:
            facing = 1
        if len(bullets) < 3:
            bullets.append(Projectile(round(hunter.x + hunter.width // 2), round(hunter.y + hunter.height // 2), 6, YELLOW, facing))
            projectile_sound.play()

    elif hunter.side == 'H1':
        if hunter.x >= prey.x and not hunter.left:
            facing = -1
        elif hunter.x <= prey.x and not hunter.right:
            facing = 1
        if hunter.left:
            facing = -1
        elif hunter.right:
            facing = 1
        if len(bullets) < 3:
            bullets.append(Projectile(round(hunter.x + hunter.width // 2), round(hunter.y + hunter.height // 2), 6, YELLOW, facing))
            projectile_sound.play()

def shoot_dm(player1, player2, bullets1, bullets2):
        if player1.side == 'H':
            if player1.x >= player2.x and not player1.left:
                facing = -1
            elif player1.x <= player2.x and not player1.right:
                facing = 1
            if player1.left:
                facing = -1
            elif player1.right:
                facing = 1
            if len(bullets1) < 3:
                bullets1.append(Projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2), 6, DESATURATED_RED, facing, 1))
                projectile_sound.play()

        elif player1.side == 'H1':
            if player1.x >= player2.x and not player1.left:
                facing = -1
            elif player1.x <= player2.x and not player1.right:
                facing = 1
            if player1.left:
                facing = -1
            elif player1.right:
                facing = 1
            if len(bullets2) < 3:
                bullets2.append(Projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2), 6, DESATURATED_BLUE, facing, 2))
                projectile_sound.play()

def collision_check(prey, bullets, turn):
    for bullet in bullets:
        if is_collision(bullet, prey, turn):
            bullets.pop(bullets.index(bullet))
            return True

def is_collision(bullet, player, turn):
    global health_progress
    if turn == 1 or turn == 2:
        if bullet.x > player.x and bullet.x < player.x + player.width:
            if bullet.y > player.y and bullet.y < player.y + player.height:
                return True
        return False
    elif turn == 3:
        if bullet.shoot_by == 1 and player.side == "H1":
            if bullet.x > player.x and bullet.x < player.x + player.width and bullet.y > player.y and bullet.y < player.y + player.height:
                health_progress += 10
                return True
        elif bullet.shoot_by == 2 and player.side == "H":
            if bullet.x > player.x and bullet.x < player.x + player.width and bullet.y > player.y and bullet.y < player.y + player.height:
                health_progress -= 10
                return True
        return False

def update_projectile(WIN_WIDTH, bullets1, bullets2 = []):
    for bullet1 in bullets1:
        if 0 < bullet1.x < WIN_WIDTH:
            bullet1.x += bullet1.vel
        else:
            bullets1.pop(bullets1.index(bullet1))
    for bullet2 in bullets2:
        if 0 < bullet2.x < WIN_WIDTH:
            bullet2.x += bullet2.vel
        else:
            bullets2.pop(bullets2.index(bullet2))

def draw_bullets(WIN, bullets1, bullets2 = []):
    for bullet1 in bullets1:
        bullet1.draw(WIN)
    for bullet2 in bullets2:
        bullet2.draw(WIN)

def draw_shared_health_bar():
    bar_width = 400
    bar_height = 30
    bar_x = (WIN_WIDTH - bar_width) // 2
    bar_y = 10

    red_width = int((health_progress / 100) * bar_width)
    blue_width = bar_width - red_width

    pygame.draw.rect(WIN, RED, (bar_x, bar_y, red_width, bar_height))
    pygame.draw.rect(WIN, BLUE, (bar_x + red_width, bar_y, blue_width, bar_height))
    pygame.draw.rect(WIN, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)

    return health_progress