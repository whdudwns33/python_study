#평균은 넘겠지
m = int(input())
for i in range(m):
    s = []
    n = []
    n = list(map(int,input().split()))
    average = sum(n) / len(n)
    for e in n :
        if e > average:
            s.append(e)
    print(f"{(len(s) / len(n)) * 100} %")