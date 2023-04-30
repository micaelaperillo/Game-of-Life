import pygame
import numpy as np
import time
import tkinter as tk

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)
nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# state: alive = 1, dead = 0
gameState = np.zeros((nxC, nyC))

# execution control 
pauseExec = True
running = True

generation = 0
title = f"Game of Life - Generation number: {generation}"

pygame.display.set_caption(title)

def help():
    popup = tk.Tk()
    popup.wm_title("Help")
    label = tk.Label(popup, text = '''
    Commands:
    - x: closes window
    - n: creates new game
    - space: pauses/reloads game
    - h: opens help''')
    label.pack(side="top", padx=20, pady=10)
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack()
    # to center the popup
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    # calculates the position
    x = (screen_width - popup.winfo_reqwidth()) / 2
    y = (screen_height - popup.winfo_reqheight()) / 2
    popup.geometry("+%d+%d" % (x, y))
    
    popup.mainloop()

def calculate_neighbours(state, x, y):
    return (state[(x-1)  % nxC, (y-1) % nyC]  + \
            state[(x-1)  % nxC, (y)   % nyC]  + \
            state[(x-1)  % nxC, (y+1) % nyC]  + \
            state[(x)    % nxC, (y-1) % nyC]  + \
            state[(x)    % nxC, (y+1) % nyC]  + \
            state[(x+1)  % nxC, (y-1) % nyC]  + \
            state[(x+1)  % nxC, (y)   % nyC]  + \
            state[(x+1)  % nxC, (y+1) % nyC])

while running:

    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.1)

    # handles events
    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            if event.key == pygame.K_SPACE:
                pauseExec = not pauseExec
            if event.key == pygame.K_n:
                newGameState = np.zeros((nxC, nyC))
                pauseExec = True
                generation = 0
            if event.key == pygame.K_h:
                help()

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not gameState[celX, celY]

    for y in range(0, nxC):
        for x in range(0, nyC):
            
            if not pauseExec:
                # amount of alive neighbours
                n_neigh = calculate_neighbours(gameState, x, y)
                
                # rule 1: dead cell with exactly 3 alive neighbours -> alive
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # rule 2: alive cell with <2 or >3 alive neighbours -> dead
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            pol = [((x)   * dimCW, (y)   * dimCH), 
                   ((x+1) * dimCW, (y)   * dimCH),
                   ((x+1) * dimCW, (y+1) * dimCH),
                   ((x)   * dimCW, (y+1) * dimCH)]
                
            # draws each cell
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), pol, width=1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), pol, width=0)

    if pauseExec:
        title = "Game of Life - PAUSED"
    else:
        generation += 1
        title = f"Game of Life - Generation number: {generation}"

    pygame.display.set_caption(title)
    gameState = np.copy(newGameState)

    pygame.display.flip()