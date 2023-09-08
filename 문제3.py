#리스트 연습문제.
#1. 상근날드(초급)800 700 900 198 330

# arr = list(map(int, input().split()))
# hb = min(arr[:3])
# dr = min(arr[3:])
# print(dr + hb - 50)

#2. 저항문제(중급)
# 저항색: black, brown, red, orange, yello, green, blue, violet, grey, white

# rg = ["black", "brown", "red", "orange", "yello", "green", "blue", "violet", "grey", "white"]
# n = [0,1,2,3,4,5,6,7,8,9]
#
# c1, c2 , c3 = input("색입력").split()
# for i in range (len(rg)):
#     if c1 == rg[i]:
#         a = n[i]*10
#
# for i in range (len(rg)):
#     if c2 == rg[i]:
#         b = n[i]
#
# for i in range (len(rg)):
#     if c2 == rg[i]:
#         c = 10**(i)
# print((a+b)*c)

#3. pc방 알바(중급)

seat = []
cnt = 0
h = int(input("손님 수:"))
while True:
    for i in range(h):
        num = int(input("좌석입력:"))
        if num < 100 and num not in seat :
            seat.append(num)
        elif num in seat :
            print("거절")
            cnt += 1
        elif num >100:
            print(sorted(seat))
            print(f"거절횟수: {cnt}")
            break

        else:
            print("다시 입력")



#4. KMP 암호 문제
#
# str = list(input().split("-"))
# val = " "
# for i in range(0,len(str),1):
#     val = str[i][0].upper()
#     print(val,end="")




