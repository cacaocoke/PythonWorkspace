class Unit:  # 'class 유닛이름 :' 형식으로 선언
    def __init__(self, name, hp, damage): # _ _ init _ _ 파이썬에서 쓰이는 생성자, 객체가 만들어 질때 자동 호출 
        self.name = name # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.". format(self.name))
        print("체력 {0}, 공격력{1}". format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage): # _ _ init _ _ 파이썬에서 쓰이는 생성자, 객체가 만들어 질때 자동 호출  
        self.name = name # 멤버 변수
        self.hp = hp
        self.damage = damage
    def attack(self, location): # self는 자기 자신을 의미함, 클래스 내에서 method 앞에는 '무조건' self를 적어준다
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃, 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받았다고 가정
firebat1.damaged(25)
firebat1.damaged(25)