s = []
while True :
    m = int(input())
    if m <= 1000:
        if m % 42 not in s:
            s.append(m % 42)
    elif m > 1000:
        break
    else:
        s = s
print(s)
print(len(s))