def plus(*args):
    result = 0
    for num in args:
        result += num
    return result

print(plus(1,2,3,4,5,6,7,8,9,10))