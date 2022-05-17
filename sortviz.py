import pygame
from helper.constant import RES,BLACK,WHITE
from helper.methods import generateArray

class MainGame:
    gameexit: bool
    values: list
    flag: int
    k: int
    j: int
    window: pygame.Surface
    framerate: int

    def __init__(self) -> None:
        self.initialize_pygame()
        self.flag = 0
        self.k = 0
        self.j = 0
        self.framerate = 30
        self.values= generateArray(780,20,450)
        self.gameexit = False
        self.window.fill(BLACK)
    
    def initialize_pygame(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RES)

    def sort_values(self) -> None:
        if self.k<len(self.values):
            for self.j in range(len(self.values)-self.k-1):
                if self.values[self.j]>self.values[self.j+1]:
                    self.values[self.j],self.values[self.j+1] = self.values[self.j+1],self.values[self.j]
    
    def exit_on_press(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameexit = True

    def draw_lines(self) -> None:
        X=20
        for i in self.values:
            if(X<780):
                pygame.draw.line(self.window,WHITE,[X,20],[X,i])
                X+=1
            self.flag+=1
    
    def reset_sorting_cursor(self) -> None:
        if self.j<len(self.values)-self.k-1:
            self.k+=1
   
    def mainLoop(self) -> None:
        while not self.gameexit:
            self.window.fill(BLACK)
            self.draw_lines()
            self.clock.tick(self.framerate)
            pygame.display.update()
            self.sort_values()      
            self.reset_sorting_cursor()
            self.exit_on_press()
            pygame.display.flip()

        pygame.display.flip()
    
    def run(self) -> None:
        self.mainLoop()

def main() -> None:
    mainGame = MainGame()
    mainGame.run()

main()