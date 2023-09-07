#1.
n = int(input("정수 입력 :"))
a = n//100
b = n % 100 // 10
c = n % 10 // 10
if a > b :
    if a > b :
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

#2.
근무타입 = int(input("주간근무[1] 야간근무[2] :"))
근무시간 = int(input("근무시간 입력 :"))
if 근무타입 == 1:
    급여 = 근무시간 * 9620
else :
    급여 = 근무시간 * 9620 * 1.5

근무타입문자열 = 근무타입 == 1 and "주간" or "야간"
print(f"{근무시간}시간 동안 {근무타입문자열}근무 급여는 {급여}원 입니다.")

#3.
s = input("s 문자열 입력: ")
k = input("k 문자열 입력: ")
n = int(input("정수 입력: "))
print(s[len(s) - n:] + k)
print(s[-n:] + k)




