import pygame
from sudoko import main
import urllib.request
import json
from button import button
BLUE=[106,159,181]

c=(106,159,181)


pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("sudoko")

window.fill((255,255,255))
pygame.display.update()
pygame.display.flip()


def index():
	window.fill((255,255,255))
	hold_on=button(BLUE,150,300,300,50,"wait a moment")
	hold_on.draw(window)

	simulate=button(BLUE,120,500,150,50,"simulate")
	restart=button(BLUE,360,500,150,50,"restart")

	pygame.display.update()
	window.fill((255,255,255))
	flag=0
	try:
		url_request=urllib.request.urlopen("https://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=3")
		squares=json.load(url_request)["squares"]

		choose_level=button(BLUE,50,300,500,50,"press any num between 1 & 3 to simulate level",fontsize=15)
		choose_level.draw(window)
		pygame.display.update()

		run=True

		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					flag=1
					run=False
					pygame.quit()
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
					    level=1
					    run=False
					    break
					if event.key == pygame.K_2:
					    level=2
					    run=False
					    break
					if event.key == pygame.K_3:
					    level=3
					    run=False
					    break
		if not flag:
			window.fill((255,255,255))

			loading=button(BLUE,150,300,300,50,"loading...")
			loading.draw(window)
			pygame.display.update()

			url_request=urllib.request.urlopen("https://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level="+str(level))
			squares=json.load(url_request)["squares"]

			window.fill((255,255,255))
		else:
			raise Exception("yahoo")
	except:
		if not flag:	
			error=button(BLUE,150,300,300,50,"you are offline")
			error.draw(window)
			pygame.display.update()
			run=True
			while run:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit()
						run=False
					if not run:
						break
					if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and restart.isOver(pygame.mouse.get_pos()):
						index()
	else:
		for x in range(120,490,40):
			if x%120 == 0:
				continue
			pygame.draw.line(window,c,(120,x),(480,x),2)
			pygame.draw.line(window,c,(x,120),(x,480),2)
			pygame.display.update()

		for x in range(120,490,120):
			pygame.draw.line(window,(0,255,0),(120,x),(480,x),2)
			pygame.draw.line(window,(0,255,0),(x,120),(x,480),2)
			pygame.display.update()

		simulate.draw(window)
		restart.draw(window)

		pygame.display.update()
		flagy=main(squares,window,simulate,restart)
		if not flagy:	
			run=True
			while run:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						run=False
						break
					if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and restart.isOver(pygame.mouse.get_pos()):
						index()
			pygame.quit()

if(__name__== "__main__" ):
	index()


