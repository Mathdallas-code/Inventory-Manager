from ..Invila.modules.itemHandler import add_item, view_items
from ..Invila.modules.item import Item

item = Item("Chocolate", 15, 6, 12, 9, 15, 20)
add_item(item=item)
print(view_items())
