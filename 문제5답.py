#영화표 예제
TICKET_PRICE = 12000
seat = [0] * 10


# 좌석 상태를 표시하는 함수
def print_seat() :
    for e in seat: # 향상된 for문으로 좌석의 개수만큼 순회
        if e == 0:
            print("[ ]", end=" ") #판매 안된 좌석
        else:
            print("[V]", end=" ") #판매된 좌석
    print()

# 총 매출액을 구하기
def amount () :
    cnt = 0
    for e in seat:
        if e == 1:
            cnt += 1    # 팔린좌석의 총 개수 구하기
    return cnt * TICKET_PRICE

# 좌석 예약하기
def sel_seat():
    print_seat()# 현재 예약가능한 좌석 보여주기
    num = int(input("좌석 번호를 선택하세요 : ")) - 1 #선택된 좌석번호는 1부터 시작하고 인덱스는 0부터 시작, 따라서 -1
    if seat[num] == 0:
        seat[num] = 1
        print_seat()
    else:
        print("이미 예약된 좌석입니다.")

while True:
    sel = int(input("[1]예매하기 [2]종료 :"))
    if sel == 1:
        sel_seat()
    else:
        print(f"총 매출액:{amount()}")
        break





