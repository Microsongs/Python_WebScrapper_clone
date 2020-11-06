class Car():
    # 생성자
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        # kwargs가 없으면 black과 $20을 넣어준다.
        self.color = kwargs.get("color","black")
        self.price = kwargs.get("price","$20")        

    # 오버라이드
    def __str__(self):
        return f"Car with {self.wheels} wheels"

    def take_off(self):
        return "taking off"

class ConvertibleCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return "Car with no roof"

class Something(ConvertibleCar):
    pass

porche = ConvertibleCar(color = "Green", price = "$40")
porche.take_off()
print(porche.__str__())
print(porche.color)