n = int(input())
for i in range(n):
    for a in range(n - i - 1):
        print(" ", end="")
    for b in range(2*i + 1):
        print("*", end="")
    print()
for i in range(n):
    for c in range(i + 1):
        print(" ", end="")
    for d in range(2*(n - i - 1) - 1):
        print("*",end="")
    print()


