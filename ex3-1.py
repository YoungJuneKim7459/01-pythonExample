# ex2-8.py
# 조건문
# 특정 조건이 참일 때만, 코드를 실행하게 한다. 선택적 실행

# if 조건(절, True 또는 False):
#     조건이 True일 때 실행될 코드(들여쓰기 필수!)

# 단순 if문
score = 85
if score >= 60:
    print("합격입니다!")

age = 15
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다")

# if elif문
month = 6
if month <=3:       # month가 3이하인가?
    print("1,2,3월")
elif month <=6:     # 아니면 6이하인가?
    print("4,5,6월")

# if elif else문
month = 6
if month <= 3:
    print("1,2,3월")
elif month <= 6:
    print("4,5,6월")
else:                  # 그러면 나머지 조건
    print("그외의 월")
        

# 연습문제
score = 80
if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
elif score >= 60:
    print('D학점')

import random
random_int = random.randint(0, 2)
print( random_int )
if random_int == 0:
    print("오늘의 날씨는 비 입니다. 우산을 챙기세요!")
if random_int == 1:
    print("오늘의 날씨는 흐림입니다. 나들이 가기 좋을 수도 있어요.") 
if random_int == 2:
    print("오늘의 날씨는 맑음입니다. 화창한 하루 되세요!")


score = input('마이클 영어점수:87')
scoreInt = int(score)
if scoreInt >= 90:
    print('A학점')
elif scoreInt >= 80:  # 아니면, 80점 이상이면
    print('B학점')
elif scoreInt >= 70:  # 아니면, 70점 이상이면
    print('C학점')
else:                # 아니면, 나머지  
    print('D학점')

if random_int == 0:
    print("오늘의 날씨는 비 입니다. 우산을 챙기세요!")
elif random_int == 1:
    print("오늘의 날씨는 흐림입니다. 나들이 가기 좋을 수도 있어요.")
else:
    print("오늘의 날씨는 맑음입니다. 화창한 하루 되세요!")




