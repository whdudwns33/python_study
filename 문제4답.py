# 평균은 넘겠지 답
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

def over_rate(): # 각케이스에서 평균이 넘는 비율을 구하기
    ls = list(map(int,input().split()))
    average = sum(ls[1:]) / len(ls[1:]) # 0번째 배열의 수는 인원수이므로 제외, 총합/ 인원수 = 평균
    cnt = 0 # 평균이 넘는 %를 구하기 위해서는 인원이 필요함. 즉, 평균이 넘는 인원 구하기를 위한 변수
    for i in range (1, len(ls)): # 0번째열의 요소를 제외하기 위함.
        if ls[i] > average :
            cnt += 1
    return (cnt / (len(ls)-1)) * 100 # %(백분율)로 표현

n = int(input())    #총 테스트 횟수
rst = []            #각 case에 대한 결과값을 받기 위한 리스트

for i in range(n):  #총 테스트 횟수만큼 반복 수행
    rst.append(over_rate())

for e in rst:
    print(f"{e:.3f}%")

