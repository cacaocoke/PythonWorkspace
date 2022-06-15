import pygame
import os
############################################################
# 기본 초기화 (반드시 해야 하는 것들)#

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 창의 가로 크기
screen_height = 640 # 창의 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Coka Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################

############################################################
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # 이미지 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))
# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용
# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러발 발사 가능
weapons = [] # 리스트 선언

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)

running = True 
while running: 
    dt = clock.tick(30) 
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) # 무기의 x좌표와 y좌표를 리스트에 등록

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


   
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 100, 200 -> 180, 160 , 140, ...
    # 500, 200 -> 180, 160 , 140, ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 한 줄 for 활용 # 무기 위치를 위로

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if  w[1] > 0 ]

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 윗줄에 입력 할 수록 레이어가 밑으로 깔림

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    

    pygame.display.update() # 게임화면을 다시 그리기 지속 리프레쉬


pygame.quit()