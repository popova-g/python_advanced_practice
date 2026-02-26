size = int(input())
initial_energy = 4
energy = initial_energy
matrix = []

possible_commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

robot_position = None
for row_index in range(size):
    row_data = input().split()
    if "R" in row_data:
        col_index = row_data.index("R")
        robot_position = (row_index, col_index)
    matrix.append(row_data)

start_position = robot_position
matrix[start_position[0]][start_position[1]] = "."

steps = 0

while steps < 10 and energy < 14:
    command = input()

    if command not in possible_commands:
        continue

    steps += 1
    move_row, move_col = possible_commands[command]
    new_row = robot_position[0] + move_row
    new_col = robot_position[1] + move_col

    if not (0 <= new_row < size and 0 <= new_col < size):
        robot_position = start_position
        continue

    robot_position = (new_row, new_col)
    step = matrix[new_row][new_col]

    if step == "E":
        energy += 2
    elif step == "A":
        energy -= 2
    elif step == "S":
        energy *= 2
    matrix[new_row][new_col] = "."

    if energy >= 14:
        break

    if energy <= 0:
        break

matrix[robot_position[0]][robot_position[1]] = "R"

if energy >= 14:
    print(f"Robot wins! Energy units: {energy}")
else:
    print(f"Mission failed! Energy units: {energy}")

for row in matrix:
    print(" ".join(row))