import pygame as pyg
import pyautogui as ptg
import keyboard
import mouse
import time
import random

pyg.init
Type = "Sand"
window = pyg.display.set_mode((1920, 1080))
window.fill([0,0,0])
scatter = 5
Particle_Size = 5
RowCount = int(1080 / Particle_Size)
ColomnCount = int(1920 / Particle_Size)
Grids = []
for i in range(0,int(RowCount-1)):
    Xaxis = [None] * int(ColomnCount-1)
    Grids.append(Xaxis)

def MouseSpawn():
    if Type == "Sand":
        xrandom = random.randint(-(scatter * Particle_Size),(scatter * Particle_Size))
        yrandom = random.randint(-(scatter * Particle_Size),(scatter * Particle_Size))
        mouse_pos = ptg.position() 
        pyg.draw.circle(window,[255,255,255],(mouse_pos.x,mouse_pos.y),(scatter * Particle_Size + (2*scatter)),1)
        if mouse.is_pressed(button='left'):
            col = (int(round((mouse_pos.x + xrandom)/Particle_Size))) - 1
            row = (int(round((mouse_pos.y + yrandom)/Particle_Size))) -1
            col = max(5, min(col, ColomnCount-5))
            row = max(0, min(row, RowCount-2))
            if Grids[row][col] == None :
                Grids[row][col] = Sand()
                
    elif Type == "Rock":
        mouse_pos = ptg.position() 
        pyg.draw.circle(window,[255,255,255],(mouse_pos.x,mouse_pos.y),(scatter * Particle_Size + (2*scatter)),1)
        if mouse.is_pressed(button='left'):
            
            for ş in range(-(scatter+2) * Particle_Size, (scatter+3)*Particle_Size):
                row = (int(round((mouse_pos.y + ş)/Particle_Size))) -1
                
                for ç in range(-(scatter+2)*Particle_Size, (scatter+3)*Particle_Size):
                    col = (int(round((mouse_pos.x + ç)/Particle_Size))) - 1
                    col = max(5, min(col, ColomnCount-5))
                    row = max(0, min(row, RowCount-2))
                    
                    if (ş-2)**2 + (ç-2)**2 < ((scatter * Particle_Size + (2*scatter))**2) - 100:
                        Grids[row][col] = Rock()
                    
    elif Type == "Delete":
            mouse_pos = ptg.position() 
            pyg.draw.circle(window,[255,255,255],(mouse_pos.x,mouse_pos.y),(scatter * Particle_Size + (2*scatter)),1)
            if mouse.is_pressed(button='left'):
                
                for ş in range(-(scatter+2) * Particle_Size, (scatter+3)*Particle_Size):
                    row = (int(round((mouse_pos.y + ş)/Particle_Size))) -1
                    
                    for ç in range(-(scatter+2)*Particle_Size, (scatter+3)*Particle_Size):
                        col = (int(round((mouse_pos.x + ç)/Particle_Size))) - 1
                        col = max(5, min(col, ColomnCount-5))
                        row = max(0, min(row, RowCount-2))
                        
                        if (ş-2)**2 + (ç-2)**2 < ((scatter * Particle_Size + (2*scatter))**2) - 100:
                            Grids[row][col] = None
        

def CellCheck():
    
    for Rowy, Rows in enumerate(reversed(Grids)):
        
        for Colx, Colomn in enumerate(Rows):
            if Grids[Rowy][Colx] == None:
                pass
            else:
                pyg.draw.rect(window,Grids[Rowy][Colx].Colour, pyg.Rect((Colx * Particle_Size), (Rowy * Particle_Size),Particle_Size,Particle_Size))
                if Grids[Rowy][Colx].Updated == True:
                    Grids[Rowy][Colx].Updated = False
                else:
                    Grids[Rowy][Colx].Update(Colx,Rowy)

class Sand :
    Updated = False
    Colour = [255,128,0]
    def Update(self,Cx,Ry):
        
        nextPosy = Ry + 1
        nextPosx = Cx
        if nextPosy > (int(1080/ Particle_Size)-2):
            nextPosy = (int(1080/Particle_Size)-2)
            nextPosx = Cx
        elif Grids[nextPosy][nextPosx] == None:
            nextPosy = Ry + 1
            nextPosx = Cx
        elif Grids[nextPosy][nextPosx + 1] == None and nextPosx < (int(1920 / Particle_Size)-3):
            nextPosx = Cx+1
            nextPosy = Ry+1
        elif Grids[nextPosy][nextPosx - 1] == None and nextPosx > 2:
            nextPosx = Cx-1
            nextPosy = Ry+1
        else: 
            nextPosx = Cx
            nextPosy = Ry
        Grids[Ry][Cx] = None
        Grids[nextPosy][nextPosx] = Sand()
        Grids[nextPosy][nextPosx].Updated = True
    
    

class Water :
    def Update():
        pass

class Wapour :
    def Update():
        pass

class Rock :
    Updated = False
    Colour = [49,56,47]
    def Update(self,Cx,Ry):
        pass
    

while True:
    window.fill([0,0,0])
    pyg.event.get()
    start_time = time.time()
    MouseSpawn()
    CellCheck()
    pyg.display.flip()
    
    if keyboard.is_pressed("q"):
        Type = "Sand"
    if keyboard.is_pressed("w"):
        Type = "Rock"
    if keyboard.is_pressed("e"):
        Type = "Water"
    if keyboard.is_pressed("r"):
        Type = "Wapour"
    if keyboard.is_pressed("d"):
        Type = "Delete"

    


    time.sleep(0.0000000000000000000001)
    if keyboard.is_pressed("escape"):
        break
    end_time = time.time()
    deltatime = end_time - start_time
    FPS = 1.0 / (deltatime)
    print(FPS)
pyg.display.quit