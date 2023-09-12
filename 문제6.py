#
A, b, price = map(int, input().split())
n = 1
bem = b / (price * n)


#
# while True:
#     if price * n < A + (b * n) :
#         n += 1
#     elif price * n >= A + (b * n) :
#         print(n + 1)
#         break
#     else:
#         print(-1)


if price > b:
    print((A // (price - b)) + 1)
else:
    print(-1)
