
import pygame
from button import button
import time
grid=[[[0 for i in range(3)] for j in range(3)]for k in range(9)]
realEmpty=[]
DELAY=0.05
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
def printSingle(window,lis):
	x=142
	y=140
	i=lis[0]
	j=lis[1]
	k=lis[2]
	largeText = pygame.font.Font('freesansbold.ttf',35)
	if grid[i][j][k] != 0:
		text=str(grid[i][j][k])
	else:
		text=" "
	TextSurf, TextRect = text_objects(text, largeText)
	pygame.draw.rect(window,(255,255,255),((y+120*j+k*40-12),(x+40*i-18),30,33))	
	TextRect.center = ((y+120*j+k*40),(x+40*i))
	window.blit(TextSurf, TextRect)
	pygame.display.update()
def checkincube(num,lis):
	x=(int(lis[0]/3))*3
	for i in range(x,x+3):
		for j in range(3):
			if grid[i][lis[1]][j] == num:
				return False
	return True
def isApproved(num,lis):
	x=lis[0]
	y=lis[1]
	z=lis[2]
	for i in range(3):
		for j in range(3):
			if grid[x][i][j] == num:
				return False
	for i in range(9):
		if grid[i][y][z] == num:
			return False
	return checkincube(num,lis)

def presentNumber(lis):
	return grid[lis[0]][lis[1]][lis[2]]
def getEmpty():
	realEmpty.clear()
	for i in range(9):
		for j in range(3):
			for k in range(3):
				if grid[i][j][k] == 0:
					realEmpty.append([i,j,k])
def storeVal(j,lis):
	grid[lis[0]][lis[1]][lis[2]]=j
	return
def solve(window):
	i=0
	while i  < len(realEmpty):
		k=presentNumber(realEmpty[i])
		for j in range(presentNumber(realEmpty[i])+1,10):
			if isApproved(j,realEmpty[i]):
				storeVal(j,realEmpty[i])
				try:
					printSingle(window,realEmpty[i])
					time.sleep(DELAY)
				except:
					return 1
				break
		if presentNumber(realEmpty[i]) == k:
			storeVal(0,realEmpty[i])
			try:
				printSingle(window,realEmpty[i])
				time.sleep(DELAY)
			except:
				return 1
			i=i-1
		else:
			i=i+1
		if i<0:
			return
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				return 1
	return 0
def loadSquares(squares):
	for i in range(9):
		for j in range(3):
			for k in range(3):
				grid[i][j][k]=0
	for box in squares:
		x=box["x"]
		y=int(box["y"]/3)
		z=box["y"]%3
		grid[x][y][z]=box["value"]

def main(squares,window,simulate,restart):
	flag=0
	loadSquares(squares)
	getEmpty()
	for i in range(9):
		for j in range(3):
			for k in range(3):
				printSingle(window,[i,j,k])
	check=True
	while check:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
				if simulate.isOver(pygame.mouse.get_pos()):
					check=False
					break
				if restart.isOver(pygame.mouse.get_pos()):
					return flag
			if event.type==pygame.QUIT:
				pygame.quit()
				return 1
	return solve(window)
