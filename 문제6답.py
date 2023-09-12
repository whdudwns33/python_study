# A = int(input("고정비용 :"))
# b = int(input("가변비용 :"))
# price = int(input("판매가격 :"))
A, b, price = map(int, input().split())
n = 1
bem = b / (price * n)

#
# while True :
#     if (n > A//(price - b)):
#         break
#     n += 1
# print(n)

if price > b:
    print((A // (price - b)) + 1)
else:
    print(-1)


