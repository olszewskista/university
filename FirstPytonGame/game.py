import pygame
import random
import sys

pygame.font.init()
pygame.mixer.init()

FPS = 60
assert FPS == 60
clock = pygame.time.Clock()

WIDTH = 840
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
assert WIDTH == 840
assert HEIGHT == 800

SCROLL = 0
TILES = 2

SPEED = 6
assert SPEED > 5
ENEMY_SPEED = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

RAVE = pygame.mixer.Sound('zasoby/rave.mp3')
START = pygame.mixer.Sound('zasoby/start.mp3')
SILNIK = pygame.mixer.music.load('zasoby/silnik.mp3')
CRASH = pygame.mixer.Sound('zasoby/crash.mp3')
HORN = pygame.mixer.Sound('zasoby/horn.mp3')
NITRO = pygame.mixer.Sound('zasoby/nitro.mp3')

ROAD = pygame.image.load('zasoby/droga2.png')
CAR_IMG = pygame.transform.scale(pygame.image.load('zasoby/lamboo.png').convert_alpha(), (80,160))
ENEMY1_IMG = pygame.transform.scale(pygame.image.load('zasoby/tir.png').convert_alpha(), (80,240))
ENEMY2_IMG = pygame.transform.scale(pygame.image.load('zasoby/policja.png').convert_alpha(), (80,160))
ENEMY3_IMG = pygame.transform.scale(pygame.image.load('zasoby/pickup.png').convert_alpha(), (80,160))
ENEMY4_IMG = pygame.transform.scale(pygame.image.load('zasoby/fura.png').convert_alpha(), (80,160))
MENU = pygame.image.load('zasoby/menu.png')
OVERSCR = pygame.image.load('zasoby/crash.png')


CAR = pygame.Rect(WIDTH/2, HEIGHT-200, 50, 130)


def main():
    global ENEMY1, ENEMY2, ENEMY3, ENEMY4, SCORE, HIGHSCORE
    SCORE = 0
    ENEMY1 = pygame.Rect(random.randint(180,220), random.randint(-1000,-200), 60, 220)
    ENEMY2 = pygame.Rect(random.randint(305,345), random.randint(-1000,-200), 60, 140)
    ENEMY3 = pygame.Rect(random.randint(435,475), random.randint(-1000,-200), 60, 140)
    ENEMY4 = pygame.Rect(random.randint(560,600), random.randint(-1000,-200), 60, 140)
    with open('zasoby/highscore.txt', 'r') as file:
        HIGHSCORE = file.read()
    menu()
    run_game = True
    while True:
        game()
        run_game = True
        over()
        
def menu():
    # SCREEN.fill(WHITE)
    SCREEN.blit(MENU,(0,0))
    RAVE.play()
    RAVE.set_volume(0.3)
    pygame.display.update()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return
                if event.key == pygame.K_2:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0)

def game():
    global run_game, ENEMY_SPEED
    SCOREFONT = pygame.font.SysFont('comicsans', 30)
    run_game = True
    counter = 0
    draw_background()
    draw_car()
    pygame.display.update()
    pygame.mixer.pause()
    START.play()
    pygame.time.delay(2000)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    ENEMY_SPEED = 0
    while run_game:
        clock.tick(FPS)

        counter += 1
        if counter == 500:
            ENEMY_SPEED += 1
            counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_e:
                    HORN.play()
                if event.key == pygame.K_LALT:
                    NITRO.play()
                    ENEMY_SPEED += 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LALT:
                    NITRO.stop()
                    ENEMY_SPEED -= 8
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and CAR.x > 150:
            CAR.x -= SPEED
        if keys_pressed[pygame.K_d] and CAR.x < WIDTH - 200:
            CAR.x += SPEED
        # if keys_pressed[pygame.K_LALT]:
            # ENEMY_SPEED = 8

        # print(counter,ENEMY_SPEED)

        SCORETEXT = SCOREFONT.render('Wynik: ' + str(SCORE), True, WHITE)
        HIGHSCORETEXT = SCOREFONT.render('Rekord: ' + HIGHSCORE, True, WHITE)

        draw_background()
        draw_car()
        draw_enemy1()
        draw_enemy2()
        draw_enemy3()
        draw_enemy4()
        loss()
        SCREEN.blit(SCORETEXT, (WIDTH - SCORETEXT.get_width() - 145, 30 ))
        SCREEN.blit(HIGHSCORETEXT, (WIDTH - SCORETEXT.get_width() - 145, 70))
        pygame.display.update()

def over():
    global HIGHSCORE
    # SCREEN.fill(RED)
    SCREEN.blit(OVERSCR, (0,0))
    pygame.mixer.music.stop()
    NITRO.stop()
    CRASH.play()
    pygame.display.update()
    if SCORE > int(HIGHSCORE):
        with open('zasoby/highscore.txt', 'w') as file:
            file.write(str(SCORE))
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main()
                if event.key == pygame.K_2:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_3:
                    with open('wynik.txt', 'w') as file:
                        file.write('Twoj wynik to: ' + str(SCORE))



def draw_background():
    global SCROLL
    for i in range(0, TILES):
        SCREEN.blit(ROAD, (0, i * -ROAD.get_height() + SCROLL))
        
    SCROLL += 20

    if SCROLL > ROAD.get_height():
        SCROLL = 0

def draw_car():
    # pygame.draw.rect(SCREEN, GREEN, CAR)
    SCREEN.blit(CAR_IMG, (CAR.x - 15, CAR.y))

def draw_enemy1():
    global SCORE
    # pygame.draw.rect(SCREEN, GREEN, ENEMY1)
    SCREEN.blit(ENEMY1_IMG, (ENEMY1.x - 10, ENEMY1.y))
    ENEMY1.y += ENEMY_SPEED + 10
    if ENEMY1.y > HEIGHT:
        ENEMY1.y = random.randint(-1200,-800)
        ENEMY1.x = random.randint(180,220)
        SCORE += 1

def draw_enemy2():
    global SCORE
    # pygame.draw.rect(SCREEN, GREEN, ENEMY2)
    SCREEN.blit(ENEMY2_IMG, (ENEMY2.x - 10, ENEMY2.y))
    ENEMY2.y += ENEMY_SPEED + 6
    if ENEMY2.y > HEIGHT:
        ENEMY2.y = random.randint(-1000,-200)
        ENEMY2.x = random.randint(305,345)
        SCORE += 1

def draw_enemy3():
    global SCORE
    # pygame.draw.rect(SCREEN, GREEN, ENEMY3)
    SCREEN.blit(ENEMY3_IMG, (ENEMY3.x - 10, ENEMY3.y))
    ENEMY3.y += ENEMY_SPEED + 8
    if ENEMY3.y > HEIGHT:
        ENEMY3.y = random.randint(-1000,-200)
        ENEMY3.x = random.randint(435,475)
        SCORE += 1

def draw_enemy4():
    global SCORE
    # pygame.draw.rect(SCREEN, GREEN, ENEMY4)
    SCREEN.blit(ENEMY4_IMG, (ENEMY4.x - 10, ENEMY4.y))
    ENEMY4.y += ENEMY_SPEED + 4
    if ENEMY4.y > HEIGHT:
        ENEMY4.y = random.randint(-1000,-200)
        ENEMY4.x = random.randint(560,600)
        SCORE += 1
 
def loss():
    global run_game
    if CAR.colliderect(ENEMY1):
         run_game = False
    if CAR.colliderect(ENEMY2):
         run_game = False
    if CAR.colliderect(ENEMY3):
         run_game = False
    if CAR.colliderect(ENEMY4):
         run_game = False


if __name__ == '__main__':
    main()