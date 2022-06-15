# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e'(1) rottn + "!"(!) 로 구성
# 생성된 비밀번호 : nav51!

url="http://google.com"
slice=url.replace("http://", "") # 규칙 1
slice=slice[:slice.index(".")] # 규칙 2
password=slice[:3]+str(len(slice))+str(slice.count("e"))+"!" # 규칙 3

print(f"{url}의 비밀번호는 {password} 입니다.")

