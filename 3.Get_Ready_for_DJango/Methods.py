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

porche = Car(color="green", price="$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color ,mini.price)