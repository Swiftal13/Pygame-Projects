import pygame  # Import pygame module
import random  # Import random module
import math  # Import math module
import time # Import time module

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1900,1060), pygame.FULLSCREEN)  # Set window and window size
pygame.display.set_caption("Galactic")  # Window Title
background = pygame.image.load("background.jpg")  # Loads background png
font2 = pygame.font.Font("Pixer-Regular.ttf", 140) # Font of text


def main_menu():

    pygame.mixer.Channel(5).play(pygame.mixer.Sound('menu.mp3'), -1) # Background music
    click = None
    global lives
    font1 = pygame.font.Font("Pixer-Regular.ttf", 200)
    font2 = pygame.font.Font("Pixer-Regular.ttf", 50)
    font3 = pygame.font.Font("Pixer-Regular.ttf", 43)
    font4 = pygame.font.Font("Pixer-Regular.ttf", 30)
    menu = True
    background = pygame.image.load("background.jpg") # Loads background png
    x1 = 600
    y1 = 60
    x2 = 1300/2 + 77
    y2 = 800
    x3 = 577
    y3 = 400
    x4 = 1157
    y4 = 400
    x5 = 774
    y5 = 405
    white = 255,255,255
    black = 0,0,0
    
    while menu:
        screen.blit(background,  (0, 0))  # Blits the background image

        
        rendermenu = font1.render("Galactic", True, (255, 255, 255)) # Renders text onto window
        screen.blit(rendermenu, (x1, y1))



        renderrules = font4.render("Created by Elyas Sepahi", True, (255, 255, 255)) # Renders text onto window
        screen.blit(renderrules, (x2, y2))


        mx, my = pygame.mouse.get_pos() # Gets position of mouse cursor

        button_play = pygame.Rect(540, 380, 200, 70) # Play button
        button_quit = pygame.Rect(1160, 380, 200, 70) # Options button 
        button_instructions = pygame.Rect(960 - 166, 380, 270, 70) # Instructions button 

        pygame.draw.rect(screen, (black), button_play)
        pygame.draw.rect(screen, (black), button_quit)
        pygame.draw.rect(screen, (black), button_instructions)

        renderplay = font2.render("Play", True, (white)) # Renders text onto window
        screen.blit(renderplay, (x3, y3))

        
        renderquit = font2.render("Quit", True, (white)) # Renders text onto window
        screen.blit(renderquit, (x4, y4))

        renderinstruct = font3.render("Intructions", True, (white)) # Renders text onto window
        screen.blit(renderinstruct, (x5, y5))
        

        if button_play.collidepoint((mx, my)):
            renderplay = font2.render("Play", True, (107, 3, 252))
            screen.blit(renderplay, (x3, y3))

            if click:
                lives = 3
                game()
                

        if button_quit.collidepoint((mx, my)):
            renderquit = font2.render("Quit", True, (107, 3, 252))
            screen.blit(renderquit, (x4, y4))
            
            if click:
                exit()


        if button_instructions.collidepoint((mx, my)):
            renderinstruct = font3.render("Intructions", True, (107, 3, 252)) # Renders text onto window
            screen.blit(renderinstruct, (x5, y5))
            
            if click:
                instructions()








        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        
        pygame.display.update()
        
            




icon = pygame.image.load("ufo.png")  # Loads custom icon png
pygame.display.set_icon(icon)  # Sets icon as png


# Spaceship
playerimg = pygame.image.load("spaceship.png")  # Loads spaceship png
playerimg2 = pygame.image.load("spaceshipL.png")
playerimg3 = pygame.image.load("spaceshipR.png")
playerX = 400  # Spaceship position x
playerY = 785  # Spaceship position y
playerX_change = 0


def spaceship(x, y):
    screen.blit(playerimg, (x, y))  # Draws image onto screen

def spaceship2(playerX, playerY):
    screen.blit(playerimg2, (playerX, playerY))



# Rock1
rockimg = (pygame.image.load("rock.png")) # Loads rock png
rockX = (random.randint(50, 1200)) # Rock position x
rockX_change = 0
rockY = 0  # Rock position y
rockY_change = 1

def rock(x, y):
    screen.blit(rockimg, (x, y))  # Draws image onto screen




# Satellite
satimg = (pygame.image.load("Satellite.png")) # Loads satellite png
satX = -50
satX_change = 0.6
satY = random.randint(20, 400)  # Satellite position y
satY_change = 0

def sat(x, y):
    screen.blit(satimg, (x, y))  # Draws image onto screen




# ufo
ufoimg = (pygame.image.load("ufo.png")) # Loads ufo png
ufoX = (random.randint(50, 1750))
ufoX_change = 0
ufoY = 0  # Satellite position y
ufoY_change = 1

def ufo(x, y):
    screen.blit(ufoimg, (x, y))  # Draws image onto screen

    


# Bullet
bulletimg = pygame.image.load("bullet.png")  # Loads rock png
bulletX = 0
bulletY = 800  # Bullet position y
bulletX_change = 0
bulletY_change = 2.3 # how fast the bullet move
bullet_state = "ready"




# Score
score = 0
font = pygame.font.Font("Pixer-Regular.ttf", 35) # Font of text
scoreX = 13
scoreY = 10
def show_score(x, y):
    render = font.render(f"Score: {str(score)}", True, (255, 255, 255)) # Renders text onto window
    screen.blit(render, (x, y))



# Lives
livesX = 1760
livesY = 10
lives = 3
def show_lives(x, y):
    render2 = font.render(f"Lives: {str(lives)}", True, (255, 255, 255)) # Renders text onto window
    screen.blit(render2, (x, y))




# Game over text
overX = 500
overY = 350
def over(x, y):
    render3 = font2.render("GAME OVER", True, (255, 255, 255)) # Renders text onto window
    screen.blit(render3, (x, y))
    




# Bullet fire mechanism
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 30, y - 60))




# Collisions with rock and bullet
def isCollision(rockX, rockY, bulletX, bulletY):
    distance = math.sqrt((math.pow(rockX - bulletX, 2)) + (math.pow(rockY - bulletY, 2)))  # Formula for distance
    if distance < 90:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('explosion.wav'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False




# Collisions with rock and spaceship
def isCollision2(rockX, rockY, playerX, playerY):
    distance2 = math.sqrt((math.pow(rockX - playerX, 2)) + (math.pow(rockY - playerY, 2)))  # Formula for distance
    if distance2 < 110:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('bam.mp3'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False




# Collisions with Satellite and bullet
def isCollision3(satX, satY, bulletX, bulletY):
    distance3 = math.sqrt((math.pow(satX - bulletX, 2)) + (math.pow(satY - bulletY, 2)))  # Formula for distance
    if distance3 < 50:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('explosion.wav'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False





# Collisions with Satellite and spaceship
def isCollision4(satX, satY, playerX, playerY):
    distance4 = math.sqrt((math.pow(satX - playerX, 2)) + (math.pow(satY - playerY, 2)))  # Formula for distance
    if distance4 < 70:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('bam.mp3'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False




# Collisions with UFO and bullet
def isCollision5(ufoX, ufoY, playerX, playerY):
    distance5 = math.sqrt((math.pow(ufoX - playerX, 2)) + (math.pow(ufoY - playerY, 2)))  # Formula for distance
    if distance5 < 80:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('explosion.wav'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False



# Collisions with UFO and spaceship
def isCollision6(ufoX, ufoY, playerX, playerY):
    distance6 = math.sqrt((math.pow(ufoX - playerX, 2)) + (math.pow(ufoY - playerY, 2)))  # Formula for distance
    if distance6 < 70:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('bam.mp3'))
        pygame.mixer.Channel(2).set_volume(0.3)
        return True
    else:
        return False






quitterText = font.render("Quit", True, (255, 255, 255))
quitter = pygame.Rect(1810, 60, 200, 70) # back button in instructions

# Game loop
def game():
    pygame.mixer.Channel(5).pause()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("game.mp3"), -1) # Background music
    global bullet_state, playerX, playerY, bulletX, bulletY, rockX, rockY, ufoX, ufoY, playerX_change, satY, satX, lives, score, playerimg, quitter, quitterText
    
    
    running = True
    while running:

        # RBG means: Red Green Blue
        screen.fill((153, 233, 255))  # Custom colour for window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # If key is pressed down
                
                if event.key == pygame.K_LEFT:
                    playerimg = playerimg2
                    # If the left key is hold down, minus x integer
                    playerX_change -= 2
                
                if event.key == pygame.K_RIGHT:
                    playerimg = playerimg3
                    # If the right key is hold down, plus x integer
                    playerX_change += 2

                if event.key == pygame.K_SPACE:  # If the spacebar is pressed, trigger function
                    if bullet_state == "ready":
                        pygame.mixer.music.load("laser.wav")
                        
                        # checks if bullet is already on the screen or not
                        pygame.mixer.music.play(0, 0.0)
                        bulletX = playerX  # bullets start at where the spaceship is
                        bullet_fire(bulletX, bulletY)  # bullet function triggers

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerimg = pygame.image.load("spaceship.png")  
                    # If key is released, x stops changing
                    playerX_change = 0

        screen.blit(background, (0, 0))  # Blits the background image

    

        # Player movement
        playerX += playerX_change
        if playerX <= -15:  # This is the logic so if the player image hits the left or right border it teleports it back to the border
            playerX = -15
        elif playerX >= 1730:
            playerX = 1730

    

        # Rock and Satellite movement
        rockY += rockY_change
        if rockY <= 0:  # This is the logic so if the rock image hits the left or right border it teleports it back to the border
            rockY = 0
        elif rockY >= 1100:
            rockY = -10
            rockX = random.randint(50, 1200)
    
        rockX += rockX_change
        if rockX <= 0:  # This is the logic so if the rock image hits the left or right border it teleports it back to the border
            rockX = 0
        elif rockX >= 1000: # Borders
            rockX = 1000




        satX += satX_change
        satX += rockX_change
        if satX <= 0:  # This is the logic so if the rock image hits the left or right border it teleports it back to the border
            satX = 0
        elif satX >= 1400: # Borders
            satX = -50
            satY = random.randint(20, 400)


    

        ufoY += ufoY_change
        if ufoY <= 0:  # This is the logic so if the rock image hits the left or right border it teleports it back to the border
            ufoY = 0
        elif ufoY >= 900:
            ufoY = -50
            ufoX = random.randint(50, 1200)
    
        ufoX += rockX_change
        if ufoX <= 0:  # This is the logic so if the rock image hits the left or right border it teleports it back to the border
            ufoX = 0
        elif ufoX >= 1000: # Borders
            ufoX = 1000
    
    
    
    
        # Bullet movement
        if bulletY <= -70:  # This is the logic so if the bullet image hits the top of the window, it dissapears
            bulletY = 810
            bullet_state = "ready"


        if bullet_state == "fire":
            bullet_fire(bulletX, bulletY)
            bulletY -= bulletY_change
    
    

    
        # Collision for bullet and rock
        collision = isCollision(rockX, rockY, bulletX, bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = 810
            score += 1
            rockX = random.randint(50,1200)
            rockY = 50



        # Collision for spaceship and rock
        collision3 = isCollision2(rockX, rockY, playerX, playerY)
        if collision3:
            lives -= 1
            rockX = random.randint(50,1200)
            rockY = 50
            if lives == 0:
                over(overX, overY)
                pygame.display.update()
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('GAMEOVER.wav'))
                time.sleep(3)
                open("scores.csv", "w")
                main_menu()
                pygame.display.update()
                

        # Collision for bullet and Satellite
        collision2 = isCollision3(satX, satY, bulletX, bulletY)
        if collision2:
            bullet_state = "ready"
            bulletY = 810
            score -= 1
            satX = -15
            satY = random.randint(20, 400)

        # Collision for spaceship and Satellite
        collision4 = isCollision4(satX, satY, playerX, playerY)
        if collision4:
            lives -= 1
            satX = random.randint(50,1200)
            satY = 50
            if lives == 0:
                over(overX, overY)
                pygame.display.update()
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('GAMEOVER.wav'))
                time.sleep(3)
                main_menu()
                pygame.display.update()
                
                

    

        # Collision for bullet and ufo
        collision5 = isCollision5(ufoX, ufoY, bulletX, bulletY)
        if collision5:
            bullet_state = "ready"
            bulletY = 810
            score += 2
            ufoX = random.randint(50,1200)
            ufoY = 50

        # Collision for spaceship and ufo
        collision6 = isCollision6(ufoX, ufoY, playerX, playerY)
        if collision6:
            lives -= 1
            ufoX = random.randint(50,1200)
            ufoY = 50
            if lives == 0:
                over(overX, overY)
                pygame.display.update()
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('GAMEOVER.wav'))
                time.sleep(3)
                main_menu()
                pygame.display.update()
               



        elif rockY >= 1200: # if rock is at the bottom of window, reset to top
            rockY = -500
            rockX = random.randint(50, 1200)
    

        elif satX >= 1300: # if Satellite is at the bottom of window, reset to top
            satX = -70

    
    
        elif ufoY >= 1200: # if ufo is at the bottom of window, reset to top
            ufoY = -60
            ufoX = random.randint(50, 1200)


        
        pygame.draw.rect(screen, (0, 0, 0), quitter) # draws quitter rect onto screen
        screen.blit(quitterText, (1824, 60)) # draws text onto screen
        mx, my = pygame.mouse.get_pos() # Gets position of mouse cursor
        
        if quitter.collidepoint((mx, my)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Channel(1).pause()
                    score = 0
                    lives = 3
                    main_menu()
                    
                    
        
                



        show_lives(livesX, livesY) # Calls the lives function
        show_score(scoreX,scoreY) # Calls the score function
        spaceship(playerX, playerY)  # Calls spaceship function
        rock(rockX, rockY)  # Calls rock function
        sat(satX, satY) # Calls Satellite function
        ufo(ufoX, ufoY) # Calls ufo function
        pygame.display.update()  # Updates window so any images and movement can show



def instructions():

    click = True
    ins = True
    font3 = pygame.font.Font("Pixer-Regular.ttf", 100)
    font4 = pygame.font.Font("Pixer-Regular.ttf", 30)
    font5 = pygame.font.Font("Pixer-Regular.ttf", 50)
    x = 550
    y = 45
   
    x2 = 320
    y2 = 200
    y3 = 230
    
    x4 = 500
    y4 = 340
    
    x5 = 500
    y5 = 532
    
    x6 = 500
    y6 = 720

    x7 = 1770
    y7 = 755


    while ins:

        screen.blit(background,  (0, 0))  # Blits the background image
        renderinstructions2 = font3.render("Instructions", True, (255, 255, 255)) # Renders text onto window
        screen.blit(renderinstructions2, (x, y))


        rendertext1 = font4.render("The aim of the game is to gain as many points as possible, by hitting the correct incoming objects", True, (255, 255, 255)) # Renders text onto window
        screen.blit(rendertext1, (x2, y2))


        rendertext2 = font4.render("without getting hit by them. If you get hit by them, you lose a life. You have 3 lives. Good luck!", True, (255, 255, 255)) # Renders text onto window
        screen.blit(rendertext2, (x2, y3))


        rockimg = (pygame.image.load("rock.png")) # Loads rock png
        rockX = 350
        rockY = 300
        screen.blit(rockimg, (rockX, rockY))  # Draws image onto screen
        rendertext3 = font4.render("Asteroids: Shoot it down for a point. Don't let them hit your beloved planet!", True, (255, 255, 255)) # Renders text onto window
        screen.blit(rendertext3, (x4, y4))



        satimg = (pygame.image.load("Satellite.png")) # Loads rock png
        satX = 371
        satY = 530
        screen.blit(satimg, (satX, satY))  # Draws image onto screen
        rendertext4 = font4.render("Satellites: They are essential for communication. Try not to destroy them!", True, (255, 255, 255))
        screen.blit(rendertext4, (x5, y5))



        ufoimg = (pygame.image.load("ufo.png"))
        ufoX = 371
        ufoY = 705
        screen.blit(ufoimg, (ufoX, ufoY))
        rendertext5 = font4.render("UFOs: We don't want enemies landing in our territory, fire away!", True, (255, 255, 255))
        screen.blit(rendertext5, (x6, y6))

        back = pygame.Rect(1760, 750, 200, 70) # back button in instructions
        pygame.draw.rect(screen, (0, 0, 0), back)

        renderback = font5.render("Back", True, (255, 255, 255)) # renders text onto window
        screen.blit(renderback, (x7, y7))
        
        mx, my = pygame.mouse.get_pos() # Gets position of mouse cursor
        
        if back.collidepoint((mx, my)):
            if click:
               main_menu()
        
    
        # Hover over effect
        if back.collidepoint((mx, my)):
            renderback = font5.render("Back", True, (107, 3, 252))
            screen.blit(renderback, (x7, y7))
        

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()


main_menu()