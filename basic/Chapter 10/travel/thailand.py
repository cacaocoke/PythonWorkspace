class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 모듈 내에서 직접 실행인지 외부에서 실행인지 구분
# 아래 내용은 외부에서 호출 시 외부에서 모듈을 호출 했다는 내용을 포함 함

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈 을 직접 실행할 때만 실행 돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")