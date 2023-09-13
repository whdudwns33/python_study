# 피타고라스
while True:
    a, b, c = map(int, input().split())
    if a*a + b*b == c*c :
        print("right")
    elif a == 0 or b == 0 or c == 0:
        break
    else:
        print("wrong")
