#다음의 함수 만들기
#x+y | x-y | x*y | x/y | x//y | x%y | -x | x**y
#유저는 멍청해서 plus(12, "10") 이렇게 사용할 수도 있음 -> 이것도 수정
#이 7가지 연산자로 계산기를 만들어라.

def plus(a, b):
    return int(a) + int(b)

def minus(a,b):
    return int(a) - int(b)

def multiply(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b)

def floored(a,b):
    return int(a) // int(b)

def remainder(a,b):
    return int(a) % int(b)

def negated(a):
    return int(a) * -1

def pow(a,b):
    return int(a) ** int(b)

print(plus(2,3))
print(minus(2,"3"))
print(multiply(3,5))
print(divide(50,20))
print(floored(3,5))
print(remainder(9,2))
print(negated(20))
print(pow(20,3))