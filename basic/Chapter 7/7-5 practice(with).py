'''
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # 종료 선언 없이 바로 종료
'''

'''
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
'''

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())