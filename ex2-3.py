# 연습문제

print("Python is easy!")

s = "Hello Python"
print( s[0] )
print( s[-1] )
print( s[0] + " " + s[-1] )

s = "Life is short, use Python"
print( s[15:] )

a = "Python"
b = " is fun"
print(a + b)

print("Hi" *3)

print("I ate %d apples" % 5)

str = "banana"
print( str.count('a') )

try:
    a = "hello"
    print( a.find('e'))
    print( a.find('z'))
    print( a.index('e'))
    print( a.index('z'))
except ValueError:
    print("값을 찾을 수 없습니다.")

fruit = "apple, banana, grape"
print( fruit.split(','))

s = "I love Java"
print( s.replace("Java","Python"))