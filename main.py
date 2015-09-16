#!/bin/python3


import pygame

def makeGrid(x, y):
    grid = []
    for i in range(y):
        grid.append([])
        for j in range(x):
            grid[i].append(' ')

    return grid

def main():
    
    locX, locY = 0
    face = 0

    
    
    while True:
        
        
        #Input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #Move player left
                if event.key == pygame.K_RIGHT:
                    #Move player right

        #Update

        #Rendering
        for 
        
