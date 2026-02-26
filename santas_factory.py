from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(el) for el in input().split()])
total_magic_level = 0
toys = {}
items = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while materials and magic_level:
    total_magic_level = materials[-1] * magic_level[0]
    if total_magic_level in items:
        current_present = items[total_magic_level]
        if current_present not in toys:
            toys[current_present] = 0
        toys[current_present] += 1
        materials.pop()
        magic_level.popleft()
    elif total_magic_level < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif total_magic_level > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()

if ('Doll' in toys and 'Wooden train' in toys) or ('Teddy bear' in toys and 'Bicycle' in toys):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
for present, amount in sorted(toys.items()):
    print(f"{present}: {amount}")