import pygame
import objects_list
from object import Object
from player import Player
from handler import handler
from inventory import Item, Inventory

class game:
    def __init__(self, size, title, framerate=20):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.title = title
        self.size = size

        self.pos = [0, 0]
        self.last_pos = [0, 0]
        self.hold_mouse = [False, False, False]
        self.hold_keys = []

        self.objects = objects_list.objects_list(self)
        self.handlers = []

        self.frame = 0
        self.framerate = framerate
        self.clock = pygame.time.Clock()

        self.player = None

    def update(self, frame: int):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                0/0

            for handler in self.handlers:
                if not handler.test(event.type): continue
                handler.run(event, frame)

        self.pos = self.last_pos
        self.pos = pygame.mouse.get_pos()

        self.hold_mouse = pygame.mouse.get_pressed()
        self.hold_keys = pygame.key.get_pressed()

        self.update_objects(frame)
        self.draw_objects()

    def update_objects(self, frame: int):
        for object in self.objects:
            object.update(frame)
        
        if self.pos != self.last_pos:
            for object in self.objects:
                object.mouse(self.pos)

    def draw_objects(self):
        self.win.fill((200, 200, 200))
        for object in self.objects:
            object.draw(self.win)
        pygame.display.update()

    def get_hold_mouse(self):
        return self.hold_mouse
    
    def get_hold_keys(self):
        return self.hold_keys

    def get_framerate(self):
        return self.framerate
    
    def get_screensize(self):
        return self.size
    
    def add_handler(self, handler: handler):
        self.handlers.append(handler)
    
    def add_object(self, object: Object):
        self.objects.add_object(object)
    
    def get_mouse_pos(self):
        return [self.pos, self.last_pos]
    
    def set_player(self, player: Player):
        self.player = player
    
    def get_player(self):
        return self.player

    def mainloop(self):
        while True:
            self.update(self.frame)
            self.frame = (self.frame + 1) % self.framerate
            self.clock.tick(self.framerate)

def main():
    main_game = game((800, 800), "game", 20)
    player = Player([175, 175], (255, 0, 0))
    player.inventory.set_item_by_index(Item(4, "gold"), 0)
    obj = Object([0, 750, 50, 50], (0, 0, 0))
    main_game.add_object(player)
    main_game.add_object(obj)
    main_game.set_player(player)
    main_game.mainloop()

if __name__ == "__main__":
    main()