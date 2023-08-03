import pygame
from object import Object
from objects_list import objects_list

class handler:
    def __init__(self, criteria: int, payload: function):
        self.criteria = criteria
        self.payload = payload
    
    def test(self, event):
        return self.criteria == event
    
    def run(self, event, frame):
        self.payload(event, frame)

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

        self.objects = objects_list()
        self.handlers = []

    def update(self, frame: int):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                0/0

            for handler in self.handlers:
                if not handler.test(event.type): continue
                handler.run(event, frame)

        self.pos = self.last_pos
        self.pos = pygame.mouse.get_pos()

        self.hold = pygame.mouse.get_pressed()

        self.update_objects(frame)
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
    
    def add_handler(self, handler: handler):
        self.handlers.append(handler)