import pygame
from assets import *
from settings import *

class Player:
    def __init__(self, x, y, width, height, vel, jumpcount, walkCount, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = jumpcount
        self.left = False
        self.right = False
        self.walkCount = walkCount
        self.side = side

    def draw_triangle(self, color):
        top_point = (self.x + self.width // 2, 344)
        left_point = (self.x + self.width // 4, 354)
        right_point = (self.x + 3 * self.width // 4, 354)
        pygame.draw.polygon(WIN, color, [top_point, left_point, right_point])

    def action(self, keys, opponent_x, turn):
        self.draw_triangle(color=RED)
        if self.side == 'H' or self.side == "P1":
            if keys[pygame.K_a] and not keys[pygame.K_d] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
            elif keys[pygame.K_d] and not keys[pygame.K_a] and self.x < (WIN_WIDTH - self.width):
                self.x += self.vel
                self.left = False
                self.right = True
            else:
                self.left = False
                self.right = False

            if self.left or self.right:
                self.walkCount += 1
            else:
                self.walkCount = 0

            if self.walkCount >= 18:
                self.walkCount = 0

            if turn == 1:
                if self.left:
                    WIN.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charHL, (self.x, self.y))
                    else:
                        WIN.blit(charHR, (self.x, self.y))
            elif turn == 2:
                if self.left:
                    WIN.blit(DwalkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(DwalkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charDL, (self.x, self.y))
                    else:
                        WIN.blit(charDR, (self.x, self.y))
            elif turn ==3:
                if self.left:
                    WIN.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charHL, (self.x, self.y))
                    else:
                        WIN.blit(charHR, (self.x, self.y))

            if not self.isJump:
                if keys[pygame.K_w]:
                    self.isJump = True
            else:
                if self.jumpCount >= -7:
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                    self.jumpCount -= 1
                else:
                    self.jumpCount = 7
                    self.isJump = False

        elif self.side == 'P' or self.side == "H1":
            self.draw_triangle(color=BLUE)
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
            elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.x < WIN_WIDTH - self.width:
                self.x += self.vel
                self.left = False
                self.right = True
            else:
                self.left = False
                self.right = False

            if self.left or self.right:
                self.walkCount += 1
            else:
                self.walkCount = 0

            if self.walkCount >= 18:
                self.walkCount = 0

            if turn == 1:
                if self.left:
                    WIN.blit(DwalkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(DwalkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charDL, (self.x, self.y))
                    else:
                        WIN.blit(charDR, (self.x, self.y))
            elif turn ==2:
                if self.left:
                    WIN.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charHL, (self.x, self.y))
                    else:
                        WIN.blit(charHR, (self.x, self.y))
            elif turn ==3:
                if self.left:
                    WIN.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                elif self.right:
                    WIN.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                else:
                    if opponent_x < self.x:
                        WIN.blit(charHL, (self.x, self.y))
                    else:
                        WIN.blit(charHR, (self.x, self.y))
                
            if not self.isJump:
                if keys[pygame.K_UP]:
                    self.isJump = True
            else:
                if self.jumpCount >= -7:
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                    self.jumpCount -= 1
                else:
                    self.jumpCount = 7
                    self.isJump = False