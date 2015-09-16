#!/bin/python3


import pygame


def charInString(letter,text):
    for c in text:
        if c == letter:
            return True
    return False


def main():
    

    obstacles = "OT~|_"


    while True:
        
        
        #Input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    face = 0
                    if not charInString(grid[locY][locX-1],obstacles):
                        locX -= 1
                if event.key == pygame.K_RIGHT:
                    face = 2
                    if not charInString(grid[locY][locX+1],obstacles):
                        locX += 1
                if event.key == pygame.K_DOWN:
                    face = 3
                    if not charInString(grid[locY+1][locX],obstacles):
                        locX += 1
                if event.key == pygame.K_UP:
                    face = 1
                    if not charInString(grid[locY-1][locX],obstacles):
                        locX -= 1
            







        #Update













        #Rendering
        print("surprise muddafakka!!")
        
