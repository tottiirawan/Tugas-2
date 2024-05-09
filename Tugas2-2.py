def print_odd_squares(n):
    for i in range(n):
        if i % 2 != 0:
            print(i**2)

n = int(input("Masukkan nilai n: "))

print_odd_squares(n)
