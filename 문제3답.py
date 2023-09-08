#1.
ls = list(map(int,input().split()))
min_b = min(ls[:3])
min_d = min(ls[3:])
print(f"{min_b + min_d - 50}")