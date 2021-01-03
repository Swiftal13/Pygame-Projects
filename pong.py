#Elyas's ping pong!
import pygame, sys, random


def ball_animation():
	global ball_speed_x, ball_speed_y, player1_score, player2_score
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	
	if ball.left <= 0:
		player2_score += 1
		ball_restart()
	
	if ball.right >= screen_width:
		ball_restart()
		player1_score += 1

	if ball.colliderect(player1) or ball.colliderect(player2):
		ball_speed_x *= -1


def player1_animation():
	player1.y += player1_speed

	if player1.top <= 0:
		player1.top = 0
	if player1.bottom >= screen_height:
		player1.bottom = screen_height


def player2_animation():
	player2.y += player2_speed

	if player2.top <= 0:
		player2.top = 0
	if player2.bottom >= screen_height:
		player2.bottom = screen_height



def ball_restart():
	global ball_speed_x, ball_speed_y
	ball.center = (screen_width / 2, screen_height / 2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

	pygame.display.flip()
	pygame.time.delay(850)
	
	
# General - setup:
pygame.init()
clock = pygame.time.Clock()

# Main - Window:
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ping Pong!")

# Colors:
light_grey = (200,200,200)
bg_color = pygame.Color("grey12")

# Game - Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 15, 140)
player2 = pygame.Rect(10, screen_height / 2 - 70, 15, 140)

# Game - Variables:
ball_speed_x = 6.5 * random.choice((1,-1))
ball_speed_y = 6.5 * random.choice((1,-1))
player1_speed = 0
player2_speed = 0


# text - variables:
player1_score = 0
player2_score = 0
font = pygame.font.Font(None,70)
font2 = pygame.font.Font(None, 60)



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
		# player1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player1_speed -= 7
			if event.key == pygame.K_DOWN:
				player1_speed += 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player1_speed += 7
			if event.key == pygame.K_DOWN:
				player1_speed -= 7
			
		# player2
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player2_speed -= 7
			if event.key == pygame.K_s:
				player2_speed += 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player2_speed += 7
			if event.key == pygame.K_s:
				player2_speed -= 7

		


   
    # Game - Logic
	ball_animation()
	player1_animation()
	player2_animation() 

	
	# Visuals
	screen.fill(bg_color)
	pygame.draw.rect(screen, light_grey, player1)
	pygame.draw.rect(screen, light_grey, player2)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
	
	player1_text = font.render(f"{player1_score}", False, light_grey)
	screen.blit(player1_text,(3,0))
	
	player2_text = font.render(f"{player2_score}", False, light_grey)
	screen.blit(player2_text,(1253,0))

	if player1_score == 5:
		elyas = "Player1 has won"
		player1_win = font2.render(f"{elyas}", False, light_grey)
		screen.blit(player1_win, (450,30))
		pygame.display.flip()
		pygame.time.delay(1400)
		pygame.quit()
		sys.exit()		

	if player2_score == 5:
		daniel = "Player 2 has won"
		player2_win = font2.render(f"{daniel}", False, light_grey)
		screen.blit(player2_win, (450, 30))
		pygame.display.flip()
		pygame.time.delay(1400)
		pygame.quit()
		sys.exit()		
	

	pygame.display.flip()
	clock.tick(60)


