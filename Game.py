import pygame, random
from Constants import *
from Player1 import *
from Player2 import *
from PlayerHealth import *
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)
# SCREEN = pygame.display.set_mode()

sprite_group = pygame.sprite.Group()
venom = Venom()
sprite_group.add(venom)

goku = Goku()
sprite_group.add(goku)

venomSprite = pygame.sprite.Group()
venomSprite.add(venom)

gokuSprite = pygame.sprite.Group()
gokuSprite.add(goku)
healthWidth = WIDTH//2 - 100
venomHealth = Health("Venom", 10, 10, healthWidth, 50)
gokuHealth = Health("Goku", WIDTH - healthWidth - 10, 10, healthWidth, 50)
def drawHealth():
    venomHealth.showHealth(SCREEN)
    venomHealth.showName(SCREEN)

    gokuHealth.showHealth(SCREEN)
    gokuHealth.showName(SCREEN)

def showTimer(time_left):
    font = pygame.font.SysFont(None, 100)
    text = font.render(f"{time_left}", True, RED)
    SCREEN.blit(text, (WIDTH//2 - 40, 10))

def main():
    bgImage = pygame.image.load("bg.jpg")

    clock = pygame.time.Clock()
    FPS = 10

    pygame.time.set_timer(USEREVENT + 1, 1000)
    seconds = 45

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1

        SCREEN.blit(bgImage, (0, -120))


        if pygame.sprite.groupcollide(venomSprite, gokuSprite, False, False):
            if venom.isAttacking:
                goku.currentMove = HIT
                gokuHealth.rect_2.w += 10
            elif goku.isAttacking:
                venom.currentMove = HIT
                venomHealth.rect_2.w += 10
            print("Collision Detection")
            venom.moveX = False
            venom.SPEED = 0
            goku.moveX = False
            goku.SPEED = 0

        drawHealth()
        showTimer(seconds)
        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
