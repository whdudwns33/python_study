#평균은 넘겠지
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
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