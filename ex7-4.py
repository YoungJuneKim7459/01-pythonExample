# ex7-4.py
# 클래스 상속 : 부모 클래스의 자산(변수와 함수)을 자식 클래식에 넘겨주는 것

# 부모 클래스
class Animal:
    age = 0
    def sleep(self):
        print("잔다")

# 자식 클래스
class Dog(Animal):  # 강아지 = 동물 + 강아지 고유
    def sleep(self):
        print("강아지가 잔다")
    pass    

# 자식 클래스  
class Cat(Animal):  # 고양이 = 동물 + 고양이 고유
    pass

dog = Dog()
print(dog.age)
dog.sleep() # 강아지가 잔다.
 
cat = Cat()
print(cat.age)

# 클래스 다중 상속
class Flyable:
    def fly(self):
        print("날 수 있다.")

class Bird(Animal, Flyable):
    pass

bird = Bird()
bird.fly()
bird.sleep()

