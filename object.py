import pygame

class Object:
    def __init__(self, pos: list, color: list, type=0, speed=[0, 0]):
        self.pos = pos
        self.color = color
        self.speed = speed
        self.type = type
        self.master = None
    
    def draw(self, win: pygame.surface):
        pygame.draw.rect(win, self.color, self.pos)

    def update(self, frame: int):
        pass

    def mouse(self, mouse_pos: list):
        pass