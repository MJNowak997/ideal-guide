def print_triangular_numbers(n):
    x = 0
    p = 0
    for i in range(1, n+1):
        r = 1 + p + x
        x = x + 1
        p = r
        print(i, "    ", r)

print_triangular_numbers(5)