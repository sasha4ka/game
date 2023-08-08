import pygame
import objects_list
from object import Object, Player
from handler import handler

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

    def mainloop(self):
        while True:
            self.update(self.frame)
            self.frame = (self.frame + 1) % self.framerate
            self.clock.tick(self.framerate)

def main():
    main_game = game((400, 400), "game", 10)
    obj = Player([175, 175, 50, 50], (255, 0, 0))
    main_game.add_object(obj)
    obj = Object([0, 0, 50, 50], (0, 0, 0))
    main_game.add_object(obj)
    main_game.mainloop()

if __name__ == "__main__":
    main()