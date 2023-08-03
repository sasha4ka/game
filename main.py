import pygame

class object:
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

    def click(self, mouse_pos: list):
        pass

class objects_list:
    def __init__(self):
        pass

    def add_object(self, object: object) -> int:
        pass

    def remove_object(self, id: int):
        pass

class game:
    def __init__(self, size, title):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.title = title
        self.size = size
        self.pos = [0, 0]
        self.last_pos = [0, 0]

        self.objects = []

    def update(self, frame: int):
        pass

    def update_objects(self, frame: int):
        self.pos = self.last_pos
        self.pos = pygame.mouse.get_pos()

        for object in self.objects:
            object.update(frame)
        
        if self.pos != self.last_pos:
            for object in self.objects:
                object.mouse(self.pos)

    def draw_objects(self, frame: int):
        for object in self.objects:
            object.draw(self.win)

    def start(self):
        pass