import pygame
import random




def main():
    #criar criamos as cartas
    """criamos simplesmente a cor. com isto é só preciso fazer shufle de cores para as posiçoes defenidas"""
    class Cartas:
        def __init__(self,r,g,b):
            self.color = (r,g,b)

    C_azul = Cartas(0,0,255)
    C_verde = Cartas(0,255,0)
    C_lilas = Cartas(177,33,199)
    C_vermelho = Cartas(255,0,0)

    #fazer shuffle
    cartas = [C_azul.color,C_azul.color,C_lilas.color,C_lilas.color,C_verde.color,C_verde.color,C_vermelho.color,C_vermelho.color]
    random.shuffle(cartas)

    
    
    
    res = (1000, 640)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                exit()

        pos = pygame.mouse.get_pos()    

        r, g, b1, = 255 , 255, 0, 
        screen.fill((0,0,20))
        #Quadrados com as cores trocadas
        pygame.draw.rect(screen,cartas[0], (465,100,70,100), 0)
        pygame.draw.rect(screen,cartas[1], (465,210,70,100), 0)
        pygame.draw.rect(screen,cartas[2], (465,320,70,100), 0)
        pygame.draw.rect(screen,cartas[3], (465,430,70,100), 0)
        pygame.draw.rect(screen,cartas[4], (365,100,70,100), 0)
        pygame.draw.rect(screen,cartas[5], (365,210,70,100), 0)
        pygame.draw.rect(screen,cartas[6], (365,320,70,100), 0)
        pygame.draw.rect(screen,cartas[7], (365,430,70,100), 0)
        #Quadrados amarelos
        Q1 = pygame.draw.rect(screen, (r,g,b1), (465,100,70,100), 0)
        Q2 = pygame.draw.rect(screen, (r,g,b1), (465,210,70,100), 0)
        Q3 = pygame.draw.rect(screen, (r,g,b1), (465,320,70,100), 0)
        Q4 = pygame.draw.rect(screen, (r,g,b1), (465,430,70,100), 0)
        Q5 = pygame.draw.rect(screen, (r,g,b1), (365,100,70,100), 0)
        Q6 = pygame.draw.rect(screen, (r,g,b1), (365,210,70,100), 0)
        Q7 = pygame.draw.rect(screen, (r,g,b1), (365,320,70,100), 0)
        Q8 = pygame.draw.rect(screen, (r,g,b1), (365,430,70,100), 0)
        Q9 = pygame.draw.rect(screen, (r,g,b1), (565,100,70,100), 0)
        Q10 = pygame.draw.rect(screen, (r,g,b1), (565,210,70,100), 0)
        Q11 = pygame.draw.rect(screen, (r,g,b1), (565,320,70,100), 0)
        Q12 = pygame.draw.rect(screen, (r,g,b1), (565,430,70,100), 0)
        #Quadrados com as cores trocadas
         if(pos[0] >= 365 and pos[0] <= 365+70 or pos[0] >= 465 and pos[0] <= 465+70 or pos[0] >= 565 and pos[0] <= 565+70 ):
            if (pos[1] >= 270 and pos[1] <= 300):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,270,100,30), 4)
                if(mb[0]):
                    click += 1
                    print(click)
            elif (pos[1] >= 310 and pos[1] <= 340):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,310,100,30), 4)
            elif (pos[1] >= 350 and pos[1] <= 380):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,350,100,30), 4)
            elif (pos[1] >= 390 and pos[1] <= 420):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,390,100,30), 4)
            elif (pos[1] >= 430 and pos[1] <= 460):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,430,100,30), 4)
            elif (pos[1] >= 470 and pos[1] <= 500):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,470,100,30), 4) 


        pygame.display.flip()

main()
        
        