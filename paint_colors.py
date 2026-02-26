from collections import deque
text = deque(input().split())
list_of_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
found = []


def check(c, box):
    if c == 'orange' and 'red' in box and 'yellow' in box:
        return True
    elif c == 'purple' and 'red' in box and 'blue' in box:
        return True
    elif c == 'green' and 'yellow' in box and 'blue' in box:
        return True
    elif c == 'red' or c == 'yellow' or c == 'blue':
        return True
    else:
        return False


while text:
    first = text.popleft()
    last = text.pop() if text else ''
    for color in (first + last, last + first):
        if color in list_of_colors:
            found.append(color)
            break
    else:
        if len(first) > 1:
            text.insert((len(text) // 2), first[:-1])
        if len(last) > 1:
            text.insert((len(text) // 2), last[:-1])

for el in found:
    if not check(el, found):
        found.remove(el)

print(found)