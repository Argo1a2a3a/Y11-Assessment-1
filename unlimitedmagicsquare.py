def test(name, expected, actual):
    if expected == actual:
        print(f"Test {name} passed: {actual}")
    else:
        print(f"Test {name} failed: expected {expected}, but got {actual}")

def is_square_magic(square):
    n = len(square)  
    for row in square:
        if len(row) != n:
            return False 
    
    target_sum = sum(square[0])  
    for row in square:
        if sum(row) != target_sum:
            return False

    for col_index in range(n):
        column_sum = sum(square[row_index][col_index] for row_index in range(n))
        if column_sum != target_sum:
            return False

    main_diagonal_sum = sum(square[i][i] for i in range(n))
    if main_diagonal_sum != target_sum:
        return False

    secondary_diagonal_sum = sum(square[i][n - 1 - i] for i in range(n))
    if secondary_diagonal_sum != target_sum:
        return False

    return True  
print("Enter the size of the square (e.g., 3 for a 3x3 square):")
size = int(input())
square = []

print(f"Enter the square row by row (each row should have {size} numbers separated by spaces):")
for _ in range(size):
    row = list(map(int, input().split()))
    square.append(row)

if is_square_magic(square):
    print("The entered square is a valid magic square!")
else:
    print("The entered square is NOT a valid magic square!")
