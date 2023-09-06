# 1. 정해진 형식으로 시간을 입력받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초 출력
from datetime import datetime

hour, min, sec = map(int, input("시:분:초 :").split())
if (hour > 12) :
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}") # 수를 두칸으로 출력하고 한칸 남으면 0을 넣어 달라는 의미
else:
    print(f"오전{hour:02}시{min:02}분{sec:02}")


# 2. 3개의 정수를 입력받아서 최대값 최소값 구하기
n1, n2, n3 = map(int, input("정수 입력 :").split())
if n1 > n2 :
    if n1 > n3 :
        print(n1)
    else :
        print(n3)
elif n1 < n2 :
    if n2 > n3 :
        print(n2)
    else :
        print(n3)
elif n1 == n2 :
    if n1 < n3 :
        print(n3)
    else :
        print(n1)
elif n1 == n3:
    if n1 < n2:
        print(n2)
    else:
        print(n1)
else :
    print()

#3. 주민등록번호 입력받아서 생년 월일 , 성별, 나이 출력하기
#980612-1234567
current_year = datetime.today().year
id = input("주민 번호 입력 : ")
year = id[:2]
month = id[2:4]
day = id[4:6]
gender = id[7]
age = (current_year - (int(year) + 1900))

print(f"year : {year}")
print(f"month : {month}")
print(f"day : {day}")

if bool(int(gender)) == 1 :
    print("남성")
else :
    print("여성")

print(f"age : {age}")

# 4. 갯수가 정해지지 않은 여러개의 정수 입력 받아서 합계와 평균 구하기
num = list(map(int, input("숫자를 입력 하시오 :").split())) # i는 요소 하나하나를 계산함.
sum = 0
for i in num:
    sum += int(i)
print(sum)

# lenth = len(list)
# while True :
#     sum += int(num[i])
