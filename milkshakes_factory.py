from collections import deque

chocolate = [int(x) for x in (input().split(", "))]
milk = deque(map(int, input().split(", ")))
shakes_prepared = 0

while shakes_prepared < 5 and len(chocolate) != 0 and len(milk) != 0:
    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        shakes_prepared += 1
    elif chocolate[-1] <= 0:
        chocolate.pop()
        continue
    elif milk[0] <= 0:
        milk.popleft()
        continue
    elif chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    elif chocolate[-1] != milk[0] and chocolate[-1] != 0 and milk[0] != 0:
        milk.append(milk.popleft())
        chocolate[0] -= 5

if shakes_prepared >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print(f"Chocolate: empty")
if len(milk) > 0:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print(f"Milk: empty")

