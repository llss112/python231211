import pygame
import sys
from pygame.locals import *

# 초기화
pygame.init()

# 화면 설정
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 20
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 5, 5

# 블럭 설정
block_width, block_height = 50, 20
blocks = []
for row in range(5):
    for col in range(10):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle_x += (keys[K_RIGHT] - keys[K_LEFT]) * 5

    # 경계 체크
    paddle_x = max(0, min(width - paddle_width, paddle_x))

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 경계 체크 및 반사
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    # 패들과의 충돌 체크
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # 블럭과의 충돌 체크
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)
    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)