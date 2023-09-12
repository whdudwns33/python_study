#영화표 예매하기
seat_set = [] # v표시 좌석
seat = [0] * 10
cnt: int = 0 # 좌석 수

def total(cnt):
    return cnt * 12000

def sel_seat():
    print(seat)
    sel = int(input("좌석 선택:"))
    seat[sel - 1]
    if seat[sel - 1] == 0:
        seat[sel - 1] = 1
        global cnt += 1
    elif seat[sel - 1] == 1:
        print("좌석이 있습니다.")



while True :
    m = int(input("[1]예매하기 [2]종료"))
    if m == 1:
        sel_seat()
    elif m == 2:
        break
    else :
        print("다시 입력하시오.")




