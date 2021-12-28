# Modules
import pygame
import math
import math

pygame.init()

screen = pygame.display.set_mode((745,477))
pygame.display.set_caption("Grief")
background = pygame.image.load("background.png")


# Player1:
playerimg1 = pygame.image.load("playerR1.png")
playerx1 = 45
playery1 = 395
playerx1_change = 7
playery1_change = 41
pressed_right1 = False
pressed_left1 = False
Jump1 = False
def player1(playerx1,playery1):
    screen.blit(playerimg1,(playerx1,playery1))



# Player2:
playerimg2 = pygame.image.load("playerL2.png")
playerx2 = 700
playery2 = 395
playerx2_change = 7
playery2_change = 41
pressed_right2 = False
pressed_left2 = False
Jump2 = False
def player2(playerx2,playery2):
    screen.blit(playerimg2,(playerx2,playery2))


# Physics:
v1 = 8
m1 = 1

v2 = 8
m2 = 1



# Platforms
grassimg = pygame.image.load("grass.png")
goldimg = pygame.image.load("gold.png")
goodimg = pygame.image.load("lume.png")
inimg = pygame.image.load("in.png")
outimg = pygame.image.load("out.png")
TILE_SIZE = grassimg.get_width()
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','5','5','5','5','5','5','5','3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','4','4','4','4','4','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','4','4','4','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','4','1','0','0','0','0','0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0'],
            ['0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','']]



def game():
    global playerx1,is_aabb_collision, playery1, playerimg1, playerx1_change, pressed_right1, pressed_left1, v1, m1, Jump1, playerx2, playery2, playerimg2, playerx2_change, pressed_right2, pressed_left2, v2, m2, Jump2

    running = True
    while running:
    
        screen.blit(background, (-37 ,0))  # Blits the background image

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == "1":
                    screen.blit(goldimg, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == "2":
                    screen.blit(grassimg, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == "3":
                    screen.blit(goodimg, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == "4":
                    screen.blit(inimg, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == "5":
                    screen.blit(outimg, (x * TILE_SIZE, y * TILE_SIZE))
                if tile != "0":
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y +=1
            


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False          
                    

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    playerimg1 = pygame.image.load("playerL1.png")
                    # If key is released, x stops changing
                    pressed_left1 = True
                    pressed_right1 = False
                
                if event.key == pygame.K_d:
                    playerimg1 = pygame.image.load("playerR1.png")
                    # If key is released, x stops changing
                    pressed_left1 = False
                    pressed_right1 = True

                if event.key == pygame.K_w:
                    playerimg1 = pygame.image.load("jumpR1.png")
                    Jump1 = True


                    
            
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_a:
                    playerimg1 = pygame.image.load("playerL1.png")
                    # If key is released, x stops changing
                    pressed_left1 = False
                    pressed_right1 = False
                
                if event.key == pygame.K_d:
                    playerimg1 = pygame.image.load("playerR1.png")
                    # If key is released, x stops changing
                    pressed_left1 = False
                    pressed_right1 = False


            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    playerimg2 = pygame.image.load("playerL2.png")
                    # If key is released, x stops changing
                    pressed_left2 = True
                    pressed_right2 = False
                
                if event.key == pygame.K_RIGHT:
                    playerimg2 = pygame.image.load("playerR2.png")
                    # If key is released, x stops changing
                    pressed_left2 = False
                    pressed_right2 = True

                if event.key == pygame.K_UP:
                    playerimg2 = pygame.image.load("jumpR2.png")
                    Jump2 = True
                

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    playerimg2 = pygame.image.load("playerL2.png")
                    # If key is released, x stops changing
                    pressed_left2 = False
                    pressed_right2 = False
                
                if event.key == pygame.K_RIGHT:
                    playerimg2 = pygame.image.load("playerR2.png")
                    # If key is released, x stops changing
                    pressed_left2 = False
                    pressed_right2 = False
            
                    
        
        # Movement
        if pressed_left1 == True:
            playerimg1 = pygame.image.load("runningL1.png")     
            playerx1 -= playerx1_change

        if pressed_right1 == True:
            playerimg1 = pygame.image.load("runningR1.png")

            playerx1 += playerx1_change

        
        # Movement
        if pressed_left2 == True:
            playerimg2 = pygame.image.load("runningL2.png")     
            playerx2 -= playerx2_change

        if pressed_right2 == True:
            playerimg2 = pygame.image.load("runningR2.png")

            playerx2 += playerx2_change
        

        
        # Platform collisions



        # Borders player1
        if playerx1 <=0:
            playerx1 = 0
        if playerx1 >=705:
            playerx1 = 705

        

        # Borders player2
        if playerx2 <=0:
            playerx2 = 0
        if playerx2 >=705:
            playerx2 = 705



        # Physics player1
        if Jump1 == True:
            playerimg1 = pygame.image.load("JumpR1.png")

            F1 = (1/2)*m1*(v1**2)
            playery1 -= F1
            v1 -= 1
            if v1<0:
                m1 =- 1
                playerimg1 = pygame.image.load("playerR1.png")
            if v1 == -9:
                Jump1 = False
                v1 = 8
                m1 = 1



        pygame.time.delay(30)




        # Physics player2
        if Jump2 == True:
            playerimg2 = pygame.image.load("JumpR2.png")

            F2 = (1/2)*m2*(v2**2)
            playery2 -= F2
            v2 -= 1
                
            if v2<0:
                m2 =- 1
                playerimg2 = pygame.image.load("playerR2.png")
            if v2 == -9:
                Jump2 = False
                v2 = 8
                m2 = 1
    
        pygame.time.delay(30)


        player1(playerx1,playery1)
        player2(playerx2,playery2)
        pygame.display.update()

game()

    