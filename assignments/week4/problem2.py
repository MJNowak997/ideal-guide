def print_triangular_numbers(n):
    x = 0
    r = 0
    for i in range(1, n+1):
        r = 1 + r + x
        x = x + 1
        r = r
        print(i, "    ", r)

print_triangular_numbers(5)