m = int(input())

for i in range(m):
    r, s = map(str, input().split())
    S = list(s[:])
    R = int(r)
    for i in range(len(S)):
        print(S[i]*R, end="")
    print()


