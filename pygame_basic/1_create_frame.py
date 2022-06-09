import pygame
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 창의 가로 크기
screen_height = 640 # 창의 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Coke game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running: # while로 무한 루프를 걸어 줌
    for event in pygame.event.get(): # 파이게임을 쓰기 위해서는 무조건 적어야 함 # 어떤 이벤트가 발생하였는지를 확인
        if event.type == pygame.QUIT: # 창 닫힘 버튼을 눌렀을때 while을 탈출 시키는 이벤트 구문
            running = False

# pygame 종료
pygame.quit()