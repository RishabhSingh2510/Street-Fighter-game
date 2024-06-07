import pygame, random
from sprite import *
from Constants import *
pygame.init()

class Goku(pygame.sprite.Sprite):
    idleFrames = []
    walkingRightFrames = []
    walkingLeftFrames = []
    punchFrames = []
    kickFrames = []
    hitFrames = []

    def __init__(self):
        super(Goku, self).__init__()
        self.sprite = pygame.image.load("goku.png")
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 250
        self.h = 300

        self.loadIdle()
        self.loadWalkingLeft()
        self.loadWalkingRight()
        self.loadPunch()
        self.loadHit()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = WIDTH - 400
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
        if keypressed[pygame.K_l]:
            self.moveX = True
            self.move = self.SPEED
            self.showWalkingright()
        elif keypressed[pygame.K_j]:
            self.moveX = True
            self.SPEED = 40
            self.move = -self.SPEED
            self.showWalkingleft()
        elif keypressed[pygame.K_m]:
            self.isAttacking = True
            self.showPunch()
        else:
            self.move = 0
            self.showIdle()

        if self.moveX:
            self.rect.x += self.move

    def loadIdle(self):
        self.image = self.spritesheet.getImage(1, 584, 110, 116)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(111, 583, 110, 116)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(221, 583, 110, 116)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(331, 582, 110, 116)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(441, 582, 110, 116)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(551, 583, 110, 116)
        self.idleFrames.append(self.image)
    
    def loadHit(self):
        self.image = self.spritesheet.getImage(2, 5960, 104, 130)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(108, 5960, 104, 130)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(5, 6903, 75, 118)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(82, 6902, 75, 118)
        self.hitFrames.append(self.image)

    def loadWalkingRight(self):
        self.image = self.spritesheet.getImage(1, 8090, 99, 139)
        self.walkingRightFrames.append(self.image)
        self.image = self.spritesheet.getImage(101, 8091, 95, 139)
        self.walkingRightFrames.append(self.image)
    
    def loadWalkingLeft(self):
        self.image = self.spritesheet.getImage(2, 7950, 108, 135)
        self.walkingLeftFrames.append(self.image)
        self.image = self.spritesheet.getImage(112, 7950, 108, 135)
        self.walkingLeftFrames.append(self.image)
        

    def loadPunch(self):
        self.image = self.spritesheet.getImage(3, 1869, 145, 119)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(148, 1869, 145, 119)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(298, 1870, 145, 119)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(443, 1868, 145, 119)
        self.punchFrames.append(self.image)

    def showIdle(self):
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalkingright(self):
        if self.index >= len(self.walkingRightFrames):
            self.index = 0
        self.image = self.walkingRightFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1
    
    def showWalkingleft(self):
        if self.index >= len(self.walkingLeftFrames):
            self.index = 0
        self.image = self.walkingLeftFrames[self.index]
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