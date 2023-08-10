import pygame
from inventory import Item
import textures
import utils

class item_slot:
    def __init__(self, item: Item):
        self.item = item
        self.surf: pygame.surface = None
        self.font = pygame.font.Font(None, 8)

    def draw(self) -> pygame.surface.Surface:
        if not self.surf: self.update()
        return self.surf

    def update(self):
        item_frame = pygame.image.load(textures.item_frame)
        item_image = pygame.image.load(textures.items[self.item.id])
        item_count = self.font.render(str(self.item.count), False, (0, 0, 0))

        self.surf = pygame.surface.Surface([50, 50])
        self.surf.blit(item_frame, [0, 0])
        self.surf.blit(item_image, [1, 1])
        self.surf.blit(item_count, [39, 39])

class gui:
    def __init__(self, player):
        self.master = player
        self.structure = {"type":"item-slot", "link":"master.inventory.0"}
        self.surface: pygame.surface.Surface = None
        self.inited = False

    def compile(self, struct):
        if type(struct) == dict:
            if struct["type"] == "item-slot":
                item = utils.link_parser(struct["link"], self)
                print(item)
                self.structure = [item_slot(item)]
                self.structure[0].update()

        elif type(struct) == list:
            pass

        self.inited = True

    def draw(self, win, pos):
        if not self.surface: self.update()
        win.blit(self.surface, pos)

    def update(self):
        if not self.inited: self.compile(self.structure)
        self.surface = self.structure[0].draw()           

    def size(self):
        if not self.surface: self.update()
        return [self.surface.get_width(), self.surface.get_height()]