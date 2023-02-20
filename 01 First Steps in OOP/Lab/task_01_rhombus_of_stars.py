def print_rows(num, row):
    for space in range(num - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=' ')
    print("*")


def print_upper_part(num):
    for row in range(1, num + 1):
        print_rows(num, row)


def print_lower_part(num):
    for row in range(num - 1, 0, -1):
        print_rows(num, row)


def print_rhombus(num):
    print_upper_part(num)
    print_lower_part(num)


n = int(input())
print_rhombus(n)
