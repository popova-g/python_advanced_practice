def calculate_next_point(direction, current_row_index, current_col_index, N, M):
    if direction == "down":
        current_row_index += 1
    elif direction == "up":
        current_row_index -= 1
    elif direction == "left":
        current_col_index -= 1
    elif direction == "right":
        current_col_index += 1

    return current_row_index, current_col_index


N, M = [int(el) for el in input().split(", ")]


matrix = []
counter_terrorist = None
seconds = 16
on_bomb = False  # Flag to track if CT is standing on a bomb

# Load matrix and find the counter-terrorist's starting position
for row_index in range(N):
    row_data = list(input())
    if "C" in row_data:
        col_index = row_data.index("C")
        counter_terrorist = (row_index, col_index)
    matrix.append(row_data)

command = input()
while seconds > 0:
    if command == "defuse":
        if on_bomb:
            if seconds >= 4:
                seconds -= 4
                matrix[counter_terrorist[0]][counter_terrorist[1]] = "D"  # Bomb defused
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {seconds} second/s remaining.")
                break
            else:
                print("Bomb was not defused successfully!")
                print(f"Time needed: {4 - seconds} second/s.")
                break  # End the game
        else:
            # Move from the bomb without defusing, continue game
            on_bomb = False  # No longer standing on a bomb
            seconds -= 2  # Failed defusal attempt costs 2 seconds
            if seconds <= 0:
                print("Terrorists win!")
                break
            continue
    next_row_i, next_col_i = calculate_next_point(command, counter_terrorist[0], counter_terrorist[1], N, M)
    if 0 <= next_row_i < N and 0 <= next_col_i < M:
        element = matrix[next_row_i][next_col_i]
        # Check if the terrorist is at the next position
        if element == "T":
            matrix[counter_terrorist[0]][counter_terrorist[1]] = "*"  # Mark previous position
            matrix[next_row_i][next_col_i] = "*"  # Mark terrorist position
            print("Terrorists win!")
            break  # End the game
        # Check if there's a bomb at the next position
        elif element == "B":
            seconds -= 1  # Deduct 1 second for the move
            matrix[counter_terrorist[0]][counter_terrorist[1]] = "*"  # Mark previous position
            counter_terrorist = (next_row_i, next_col_i)
            matrix[next_row_i][next_col_i] = "C"  # Place counter-terrorist on bomb
            on_bomb = True
        else:
            matrix[counter_terrorist[0]][counter_terrorist[1]] = "*"  # Mark the previous spot
            counter_terrorist = (next_row_i, next_col_i)
            matrix[next_row_i][next_col_i] = "C"
            seconds -= 1  # Each move costs 1 second
            if seconds <= 0:
                print("Terrorists win!")
                break  # End the game:
    command = input()
for row in matrix:
    print("".join(row))
