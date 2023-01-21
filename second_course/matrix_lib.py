def print_matrix_kvadrat(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def print_matrix_not_kvadrat(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def print_matrix_not_kvadrat_reverse(matrix, n, m, width=1):
    for r in range(m):
        for c in range(n):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()