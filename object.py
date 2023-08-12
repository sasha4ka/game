import pygame
from handler import handler
from inventory import Item as item
import utils
import textures
import objects_list

class Object:
    def __init__(self, color: list, pos: list, speed=[0, 0]):
        self.rect = pygame.rect.Rect(*pos, 50, 50)
        self.color = color
        self.speed = speed
        self.type = 0
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

class Gravity_object(Object):
    def __init__(self, color: list, pos=[0, 0], speed=[0, 0]):
        self.rect = pygame.rect.Rect(*pos, 50, 50)
        self.color = color
        self.speed = speed
        self.type = 0
        self.master: objects_list.objects_list = None
        self.active = False

        self.onGround = False
        self.gravspeed = 0
        self.tickrate = None

        self.title = "Object"

    def update(self, frame: int):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

        self.gravity(frame)
        self.rect.top += self.gravspeed

        if not self.master: return
        if self.rect.bottom >= self.bottom:
            self.rect.bottom = self.bottom
            self.onGround = True
            self.gravspeed = 0
        else:
            self.onGround = False

    def gravity(self, frame):
        if not self.tickrate: return
        if self.onGround: return

        self.gravspeed += utils.g / self.tickrate
    
    def on_master_initilazed(self):
        self.tickrate = self.master.get_framerate()
        self.bottom = self.master.get_screensize()[1]

class Item(Gravity_object):
    def __init__(self, item: item, pos=[0, 0], speed=[0, 0]):
        self.rect = pygame.rect.Rect(*pos, 50, 50)
        self.speed = speed
        self.type = 2
        self.master = None
        self.active = False

        self.item = item
        self.item_id = self.item.id
        self.old_item_id = self.item.id
        if self.item_id != "empty": self.texture = pygame.image.load(textures.items[self.item.id])
        else: self.texture = None

        self.onGround = False
        self.gravspeed = 0
        self.tickrate = None

        self.title = "Item"
    
    def draw(self, win):
        if self.item_id != self.old_item_id:
            self.texture = pygame.image.load(textures.items[self.item_id])
        if self.texture:
            win.blit(self.texture, self.rect.topleft)

    def update(self, frame: int):
        super().update(frame)

        self.old_item_id = self.item_id
        self.item_id = self.item.id        

        if not self.master: return
        collide = self.master.get_collide_list(self)
        collide = [obj for obj in collide if obj.type==1]
        min_dist = 100
        min_player = None
        for player in collide:
            dist = utils.dist(*player.rect.center, *self.rect.center)
            if dist > min_dist: return
            min_player = player

        if min_player and min_player.inventory.add(self.item):
            min_player.inventory_gui.update()
            self.master.remove_object(self)