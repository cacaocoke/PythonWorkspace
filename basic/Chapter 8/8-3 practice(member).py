class Unit:  # 'class 유닛이름 :' 형식으로 선언
    def __init__(self, name, hp, damage): # _ _ init _ _ 파이썬에서 쓰이는 생성자, 객체가 만들어 질때 자동 호출 
        self.name = name # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.". format(self.name))
        print("체력 {0}, 공격력{1}". format(self.hp, self.damage))

# marine1 = Unit("마린",40, 5) # 객체, 클래스의 인스턴스 __init___ 안에 정보 갯수와 같이 입력해야 함
# marine2 = Unit("마린",40, 5)
# # marine2 = Unit("마린",40) 이 경우 damage 값이 없다고 나옴
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은레이스", 80, 5)
wraith2. clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
    