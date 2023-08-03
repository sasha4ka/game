import pygame
from main import handler
from object import Object

class objects_list:
    def __init__(self, master, objects=[]):
        self.master = master
        self.object_list = objects

    def add_object(self, object: Object) -> int:
        pass

    def remove_object(self, id: int):
        pass

    def get_hold(self):
        return self.master.get_hold()
    
    def add_handler(self, handler: handler):
        self.master.add_handler(handler)
    
    class objects_list_iterator:
        def __init__(self, objects: list):
            self.objects = objects
            self._pos = 0
        
        def __next__(self):
            if self._pos < len(self.objects):
                self._pos += 1
                return self.objects[self._pos]
            else:
                raise StopIteration

    def __iter__(self):
        return self.objects_list_iterator(self.object_list)