# Assignment:- Create lower triangular, upper triangular and pyramid containing the "*" character.

print("Lower Triangular Pattern")
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()



print("Upper Triangular Pattern")
n = 4

for i in range(n):
    for space in range(i):
        print("  ", end="")
    for j in range(n - i):
        print("*", end=" ")
    print()

print("Pyramid Pattern")
n = 4

for i in range(1, n + 1):
    for space in range(n - i):
        print("  ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

