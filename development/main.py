import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class player :
    lives = 0
    points = 0
    playerSpeed = 5
    playerSprite = pygame.image.load("../art/spr_Player.PNG")
    playerRect = playerSprite.get_rect()
    def __init__(self, levens):
        self.lives = levens
    def update(self):
        if (KEYS_DOWN[K_w]):
            playerRect.y -= playerSpeed
        elif (KEYS_DOWN[K_s]):
            playerRect.y += playerSpeed

        if (KEYS_DOWN[K_a]):
            playerRect.x -= playerSpeed
        elif (KEYS_DOWN[K_d]):
            playerRect.x += playerSpeed
    def draw(self):
        SCREEN.fill(BG_COLOUR)


player1 = player(3)


playerSprite = player.playerSprite
playerRect = player.playerRect
playerSpeed = player.playerSpeed


while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    player1.update()

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    player1.draw()

    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)

    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
