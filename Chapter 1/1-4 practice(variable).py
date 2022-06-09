# 애완동물을 소개해 주세요~
animal = "고양이"
name = "나비"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal +"의 이름은 "+ name +"예요") # 변수 불러올땐 '+' 표시로 감싸기 또는 ','로 마무리
hobby = "그루밍"
#print(name +"는 "+ str(age) +"살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(""+ name +"는 어른일까요? " + str(is_adult))