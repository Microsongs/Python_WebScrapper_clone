def minus(a,b):
    return a-b

result = minus(b=30, a=1)
print(result)

def say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"

def say_hello2(name, age):
    return "Hello " + name + "you are " + age + "years old"

hello = say_hello(name="nico", age="12", fav_food="kimchi", are_from="colombia")
print(hello)