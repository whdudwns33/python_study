#평균은 넘겠지
m = int(input())
for i in range(m):
    s = []
    n = []
    n = list(map(int,input().split()))
    average = sum(n[1:]) / len(n[1:])
    for e in n :
        if e > average:
            s.append(e)
    print()
    print(f"{((len(s) / len(n[1:])) * 100):.3f} %")