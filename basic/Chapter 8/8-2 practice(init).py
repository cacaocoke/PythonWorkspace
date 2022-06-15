class Unit:  # 'class 유닛이름 :' 형식으로 선언
    def __init__(self, name, hp, damage): # _ _ init _ _ 파이썬에서 쓰이는 생성자, 객체가 만들어 질때 자동 호출 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.". format(self.name))
        print("체력 {0}, 공격력{1}". format(self.hp, self.damage))
marine1 = Unit("마린",40, 5) # 객체, 클래스의 인스턴스 __init___ 안에 정보 갯수와 같이 입력해야 함
marine2 = Unit("마린",40, 5)
# marine2 = Unit("마린",40) 이 경우 damage 값이 없다고 나옴
tank = Unit("탱크", 150, 35)