# A = int(input("고정비용 :"))
# b = int(input("가변비용 :"))
# price = int(input("판매가격 :"))
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


while True:
    if price > b:
        print((A // (price - b)) + 1)
        break
    else:
        print(-1)
        break

