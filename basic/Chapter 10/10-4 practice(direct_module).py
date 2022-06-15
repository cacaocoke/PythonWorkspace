from travel import * # *을 쓴다는 건 패키지내 모든 걸 가져 오겠다는 의미 지만 실제로는 개발자가 문법상에서 공개 범위를 설정 해줘야 함 
#패키지 내에서 원하는건 공개로 하고 원치 않는 건 비공개 할 수 있다.

trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()

# 이 강좌 공부할때 travel.thailand 내용을 내,외부 호출용으로 추가 구문 작성 함