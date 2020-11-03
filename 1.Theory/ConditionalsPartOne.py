def plus(a,b):
    if type(b) is str:
        return None
    else:
        return a+b

def minus(a,b):
    if type(b) is int or type(b) is float:
        return a-b
    else:
        return None

print(plus(12, "10"))
print(minus(12, "3"))
print(minus(12, 1.2))