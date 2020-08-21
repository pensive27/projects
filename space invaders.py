import pygame
import random
import math

pygame.init()  # initialize pygame ALWAYS NEED THIS

screen = pygame.display.set_mode((800, 600))  # tuple for screen resolution

# TITLE AND ICON
pygame.display.set_caption("Alien invaders")
icon = pygame.image.load('enemy.png')  # find icon in project file
pygame.display.set_icon(icon)  # set icon in game

#background

background = pygame.image.load('space.png')

# player position on screen
playerImg = pygame.image.load('playership.png')
playerX = 520  # sets where player image appears. This sets it near the middle. 1060 is near the right
playerY = 480  # near bottom 600 is at the bottom of the screen
playerX_change = 0

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 520
bulletY = 480 # same as spaceship
bulletX_change = 0
bulletY_change = 10 # speed of bullet
bullet_state = "ready" # when bullet is no longer on screen

# enemy position on screen. It will be random
# this list will create multiple enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change =  []
enemyY_change= []
numofenemies = 10 # function makes enemies run six times in for loop


for i in range (numofenemies): # allows a range of six enemies to spawn following below parameters
	enemyImg.append(pygame.image.load('enemy.png'))
	enemyX.append(random.randint(0,700)) # allows random enemy placement. Needs import random. dont make it be 800 or enemy will move down to later if function
	enemyY.append(random.randint(50,100))
	enemyX_change.append(1) # how fast enemy moves on x
	enemyY_change.append(40) # how fast enemy moves on y

#score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)#style of text , size
textX= 10
textY=10 # where score appears

#game over text
gameoverfont = pygame.font.Font('freesansbold.ttf',64)#style of text , size

def show_score(x,y):
	score = font.render("score: " + str(score_value),True, (255,255,255))# white colour # render toshow the text score in the chosen fount and str to change the int into a string.
	screen.blit(score, (x, y)) #to show on screen

def gameovertext(): #function where score appears
	gameover = gameoverfont.render ("GAME OVER",True, (255,255,255))
	screen.blit(gameover, (200,250)) #to show on screen middle of screen


def fire_bullet(x,y): # function to fire bullet
	global bullet_state # so it can be accessed outside function
	bullet_state = "fire"
	screen.blit(bulletImg, (x +16 ,y+10)) # bullet to appear  on centre of spaceship


def enemy(x, y, i):  # function to draw playership. The x and y will allow player movement
	screen.blit(enemyImg[i],(x, y))  # this draws an image, we are drawing player image. blit measn to draw. Needs parameters of player position


def player(x, y):  # function to draw playership. The x and y will allow player movement
	screen.blit(playerImg, (x, y))  # this draws an image, we are drawing player image. blit measn to draw. Needs parameters of player position

# function to know if bullet has hit enemy using MATH
def isCollision(enemyX,enemyY, bulletX,bulletY):
	distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2))) # works out distance between two coorindates; the enemy and bullet
	if distance <27:
		return True # collision occured
	else:
 		return  False # collision did not occur

# Need a loop to keep game running
running = True  # create a game loop
while running:
	screen.fill((0, 0, 0))  # this tuple in the while loop puts things onto the screen. The 0,0,0 stand for Red, Green and Blue.0-255 use colour to RGB on google to find out more
	#background image#
	screen.blit(background, (0,0) )
	for event in pygame.event.get():  # event is something happening/ The for loop event and .get allows events to be collected.
		if event.type == pygame.QUIT:  # Any type of event can be quit  if running stops
			running = False
		# if keystroke is pressed check whether right or left in the for loop
		if event.type == pygame.KEYDOWN:  # KEYDOWN means a key is pressed
			if event.key == pygame.K_LEFT:
				playerX_change = -5  # will move left
			if event.key == pygame.K_RIGHT:
				playerX_change = 5  # will move right
			if event.key == pygame.K_SPACE: # pressing space fires bullet
				if bullet_state is "ready": # checks if bullet is on screen and prevents bullet firing until bullet crosses 0 coorgindate (won't be on screen)
					# if bullet is not on screen then below code activates
					bulletX = playerX # makes sure bullet doesnt move if player moves. Get the current x coordinate of the playership and
					#stores it in bulletx
					fire_bullet(bulletX,bulletY) # bullet fires from current bulletx (player location) and y (at a certain speed)

		if event.type == pygame.KEYUP:  # KEYUP means key released
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0  # stops movement when keys not pressed

	playerX += playerX_change  # registers player change. Added because the numbers, even negative, will be positive integer. Prevents it going out of bounds
	if playerX <= 0:  # creates boundary. If the sprite moves too far left won't leave screen
		playerX = 0
	elif playerX >= 760:
		playerX =760


	for i in range(numofenemies):
		#game over
		if enemyY[i] >400 and enemyX[i] == playerX: # if an enemy goes > 200 then below loop executes
			for j in range(numofenemies): #move all enemies off screen
				enemyY[j] = 2000 # enemies drop 2000 pixies off screen if game over
			gameovertext()
			break


		enemyX[i] += enemyX_change[i]  # registers player change. Added because the numbers, even negative, will be positive integer. Prevents it going out of bounds
		if enemyX[i] <= 0:  # creates boundary. If the sprite moves too far left won't leave screen
			enemyX_change[i] = 1
			enemyY[i] += enemyY_change[i] # will allow the enemy to move down by whatever y change set to after hitting a boundary on x
		elif enemyX[i] >= 760:
			enemyX_change[i] = -1
			enemyY[i] += enemyY_change[i]
		# collision
		collision = isCollision(enemyX[i], enemyY[i], bulletX,bulletY)  # I think this calls the collision function created earlier.
		# now we will define what we want to happen
		if collision:
			bulletY = 480  # if collision occurs reset bullet
			bullet_state = "ready"  # because bullet not showing anymore as its back at player reset state to ready
			score_value += 1 # knows that score increased by one if collsion is true
			enemyX[i] = random.randint(0, 735)  # respawn if collision is due, following from an increase in score
			enemyY[i] = random.randint(50, 100)

		enemy(enemyX[i], enemyY[i],i) # which enemy image on x y coordinates we want blited on screen



	if bullet_state is "fire": # by default state is ready but called when spacebar pressed
		fire_bullet(bulletX, bulletY) # bullet fired from player location
		bulletY -= bulletY_change #bullet moves in upward direction by reducing y value.

		# bullet movement
	if bulletY <=0: # reset bullet state if the bullet appears offscreen due to bulletY -= bulletY_change
		bulletY = 480 # puts it back at player
		bullet_state = "ready" # resets to ready

	play_again = 1



	# all this stuff is shown on screen in while loop (blitted stuff)
	show_score(textX,textY)
	player(playerX,playerY)  # to make sure player appears on the screen in the while loop. MAKE SURE IT APPEARS AFTER SCREEN.FILL OTHER WON'T APPEAR ON SCREEN
	pygame.display.update()  # updates what you to do to the display. ALWAYS NEED THIS and at the end.

