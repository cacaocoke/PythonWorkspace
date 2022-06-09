# 프로그램 상에서 이용하고 있는 데이터를 파일로 저장 하는 거
import pickle
# profile_file = open("profile.pickle", "wb") # 'b'는 Binary이며 pickle 사용할땐 반드시 사용해야 함
# profile = {"이름" : "박명수", "나이": 30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()