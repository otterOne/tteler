#!/bin/python3

import pygame

def isCharInString(letter,text):
    for c in text:
        if c == letter:
            return True
    return False

def makeGrid(x, y):
    grid = []
    for i in range(y):
        grid.append([])
        for j in range(x):
            grid[i].append('x')

    return grid

def main():
    
    locX, locY = 0
    face = 0
    obstacles = "OT~|_"

    grid = makeGrid(50, 50)
    
    while True:
        
        
        #Input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    face = 0
                    if not isCharInString(grid[locY][locX-1],obstacles):
                        locX -= 1
                if event.key == pygame.K_RIGHT:
                    face = 2
                    if not isCharInString(grid[locY][locX+1],obstacles):
                        locX += 1
                if event.key == pygame.K_DOWN:
                    face = 3
                    if not isCharInString(grid[locY+1][locX],obstacles):
                        locX += 1
                if event.key == pygame.K_UP:
                    face = 1
                    if not isCharInString(grid[locY-1][locX],obstacles):
                        locX -= 1

        #Update

        #Rendering
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                print(grid[y][x], end='')

            print('/n')

                
            

        
