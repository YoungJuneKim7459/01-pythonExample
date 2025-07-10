# ex3-3.py
# while문  - for문(60%)

# 형식
# 반복변수 초기화
# while 조건절:
#    조건절이 True일 때 반복적으로 수행되는 코드
#    반복변수 증감

# 5초 카운트다운
count = 5
while count > 0:
    print(f"{count}")
    count -= 1   # 복합대입 연산자 A -= B -> A = A - B
print( "발사!" )

# 반복문을 사용시 무한루프에 빠지는 경우
# 1. 콘솔을 클릭후 CTRL + C 키로 빠져나온다.
# 2. 콘솔 세션을 종료 - 휴지통 버튼을 클릭한다.
# 3. VScode를 껐다 켠다.
# 4. 작업관리자에서 python 프로세스 끝내기를 한다.

# 무한루프 만들기 - 자판기, 엘리베이터 프로그램
count = 0
while True:
    if count > 10:
        break    # 반복문을 종료한다.
    print(f"무한루프 - {count}")
    count += 1
print("무한루프 종료!")    

# continue 문 : 해당 회차를 종료하고 반복문의 처음으로 돌아간다.
# 1부터 10사이의 홀수만 출력하기
for i in range(1, 11):
    if i % 2 == 0:  #짝수이면
        continue    #해당 회차 종료, 아랫쪽 print문을 건너뜀
    print(i)

# 연습문제 1. while문을 이용하여 1부터 10사이의 짝수 출력 continue문(건너뛰기) 사용
num = 1
while num < 11:
    if num % 2 == 0:
        print(num)
    num += 1    

num = 1
while num < 11:
    if num % 2 == 1:
        continue
    print(num)
    num += 1    
# 런타임(실행시) 디버거 사용
# 1. 중단점을 찍는다.
# 2. 실행 및 디버그 실행
# 3. F10 으로 step over 실행

# 연습 2. while문을 이용해 1부터 100사이의 2의 배수이면서 5의 배수인 수 출력
num = 1
while num < 101:
    if num % 2 == 0 and num % 5 == 0:
        print(num)
    num += 1

# 연습 3. 무한루프를 이용해 사용자로부터 정수(1~10사이)를 입력받고, 1~9 사이면, 그 수를 출력하고, 10이면 종료하는 프로그램 작성 한트(break)
while True:
    n = int(input("1~10사이의 정수 입력: "))
    if 0 <= n <= 9:
        print(n)
    elif n == 10:
        print("10 종료!")
        break
    else:
        print("1~10사이의 정수가 아닙니다.")
print("무한루프 종료")

# 연습 4. 구구단 3단을 출력하는 프로그램 출력
for i in range(1,10):
    print(f"3 x {1} = {3*i}")

# 연습 5. while문을 사용하여 사용자가 입력한 숫자의 자릿수를 세어서 출력
# 예시 : 12345 입력 -> "5자리 숫자입니다" 789->"3자리 숫자입니다"  힌트-숫자를 10으로 나누면서 0이 될때까지 반복
n = int(input("정수를 입력하세요: "))
count = 1
while True:
    n = n // 10
    if n == 0:
        break
    count += 1
print(f"{count}자리 숫자입니다.")