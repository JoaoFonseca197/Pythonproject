import pygame
import random




def main():

    azul =(0,0,255)
    verde =(0,255,0)
    vermelho =(255,0,0)
    lilas =(177,33,199)
    azul_claro=(0,239,255)
    laranja=(255,145,0)

    #fazer shuffle
    cartas = [azul,azul,verde,verde,vermelho,vermelho,lilas,lilas,azul_claro,azul_claro,laranja,laranja]
    random.shuffle(cartas)

     #criar criamos as cartas
    """criamos simplesmente a cor. com isto é só preciso fazer shufle de cores para as posiçoes defenidas"""
    class Cartas:
        def __init__(self,c,x,y,comprimento,largura):
            self.color = c
            self.position =pygame.Rect(x,y,comprimento,largura)
            self

    C_1 = Cartas(cartas[0],465,100,70,100)
    C_2 = Cartas(cartas[7],465,210,70,100)
    C_3 = Cartas(cartas[1],465,320,70,100)
    C_4 = Cartas(cartas[2],465,430,70,100)
    C_5 = Cartas(cartas[3],365,100,70,100)
    C_6 = Cartas(cartas[4],365,210,70,100)
    C_7 = Cartas(cartas[5],365,320,70,100)
    C_8 = Cartas(cartas[6],365,430,70,100)
    C_9 = Cartas(cartas[11],565,100,70,100)
    C_10=Cartas(cartas[8],565,210,70,100)
    C_11= Cartas(cartas[9],565,320,70,100)
    C_12= Cartas(cartas[10],565,430,70,100)
     
    



    
    
    
    res = (1000, 700)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            pos = pygame.mouse.get_pos()
            if(C_1.position.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                C_1.color = (255,0,0)
            if(event.type == pygame.QUIT):
                exit()

        

        
        screen.fill((0,0,20))
        #Quadrados com as cores trocadas
        pygame.draw.rect(screen,C_1.color, C_1.position, 0)
        pygame.draw.rect(screen,C_2.color, C_2.position, 0)
        pygame.draw.rect(screen,C_3.color, C_3.position, 0)
        pygame.draw.rect(screen,C_4.color, C_4.position, 0)
        pygame.draw.rect(screen,C_5.color, C_5.position, 0)
        pygame.draw.rect(screen,C_6.color, C_6.position, 0)
        pygame.draw.rect(screen,C_7.color, C_7.position, 0)
        pygame.draw.rect(screen,C_8.color, C_8.position, 0)
        pygame.draw.rect(screen,C_9.color, C_9.position, 0)
        pygame.draw.rect(screen,C_10.color, C_10.position, 0)
        pygame.draw.rect(screen,C_11.color, C_11.position, 0)
        pygame.draw.rect(screen,C_12.color, C_12.position, 0)
        #Quadrados amarelos
       
        Q2 = pygame.draw.rect(screen, (255,255,0), (465,210,70,100), 0)
        Q3 = pygame.draw.rect(screen, (255,255,0), (465,320,70,100), 0)
        Q4 = pygame.draw.rect(screen, (255,255,0), (465,430,70,100), 0)
        Q5 = pygame.draw.rect(screen, (255,255,0), (365,100,70,100), 0)
        Q6 = pygame.draw.rect(screen, (255,255,0), (365,210,70,100), 0)
        Q7 = pygame.draw.rect(screen, (255,255,0), (365,320,70,100), 0)
        Q8 = pygame.draw.rect(screen, (255,255,0), (365,430,70,100), 0)
        Q9 = pygame.draw.rect(screen, (255,255,0), (565,100,70,100), 0)
        Q10 = pygame.draw.rect(screen, (255,255,0), (565,210,70,100), 0)
        Q11 = pygame.draw.rect(screen, (255,255,0), (565,320,70,100), 0)
        Q12 = pygame.draw.rect(screen, (255,255,0), (565,430,70,100), 0)


        #Quadrados com as cores trocadas




        pygame.display.flip()

main()
        
        