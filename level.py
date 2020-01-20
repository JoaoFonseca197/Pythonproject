import pygame
import random
class Carta:
        def __init__(self,r,g,b,x,y,comprimento,largura):
            self = r,g,b
            self =pygame.Rect(x,y,comprimento,largura)
            self.match = False
            self.picked = False



def main():

    azul =(0,0,255)
    verde =(0,255,0)
    vermelho =(255,0,0)
    lilas =(177,33,199)
    azul_claro=(0,239,255)
    laranja=(255,145,0)
    i= 0
    comp=[]
    #fazer shuffle
    cores = [azul,azul,verde,verde,vermelho,vermelho,lilas,lilas,azul_claro,azul_claro,laranja,laranja]
    random.shuffle(cores)

     #criar criamos as cartas
    """criamos simplesmente a cor. com isto é só preciso fazer shufle de cores para as posiçoes defenidas"""
    
    Cartas = [0,1,2,3,4,5,6,7,8,9,10,11]
    Cartas[0] = (255,255,0)
    Cartas[1] = (255,255,0)
    Cartas[2] = (255,255,0)
    Cartas[3] = (255,255,0)
    Cartas[4] = (255,255,0)
    Cartas[5] = (255,255,0)
    Cartas[6] = (255,255,0)
    Cartas[7] = (255,255,0)
    Cartas[8] = (255,255,0)
    Cartas[9]=(255,255,0)
    Cartas[10]= (255,255,0)
    Cartas[11]= (255,255,0)
    Posicoes = [0,1,2,3,4,5,6,7,8,9,10,11]
    Posicoes[0] =pygame.Rect(365,100,70,100)
    Posicoes[1] =pygame.Rect(365,210,70,100)
    Posicoes[2] =pygame.Rect(365,320,70,100)
    Posicoes[3] =pygame.Rect(365,430,70,100)
    Posicoes[4] =pygame.Rect(465,100,70,100)
    Posicoes[5] =pygame.Rect(465,210,70,100)
    Posicoes[6] =pygame.Rect(465,320,70,100)
    Posicoes[7] =pygame.Rect(465,430,70,100)
    Posicoes[8] =pygame.Rect(565,100,70,100)
    Posicoes[9] =pygame.Rect(565,210,70,100)
    Posicoes[10] =pygame.Rect(565,320,70,100)
    Posicoes[11] =pygame.Rect(565,430,70,100)
    
    
   
   
    """ for (i in Cartas)
        if(Cartas)"""

    
    
    
    res = (1000, 700)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            
            if(event.type == pygame.QUIT):
                exit()

            pos = pygame.mouse.get_pos()
            if(len(comp) < 2):
                if(Posicoes[0].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[0] = cores[0]
                    comp.append(Cartas[0])
                    
                elif (Posicoes[1].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[1] = cores[1]
                    comp.append(Cartas[1])
                   
                    
                elif(Posicoes[2].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[2] = cores[2]
                    comp.append(Cartas[2])
                  
                    
                elif(Posicoes[3].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[3] = cores[3]
                    comp.append(Cartas[3])
                   
                
                    
                elif(Posicoes[4].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[4] = cores[4]
                    comp.append(Cartas[4])
                   
                     
                      
                elif(Posicoes[5].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[5] = cores[5]
                    comp.append(Cartas[5])
                   
                   
                    
                elif(Posicoes[6].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[6] = cores[6]
                    comp.append(Cartas[6])
                   
                    
                    
                
                elif(Posicoes[7].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[7] = cores[7]
                    comp.append(Cartas[7])
                    
                   
                    
                
                elif(Posicoes[8].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[8] = cores[8]
                    comp.append(Cartas[8])
                 
                    
                    
                
                elif(Posicoes[9].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[9] = cores[9]
                    comp.append(Cartas[9])
                   
                    
                
                elif(Posicoes[10].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[10] = cores[10]
                    comp.append(Cartas[10])
                    
                    
                    
                
                elif(Posicoes[11].collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN):
                    Cartas[11] = cores[11]
                    comp.append(Cartas[11])
                    
                   
            else:        
                if(comp[0] == comp[1]):
                    print("igual")
                else:
                    Cartas[0] = (255,255,0)
                    Cartas[1] = (255,255,0)
                    Cartas[2] = (255,255,0)
                    Cartas[3] = (255,255,0)
                    Cartas[4] = (255,255,0)
                    Cartas[5] = (255,255,0)
                    Cartas[6] = (255,255,0)
                    Cartas[7] = (255,255,0)
                    Cartas[8] = (255,255,0)
                    Cartas[9]=(255,255,0)
                    Cartas[10]= (255,255,0)
                    Cartas[11]= (255,255,0)
                    comp.pop(0)
                    comp.pop(0)
 
        screen.fill((0,0,20))
        #Quadrados com as cores trocadas
        pygame.draw.rect(screen,Cartas[0],(365,100,70,100), 0)
        pygame.draw.rect(screen,Cartas[1],(365,210,70,100), 0)
        pygame.draw.rect(screen,Cartas[2],(365,320,70,100), 0)
        pygame.draw.rect(screen,Cartas[3],(365,430,70,100),0)
        pygame.draw.rect(screen,Cartas[4],(465,100,70,100), 0)
        pygame.draw.rect(screen,Cartas[5],(465,210,70,100), 0)
        pygame.draw.rect(screen,Cartas[6],(465,320,70,100), 0)
        pygame.draw.rect(screen,Cartas[7], (465,430,70,100), 0)
        pygame.draw.rect(screen,Cartas[8], (565,100,70,100), 0)
        pygame.draw.rect(screen,Cartas[9], (565,210,70,100), 0)
        pygame.draw.rect(screen,Cartas[10], (565,320,70,100), 0)
        pygame.draw.rect(screen,Cartas[11], (565,430,70,100), 0)
        




        #Quadrados amarelos
       
        


        #Quadrados com as cores trocadas




        pygame.display.flip()

main()
        
        