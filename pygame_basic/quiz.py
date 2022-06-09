# from lib2to3.pgen2 import pgen


# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 램덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 ㅈ오료
# 5. FPS는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 650 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - chrt.png
# 3. 똥 : 70 * 70 - enemy.png

import random
import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Escape poop")


clock = pygame.time.Clock()

background = pygame.image.load("/Users/cacaocoke/Documents/PythonWorkspace/pygame_basic/bg.png")

chrt = pygame.image.load("/Users/cacaocoke/Documents/PythonWorkspace/pygame_basic/dog.png")
chrt_size = chrt.get_rect().size
chrt_width = chrt_size[0]
chrt_height = chrt_size[1]
chrt_x_pos = (screen_width / 2) - (chrt_width / 2)
chrt_y_pos = screen_height - chrt_height
chrt_speed = 0.6

to_x = 0
to_y = 0

enemy = pygame.image.load("/Users/cacaocoke/Documents/PythonWorkspace/pygame_basic/poop.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 20

game_font = pygame.font.Font(None, 40)




running = True 
while running: 
    dt = clock.tick(30) 
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= chrt_speed
            elif event.key == pygame.K_RIGHT:
                to_x += chrt_speed   
        if event.type == pygame.KEYUP: # KEYPUP은 키를 떼는 구문 대문자로 적어줘야 함 # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    # 3. 게임 캐릭터 위치 정의
    chrt_x_pos += to_x * dt 

    if chrt_x_pos < 0:
        chrt_x_pos = 0
    elif chrt_x_pos > screen_width - chrt_width:
        chrt_x_pos = screen_width - chrt_width
    
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
    
    # 4. 충돌 처리
    chrt_rect = chrt.get_rect()
    chrt_rect.left = chrt_x_pos
    chrt_rect.top = chrt_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if chrt_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기

    screen.blit(background, (0,0))
    screen.blit(chrt, (chrt_x_pos,chrt_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기 지속 리프레쉬


pygame.quit()