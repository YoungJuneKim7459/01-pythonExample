# ex6-1.py
# 파일 입출력

# 파일 생성하기

# w 쓰기, r 읽기전용, a 추가
f = open("test1.txt", 'w')
f.write('테스트 파일입니다.')
f.close() # 파일닫기
