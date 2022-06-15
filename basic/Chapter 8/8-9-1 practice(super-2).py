from re import U


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # super 이용시 다중상속 하면 마지막에 상속받는 클래스에 대해서만 __init__ 함수가 호출 된다
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽

dropship = FlyableUnit()