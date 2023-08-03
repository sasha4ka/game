import pygame
from object import Object

class objects_list:
    def __init__(self, master):
        self.master = master

    def add_object(self, object: Object) -> int:
        pass

    def remove_object(self, id: int):
        pass

    def get_hold(self):
        return self.master.get_hold()

class game:
    def __init__(self, size, title):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.title = title
        self.size = size

        self.pos = [0, 0]
        self.last_pos = [0, 0]
        self.hold = [False, False, False]

        self.objects = []

    def update(self, frame: int):
        self.pos = self.last_pos
        self.pos = pygame.mouse.get_pos()

        self.hold = pygame.mouse.get_pressed()

        self.update_objects()
        self.draw_objects()

    def update_objects(self, frame: int):
        for object in self.objects:
            object.update(frame)
        
        if self.pos != self.last_pos:
            for object in self.objects:
                object.mouse(self.pos)

    def draw_objects(self, frame: int):
        for object in self.objects:
            object.draw(self.win)

    def get_hold(self):
        return self.hold