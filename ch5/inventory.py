stuff = {'rope': 1,
         'torch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print()
    print('Total number of items:', item_total)

# display_inventory(stuff)

def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        print('added_items[',i,']:', added_items[i])
        # if added_items[i] in inventory:
        #     inventory[i] += 1
        # else:
        #     inventory.setdefault(i, 1)
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] += 1

inv = {'gold coin': 42, 'rope': 1}
dragons_loot = ['gold coin', 'gold coin', 'ruby', 'rope', 'gold coin', 'gold coin', 'gold coin',
                'gold coin', 'dagger', 'ruby']

add_to_inventory(inv, dragons_loot)
display_inventory(inv)