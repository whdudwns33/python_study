#1.
# ls = list(map(int,input().split()))
# min_b = min(ls[:3])
# min_d = min(ls[3:])
# print(f"{min_b + min_d - 50}")

#2.
color = "black", "brown", "red", "orange", "yello", "green", "blue", "violet", "grey", "white" # 튜플로 저장.
f_name = color.index(input())   # input으로 입력받은 문자열이 color 튜플에 몇번째 인덱스에 있는지 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))

#3.
# seat_num = list(map(int,input().split()))
# pc = [0] * 100 # 0으로 초기화된 100개의 리스트 생성
# cnt = 0
# for e in seat_num: #향상된 for문 고객이 안고싶어하는 좌석 번호
#     if pc[e - 1] != 0 : # 사용하는 자리
#         cnt += 1
#     else: pc[e - 1] = 1
# print(cnt)

#4.
# kmp_str = ""
# for e in input() : #입력받은 문자열수만큼 향상된 for문 순회
#     if e.isupper() : kmp_str += e
# print(kmp_str)