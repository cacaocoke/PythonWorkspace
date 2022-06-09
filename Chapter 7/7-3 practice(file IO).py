'''
score_file = open("score.txt", "w", encoding="utf8") # 'w'는 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
'''

'''
score_file=open("score.txt", "a", encoding="utf8") # 'a'는 내용 더하기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write를 통할땐 줄바꿈이 따로 없어 '\n' 로 줄바꿈 해줘야 함
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
'''

'''
score_file=open ("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 end=""로 줄 바꿈 없이
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8") #파일이 몇줄 인줄 모를때 모두 불러오기
while True: # 무한루프
    line = score_file.readline()
    if not line:
        break
    print(line, end="") 
score_file.close()
'''

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()