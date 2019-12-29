import pygame
import random




def main():
    class Cartas:
        def __init__(self,r,g,b):
            self.color = (r,g,b)

    C_azul = Cartas(0,0,255)
    C_verde = Cartas(0,255,0)
    C_lilas = Cartas(177,33,199)
    C_vermelho = Cartas(255,0,0)

   
    cartas = [C_azul.color,C_azul.color,C_lilas.color,C_lilas.color,C_verde.color,C_verde.color,C_vermelho.color,C_vermelho.color]
    random.shuffle(cartas)

    
    
    
    res = (1000, 640)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                exit()
            

        r, g, b1, = 255 , 255, 0, 
        screen.fill((0,0,20))
        pygame.draw.rect(screen, (r,g,b1), (465,100,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (465,210,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (465,320,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (465,430,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (365,100,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (365,210,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (365,320,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (365,430,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (565,100,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (565,210,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (565,320,70,100), 0)
        pygame.draw.rect(screen, (r,g,b1), (565,430,70,100), 0)
        
        pygame.draw.rect(screen,cartas[0], (465,100,70,100), 4)
        pygame.draw.rect(screen,cartas[1], (465,210,70,100), 4)
        pygame.draw.rect(screen,cartas[2], (465,320,70,100), 4)
        pygame.draw.rect(screen,cartas[3], (465,430,70,100), 4)
        pygame.draw.rect(screen,cartas[4], (365,100,70,100), 4)
        pygame.draw.rect(screen,cartas[5], (365,210,70,100), 4)
        pygame.draw.rect(screen,cartas[6], (365,320,70,100), 4)
        pygame.draw.rect(screen,cartas[7], (365,430,70,100), 4)

        pygame.display.flip()

main()
        
        