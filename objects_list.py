from main import handler
from object import Object

class objects_list:
    def __init__(self, master, objects=[]):
        self.master = master
        self.object_list = objects

    def add_object(self, object: Object) -> int:
        object.master = self
        self.object_list.append(object)
        object.on_master_initilazed()

    def remove_object(self, id: int):
        pass

    def get_active_object(self) -> Object:
        active = None
        for obj in self.object_list:
            if not obj.active: continue
            active = obj
        
        return active

    def get_hold_mouse(self) -> list:
        return self.master.get_hold_mouse()
    
    def get_mouse_pos(self):
        return self.master.get_mouse_pos()
    
    def get_hold_keys(self):
        return self.master.get_hold_keys()
    
    def get_framerate(self) -> int:
        return self.master.get_framerate()
    
    def get_screensize(self) -> list:
        return self.master.get_screensize()
    
    def add_handler(self, handler: handler):
        self.master.add_handler(handler)
    
    class objects_list_iterator:
        def __init__(self, objects: list):
            self.objects = objects
            self._pos = 0
        
        def __next__(self):
            if self._pos < len(self.objects):
                obj = self.objects[self._pos]
                self._pos += 1
                return obj
            else:
                raise StopIteration

    def __iter__(self):
        return self.objects_list_iterator(self.object_list)