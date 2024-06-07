import pygame, random
from sprite import *
from Constants import *
pygame.init()

class Venom(pygame.sprite.Sprite):
    idleFrames = []
    walkingFrames = []
    punchFrames = []
    kickFrames = []
    hitFrames = []
    def __init__(self):
        super(Venom, self).__init__()
        self.sprite = pygame.image.load("venom.png")
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 200
        self.h = 250

        self.loadIdle()
        self.loadWalking()
        self.loadPunch()
        self.loadHit()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = 300
        self.rect.y = self.ground - self.h - 60
        self.moveX = True
        self.SPEED = 40
        self.move = 0
        self.index = 0
        self.currentMove = IDLE
        self.isAttacking = False


    def update(self):
        if self.currentMove == MOVE:
            pass
        elif self.currentMove == KICK:
            pass
        elif self.currentMove == HIT:
            self.showHit()
        else:
            self.showIdle()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_d]:
            self.moveX = True
            self.move = self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_a]:
            self.moveX = True
            self.SPEED = 40
            self.move = -self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_z]:
            self.isAttacking = True
            self.showPunch()
            self.isAttacking = False
        else:
            self.move = 0
            self.showIdle()

        if self.moveX:
            self.rect.x += self.move

    def loadIdle(self):
        self.image = self.spritesheet.getImage(145, 167, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(276, 169, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(410, 168, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(544, 168, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(677, 170, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(806, 168, 113, 151)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(940, 168, 113, 151)
        self.idleFrames.append(self.image)
    
    def loadHit(self):
        self.image = self.spritesheet.getImage(3, 5959, 117, 91)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(286, 5928, 202, 126)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(506, 5911, 201, 149)
        self.hitFrames.append(self.image)
        

    def loadWalking(self):
        self.image = self.spritesheet.getImage(5, 3248, 128, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(162, 3247, 112, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(303, 3246, 107, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(439, 3246, 128, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(596, 3250, 140, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(759, 3246, 125, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(909, 3245, 100, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(1032, 3247, 118, 127)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(5, 3385, 135, 127)
        self.walkingFrames.append(self.image)

    def loadPunch(self):
        self.image = self.spritesheet.getImage(2, 681, 144, 91)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(335, 667, 144, 96)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1, 842, 137, 98)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(165, 843, 220, 98)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(404, 836, 156, 103)
        self.punchFrames.append(self.image)

    def showIdle(self):
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalking(self):
        if self.index >= len(self.walkingFrames):
            self.index = 0
        self.image = self.walkingFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showPunch(self):
        if self.index >= len(self.punchFrames):
            self.index = 0
        self.image = self.punchFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showHit(self):
        if self.index >= len(self.hitFrames):
            self.index = 0
            self.currentMove = IDLE
        self.image = self.hitFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1