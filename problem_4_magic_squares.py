def test(name, expected, actual):
    if expected == actual:
        print(f"Test {name} passed: {actual}")
    else:
        print(f"Test {name} failed: expected {expected}, but got {actual}")

def is_square_magic(square):
    target_sum = sum(square[0])

    for row in square:
        if sum(row) != target_sum:
            return False

    for col_index in range(len(square)):
        column_sum = sum(square[row_index][col_index] for row_index in range(len(square)))
        if column_sum != target_sum:
            return False

    main_diagonal_sum = sum(square[i][i] for i in range(len(square)))
    if main_diagonal_sum != target_sum:
        return False

    secondary_diagonal_sum = sum(square[i][len(square) - 1 - i] for i in range(len(square)))
    if secondary_diagonal_sum != target_sum:
        return False

    return True


size = 3
square = []

print(f"Enter the square row by row (each row should have {size} numbers separated by spaces):")
for _ in range(size):
    row = list(map(int, input().split()))
    square.append(row)

if is_square_magic(square):
    print("The entered square is a valid magic square!")
else:
    print("The entered square is NOT a valid magic square!")
