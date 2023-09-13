#배수찾기
n = int(input())
ls = []
while True:
    x = int(input())
    if x == 0:
        break
    ls.append(x)

for e in ls:
    if e % n == 0:
        print(f"{e} is a multiple of {n}.")
    else:
        print(f"{e} is NOT a multiple of {n}.")