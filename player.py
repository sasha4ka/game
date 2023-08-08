import utils
import pygame
from handler import handler
from object import Object

class Player(Object):
    def __init__(self, pos: list, color: list, type=1, speed=[0, 0], master = None):
        pos[2] = 50
        pos[3] = 70
        self.rect = pygame.rect.Rect(*pos)
        self.color = color
        self.speed = speed
        self.type = type
        self.master = master
        self.tickrate = None

        self.onGround = False
        self.gravspeed = 0

        self.title = "Player"
    
    def update(self, frame: int):
        self.move()
        
        if frame == 0 and self.master.get_platform_collide_list(self):
            print(f"Collide!")

        self.gravity(frame)
        self.rect.top += self.gravspeed

        if self.rect.bottom >= self.bottom:
            self.rect.bottom = self.bottom
            self.onGround = True
            self.gravspeed = 0
        else:
            self.onGround = False

        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

    def move(self):
        if self.master == None: return
        keys = self.master.get_hold_keys()

        move_speed = [0, 0]
        if keys[pygame.K_d]:
            move_speed[0] += utils.horizontal_speed / self.tickrate
        if keys[pygame.K_a]:
            move_speed[0] -= utils.horizontal_speed / self.tickrate

        self.rect.left += move_speed[0]
        self.rect.top += move_speed[1]
    
    def on_master_initilazed(self):
        key_handler = handler(pygame.KEYDOWN, self.on_key)
        self.master.add_handler(key_handler)
        self.tickrate = self.master.get_framerate()
        self.bottom = self.master.get_screensize()[1]
    
    def on_key(self, event: pygame.event.Event, frame: int):
        if event.key != pygame.K_SPACE: return
        if not self.onGround: return
        self.gravspeed -= utils.jump_force
        self.onGround = False

    def gravity(self, frame):
        if not self.tickrate: return
        if self.onGround: return

        self.gravspeed += utils.g / self.tickrate
