import pygame
from handler import handler

class Object:
    def __init__(self, pos: list, color: list, type=0, speed=[0, 0]):
        self.rect = pygame.rect.Rect(*pos)
        self.color = color
        self.speed = speed
        self.type = type
        self.master = None
        self.active = False
    
    def draw(self, win: pygame.surface):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self, frame: int):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

    def mouse(self, mouse_pos: list):
        if mouse_pos[0] > self.rect.left and mouse_pos[0] < self.rect.right:
            if mouse_pos[1] > self.rect.top and mouse_pos[1] < self.rect.bottom:
                self.active = True
                return
        
        self.active = False

    def on_master_initilazed(self):
        pass