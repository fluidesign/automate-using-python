#Fantasy Game Inventory

playerInventory = {}

def display_inventory(playerInventory):
    print('Inventory:')
    if len(playerInventory.values()) == 0:
        print('Currently empty')
    for key, value in playerInventory.items():
        print(key + ':' + str(value))
    
def add_to_inventory(item):
    global playerInventory
    if item in playerInventory.keys():
        playerInventory[item] = playerInventory[item] + 1
    else:
        playerInventory.setdefault(item,1) ## make sure to add the right type | int/string
    
while True:
    display_inventory(playerInventory)
    print('Enter a new item to add, blank to exit')
    newItem = str(input())
    if newItem != '':
        add_to_inventory(newItem)
    else:
        break
