import pygame

class Object:
    def __init__(self, pos: list, color: list, type=0, speed=[0, 0]):
        self.pos = pos
        self.color = color
        self.speed = speed
        self.type = type
    
    def draw(self, win: pygame.surface):
        pass

    def update(self, frame: int):
        pass

    def mouse(self, mouse_pos: list):
        pass

    def click(self, mouse_pos: list, mouse_button: list):
        pass