import pygame
import time

millis = 0
pygame.init()

font = pygame.font.SysFont("monospace", 26)
font2 = pygame.font.SysFont("monospace",52)
screen = pygame.display.set_mode((500,200))

NEN = (28,47,77)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (194,134,134)
running = True
bien = '0:00'
h=0
kt = False
TEXT2 = font2.render(bien,True,WHITE)
while running == True:
	screen.fill(NEN)

	TEXT0 = font.render('STOPWATCH',True,RED)
	screen.blit(TEXT0,(272,14))

	pygame.draw.rect(screen,WHITE,(70,30,140,45))
	TEXT0 = font.render('START',True,BLACK)
	screen.blit(TEXT0,(100,38))

	pygame.draw.rect(screen,WHITE,(70,100,140,45))
	TEXT = font.render('STOP',True,BLACK)
	screen.blit(TEXT,(100,108))
		
	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			if (70<mouse_x<210) and (30<mouse_y<75): 
				millis = int(round(time.time() * 1000))
				kt = True	
			if (70<mouse_x<210) and (100<mouse_y<140): 
				kt = False
	if kt == True:
		tam = int(round(time.time() * 1000)) - millis
		h = tam%1000
		bien = str(tam//1000) + ':' +str(h//10)
		TEXT2 = font2.render(bien,True,WHITE)
	screen.blit(TEXT2,(290,70))
	# TEXT2 = font.render(str(tam//1000) + ':' +str(h//10),True,WHITE)
	# screen.blit(TEXT3,(180,160))
	
	pygame.display.flip()
pygame.quit()