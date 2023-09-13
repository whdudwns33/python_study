# 배수 찾기
n = int(input())
ls = []
while True:
    m = int(input())
    if m % n == 0:
        print(f"{m} is a multiple of {n}.")
    else:
        print(f"{m} is NOT a multiple of {n}.")
    if m == 0:
        break


