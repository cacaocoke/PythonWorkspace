# 구글에 list of python modules 검색
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir과 같음)

#import glob
#print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능


# import os
'''
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else :
    os.makedirs(folder) # 폴더가 없을 경우 폴더 생성
    print(folder,"폴더를 생성하였습니다.")
'''

# print(os.listdir()) # glob과 비슷하게 사용 됨

'''
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # month는 m / Minute는 M
'''

import datetime
#print ("오늘 날짜는 ", datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘을 기준으로 지정
td = datetime.timedelta(days=100) # 100일 뒤를 지정
print("우리가 만난 지 100일은", today+td) # 오늘 날짜로 부터 100일 뒤를 계산
