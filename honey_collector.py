from collections import deque


def operation(bee, operator, material):
    global result
    if operator == "+":
        result = bee + material
    elif operator == "-":
        result = bee - material
    elif operator == "*":
        result = bee * material
    elif operator == "/":
        result = bee / material
    return result


bees = deque(map(int, input().split()))
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while len(bees) > 0 and len(nectar) > 0:
    if bees[0] <= nectar[-1]:
        total_honey += abs(operation(bees.popleft(), symbols[0], nectar.pop()))
        symbols.popleft()
    elif bees[0] > nectar[-1]:
        nectar.pop()
        continue

print(f"Total honey made: {total_honey}")
if len(bees) > 0:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif len(nectar) > 0:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
