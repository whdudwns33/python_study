# 조건문 연습 문제
# 1.세자리 정수를 입력 받아 가장 큰 수 찾기
n1, n2, n3 = map(int, input("정수입력 : ").split())
if n1 > n2 :
    if n1 > n3 :
        print(n1)
    else:
        print(n3)
else:
    if n2 < n3:
        print(n3)
    else:
        print(n2)


# 2. 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간: 9620
# 야간: 주간 * 1.5
# 주간근무[1] 야간근무[2]
# 근무시간
# # 입력한 시간 동안 근무한 급여는 ---원 입니다.
t1, t2 = map(int,input("근무시간을 입력하시오: [1] 주간 [2] 야간").split())
if t1 > 0: # 주간 근무
    day_pay = t1 * 9620
    if t2 > 0: # 주간 및 야간
        night_pay = t2*9620*1.5
        print(f"주/야간 급여 : {day_pay + night_pay}")
    else: # 야간은 안함
        print(f"주간 급여 : {day_pay}")
else: #주간은 안함
    night_pay = t2 * 9620 * 1.5
    print(f"야간 급여 : {night_pay}")


# 3. 문자열 추가하기.
# 2개의 문자열을 포인터 변수 s, k에
# 양의 정수를 정수형 변수 n에 각각 전달 받아 s열 문자 뒷 부분에 n개의 문자를 k열 앞까지
# 삽입하는 코드 작성
# s: seoul
# k: korea
# n : 2
# 결과 : ulkorea
s = "seoul"
k = "korea"
n = int(input("정수 입력: "))
a = str(s[-n:])
print(a+k)

