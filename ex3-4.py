# ex3-4.py
# 연습문제
# 자판기 프로그램을 작성하시오.
# 사용자가 1을 입력하면, 콜라가 나옵니다
# 2를 입력하면 "사이다가 나옵니다"
# 3을 입력하면 "오렌지쥬스가 나옵니다"
# 콜라의 잔고는 3개
# 오렌지의 잔고는 4개 입니다.
# 잔고 소진시 "콜라(사이다, 오렌지쥬스) 잔고가 떨어졌습니다."라고 출력하시오.

stock_cola = 3
stick_soda = 2
stock_juice = 4
while True:
    menu = int(input('콜라(1) 사이다(2) 오렌지쥬스(3):'))
    if menu ==1:       
        print("콜라가 나옵니다")
        stock_cola <= 0
        print("콜라 잔고가 떨어졌습니다")
        continue
    elif menu == 2: 
        print("사이다가 나옵니다")
        stock_soda <= 0
        print("사이다 잔고가 떨어졌습니다")
        continue
    elif menu == 3:
        print("오렌지 쥬스가 나옵니다")
        stock_juice <= 0
        print("오렌지쥬스 잔고가 떨어졌습니다")
        continue
    elif menu == 10:
        print("자판기 프로그램을 종료합니다.")
    else:
        print("메뉴번호를 확인해 주세요~")
    

# 연습문제2 텍스트 야구게임(무한루프) 작성
# 투수가 공을 던지는데, 스트라이크 확률이 70%, 볼 확률이 30%입니다.
# 투수가 공을 계속 던졌을 때 볼 카운트(스트라이크와 볼)을 출력하시오.
# 확률은 rand.randint()함수를 이용합니다.
# 출력예시 
# 1번 송구 : 스트라이크 - 1스트라이크 0볼
# 2번 송구 : 볼 - 1스트라이크 1볼
# 3번 송구 : 스트라이크 - 2스트라이크 1볼
# 4번 송구 : 스트라이크 - 3스트라이크 1볼 - 스트라이크 아웃!
# 게임끝
# 게임종료 조건 : 3스트라이크 이거나 4볼이면 종료됩니다.

import random

ball_type = 0  # 0 ball 1 strike
ball_count = 0
strike_count = 0
count = 1
while True:
    ball = random.randint(0, 100) # 1~100까지의 랜덤수
    if ball <= 70:
        ball_type = 1 # strike
    else:
        ball_type = 0 # ball
    if ball_type == 1:
        strike_count += 1
        print(f"{count}번째 송구 : 스트라이크") 
        if strike_count >= 3:
        print("스트라이크 아웃!")
        break
    else:
        ball_count += 1
        print(f"{count}번째 송구 : 볼")
        if ball_count >= 4:
        print("볼넷!")    
    count += 1    
        


