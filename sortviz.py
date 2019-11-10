import pygame
import random
white=(255,255,255)
black =(0,0,0)
pygame.init()
values = []
clock = pygame.time.Clock()

window = pygame.display.set_mode((800,500))
window.fill(black)
gameexit = False
X = 20
for i in range(780):
    Y = random.randint(20,450)
    values.append(Y)

print(len(values))
temp = 0

# for i in values:
#     if(X<780):
#         pygame.draw.line(window,white,[X,20],[X,i])
#         X+=1
flag =0
k=0
j=0
while not gameexit:
    X=20
    window.fill(black)
    for i in values:
        if(X<780):
            pygame.draw.line(window,white,[X,20],[X,i])
            X+=1
            # pygame.display.update()
        flag+=1
    
    clock.tick(30)
    
    pygame.display.update()
    # for k in range(len(values)):
    #     for j in range(len(values)-k-1):
    #         if values[j]>values[j+1]:
    #             values[j],values[j+1] = values[j+1],values[j]

    if k<len(values):
        for j in range(len(values)-k-1):
            if values[j]>values[j+1]:
                values[j],values[j+1] = values[j+1],values[j]
        
    # j=j+1
    # temp = k
    if j<len(values)-k-1:
        k+=1
        #j=0
    # if temp+1 == k:
    #     j=0


   # window.fill(black)
    # for i in values:
    #     if(X<780):
    #         print(i)
    #         pygame.draw.line(window,white,[X,20],[X,i])
    #         X+=1
    #         pygame.display.update()
    #print(values)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
   # Y = random.randint(100,450)
    pygame.display.update()

pygame.display.update()      