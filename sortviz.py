import pygame
import random

# Defining some constants
WHITE=(255,255,255)
BLACK =(0,0,0)
RES=(800,500)

 

#  Helper Methods
def generateArray(n,min,max):
    arr=[]
    for i in range(n):
        Y = random.randint(min,max)
        arr.append(Y)
    return arr


gameexit = False
values=generateArray(780,20,450)
flag=k=j=0


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(RES)
window.fill(BLACK)


# Main loop

while not gameexit:
    X=20
    window.fill(BLACK)
    for i in values:
        if(X<780):
            pygame.draw.line(window,WHITE,[X,20],[X,i])
            X+=1
        flag+=1
    
    clock.tick(30)
    
    pygame.display.update()

    if k<len(values):
        for j in range(len(values)-k-1):
            if values[j]>values[j+1]:
                values[j],values[j+1] = values[j+1],values[j]
        
    if j<len(values)-k-1:
        k+=1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
    pygame.display.update()

pygame.display.update()      