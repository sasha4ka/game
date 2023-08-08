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

        self.title = "Object"
    
    def draw(self, win: pygame.surface):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self, frame: int):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

    def test_platform_collide(self, other):
        other_rect = other.rect

        vert_test = other_rect.bottom < self.rect.top and self.rect.top-5 > other_rect.bottom
        horizont_test = (other_rect.left - other_rect.width/2 > self.rect.left) and (other_rect.right + other_rect.width/2 < self.rect.right)
        return vert_test and horizont_test
    
    def test_collide(self, other):
        return self.rect.colliderect(other)

    def mouse(self, mouse_pos: list):
        if mouse_pos[0] > self.rect.left and mouse_pos[0] < self.rect.right:
            if mouse_pos[1] > self.rect.top and mouse_pos[1] < self.rect.bottom:
                self.active = True
                return
        
        self.active = False

    def on_master_initilazed(self):
        pass