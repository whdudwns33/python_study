v = [[1,4], [3,4], [3, 10]]

def sol(v) :
    x1, y1 = v[0][0], v[0][1]
    x2, y2 = v[1][0], v[1][1]
    x3, y3 = v[2][0], v[2][1]
    x4, y4 = 0, 0

    if x1 == x2 :
        x4 = x3
    elif x1 == x3 :
        x4 = x2
    else :
        x4 = x1

    if y1 == y2 :
        y4 = y3
    elif y1 == y3 :
        y4 = y2
    else:
        y4 = y1

    return [x4, y4]

print(f"result : {sol(v)}")
