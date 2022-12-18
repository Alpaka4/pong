import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH=1920
SCREEN_HEIGHT=1000
 
# здесь происходит инициация,
# создание объектов

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
ORANGE = (255,155,100)
BLACK = (0,0,0)
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
 
# радиус круга
r = 20
# координаты круга
# скрываем за левой границей
ball_x = SCREEN_WIDTH//2
# выравнивание по центру по вертикали
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x=3
ball_speed_y=4
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # передвигаем мяч по экарну
    ball_x+=ball_speed_x
    ball_y+=ball_speed_y
    #выход за левый кран экрана
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x=-ball_speed_x
    if ball_x>= SCREEN_WIDTH - r:
        #летел направо - полетел налево
        ball_speed_x= -ball_speed_x
    #выход за верхний край
    if ball_y>= SCREEN_HEIGHT - r:
        #летел наверх-полетел вниз
        ball_speed_y=-ball_speed_y
    #выход за нижний край
    if ball_y<=r:
        #летел вниз-полетел наверх
        ball_speed_y=-ball_speed_y
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    # обновляем окно
    pygame.display.update()
 
    # Если круг полностью скрылся
    # за правой границей,
    
 
    clock.tick(FPS)
