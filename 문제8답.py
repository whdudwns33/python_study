# 피타고라스
rst = []    # 결과출력을 위한 빈리스트
while True:
    n = list(map(int, input().split()))
    n.sort()
    if n[0] == 0 and n[1] == 0 and n[2] == 0:
        break
    elif n[0]**2 + n[1]**2 == n[2]**2:
        rst.append("right")
    else:
        rst.append("wrong")
print(rst)