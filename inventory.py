class Item:
    def __init__(self, count: int, id: str = "empty"):
        self.count = count
        self.id = id
    
    def __iadd__(self, other: int):
        self.count += other
    
    def __isub__(self, other: int):
        self.count += other
    
    def __str__(self) -> str:
        return f"{self.id}, {self.count}"

class Inventory: 
    def __init__(self, slots: int):
        self.inventory: list[Item] = [None for i in range(slots)]
        self.size = slots
    
    def remove_item_by_index(self, index: int):
        self.inventory[index] = None
    
    def set_item_by_index(self, item: Item, index: int):
        self.inventory[index] = item

    def get_item_by_index(self, index: int) -> Item:
        return self.inventory[index]
    
    def __str__(self) -> str:
        return "\n".join(f"{i}: {self.inventory[i]}" for i in range(len(self.inventory)) if self.inventory[i])
    
    def __len__(self) -> int:
        return len(self.inventory)
    
    def __getitem__(self, key: int) -> Item:
        return self.inventory[key]
    
    def __setitem__(self, key: int, value: Item):
        self.inventory[key] = value