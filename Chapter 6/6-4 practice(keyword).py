def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", age=25, main_lang="파이썬")
profile(main_lang="자바", age=20, name="김태호") # 순서를 뒤바꿔도 앞서 선언 된 순서에 따라 출력 됨