import pygame
import random
#Cria uma classe de cartas
class Carta:
        def __init__(self,color,square):
            self.color = color
            self.square =pygame.Rect(square)
            self.match = False
            self.picked = 0
        def show (self):
            if(self.picked == False):
                pygame.draw.rect(screen,self.color,self.coordinates, 0)



#main só para ficar bonito
def main():
    #todas as cores e variaveis utilizadas
    azul =(0,0,255)
    verde =(0,255,0)
    vermelho =(255,0,0)
    lilas =(177,33,199)
    azul_claro=(0,239,255)
    laranja=(255,145,0)
    rosa = (240,15,240)
    verde_ranho = (87,111,30)
    cont= 0
    penalização = 0
    score = 0
    i= 0
    comp=[]
    #fazer shuffle
    cores = [azul,azul,verde,verde,vermelho,vermelho,lilas,lilas,azul_claro,azul_claro,laranja,laranja,rosa,rosa,verde_ranho,verde_ranho]
    random.shuffle(cores)

    #fazemos cartas amarelas    
    C1 = Carta((255,255,0),(365,100,70,100))
    C2 = Carta((255,255,0),(365,210,70,100))
    C3 = Carta((255,255,0),(365,320,70,100))
    C4 = Carta((255,255,0),(365,430,70,100))
    C5 = Carta((255,255,0),(465,100,70,100))
    C6 = Carta((255,255,0),(465,210,70,100))
    C7 = Carta((255,255,0),(465,320,70,100))
    C8 = Carta((255,255,0),(465,430,70,100))
    C9 = Carta((255,255,0),(565,100,70,100))
    C10= Carta((255,255,0),(565,210,70,100))
    C11= Carta((255,255,0),(565,320,70,100))
    C12= Carta((255,255,0),(565,430,70,100))
    C13 = Carta((255,255,0),(665,100,70,100))
    C14= Carta((255,255,0),(665,210,70,100))
    C15= Carta((255,255,0),(665,320,70,100))
    C16= Carta((255,255,0),(665,430,70,100))
    #Se elas já foram "viradas" ou não
    Cartas = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    
   
   

    
    
    #resolução do ecrã
    res = (1000, 1000)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            
            if(event.type == pygame.QUIT):
                exit()

            pos = pygame.mouse.get_pos()
            if(cont < 2):

                if(C1.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C1.color = cores[0]
                    comp.append(C1.color)
                    Cartas[0] = True
                    cont += 1
                elif(C2.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C2.color = cores[1]
                    comp.append(C2.color)
                    Cartas[2] = True
                    cont += 1
                elif(C3.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C3.color = cores[2]
                    comp.append( C3.color)
                    Cartas[2] = True
                    cont += 1
                elif(C4.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C4.color = cores[3]
                    comp.append( C4.color)
                    Cartas[3] = True
                    cont += 1
                elif(C5.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C5.color = cores[4]
                    comp.append( C5.color)
                    Cartas[4] = True
                    cont += 1
                elif(C6.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C6.color = cores[5]
                    comp.append( C6.color)
                    Cartas[5] = True
                    cont += 1
                elif(C7.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C7.color = cores[6]
                    comp.append( C7.color)
                    Cartas[6] = True
                    cont += 1
                elif(C8.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C8.color = cores[7]
                    comp.append( C8.color)
                    Cartas[7] = True
                    cont += 1
                elif(C9.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C9.color = cores[8]
                    comp.append( C9.color)
                    Cartas[8] = True
                    cont += 1
                elif(C10.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP): 
                    C10.color = cores[9]
                    comp.append(C10.color)
                    Cartas[9] = True
                    cont += 1
                elif(C11.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C11.color = cores[10]
                    comp.append(C11.color)
                    Cartas[10] = True
                    cont += 1
                elif(C12.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C12.color = cores[11]
                    comp.append(C12.color)
                    Cartas[11] = True
                    cont += 1
                elif(C13.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C13.color = cores[12]
                    comp.append(C13.color)
                    Cartas[12] = True
                    cont += 1
                elif(C14.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C14.color = cores[13]
                    comp.append(C14.color)
                    Cartas[13] = True
                    cont += 1
                elif(C15.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C15.color = cores[14]
                    comp.append(C15.color)
                    Cartas[14] = True
                    cont += 1
                elif(C16.square.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP):
                    C16.color = cores[15]
                    comp.append(C16.color)
                    Cartas[15] = True
                    cont += 1
            else :
                    if (comp[0] == comp[1]):
                        score += 100
                        comp.pop(0)
                        comp.pop(0)
                        while(i < 2):
                            for index in Cartas:
                                if (Cartas[index] == True):
                                    comp.append (index)
                                    
                            i += 1
                        while (i < 2):
                            C[comp[i]] =Carta((0,0,20),(920,50,70,100))
                        
                        comp.pop(0) 
                    else:
                        score -= penalização
                        penalização -= 20
                        comp.pop(0)
                        comp.pop(0)
                        while(i < 2):
                            for index in Cartas:
                                if(Cartas[index] == True):
                                    comp.append (index)
                            i += 1
                        while (i < 2):
                            C[comp[i]].color = (255,255,0)
                            Cartas[comp[i]] = False
                        comp.pop(0)
                        comp.pop(0)

                        


 
        screen.fill((0,0,20))
        #Quadrados com as cores trocadas
        
        pygame.draw.rect(screen,C1.color,(365,100,70,100), 0)
        pygame.draw.rect(screen,C2.color,(365,210,70,100), 0)
        pygame.draw.rect(screen,C3.color,(365,320,70,100), 0)
        pygame.draw.rect(screen,C4.color,(365,430,70,100),0)
        pygame.draw.rect(screen,C5.color,(465,100,70,100), 0)
        pygame.draw.rect(screen,C6.color,(465,210,70,100), 0)
        pygame.draw.rect(screen,C7.color,(465,320,70,100), 0)
        pygame.draw.rect(screen,C8.color, (465,430,70,100), 0)
        pygame.draw.rect(screen,C9.color, (565,100,70,100), 0)
        pygame.draw.rect(screen,C10.color, (565,210,70,100), 0)
        pygame.draw.rect(screen,C11.color, (565,320,70,100), 0)
        pygame.draw.rect(screen,C12.color, (565,430,70,100), 0)
        pygame.draw.rect(screen,C13.color, (665,100,70,100), 0)
        pygame.draw.rect(screen,C14.color, (665,210,70,100), 0)
        pygame.draw.rect(screen,C15.color, (665,320,70,100), 0)
        pygame.draw.rect(screen,C16.color, (665,430,70,100), 0)
        




        #Quadrados amarelos
       
        


        #Quadrados com as cores trocadas




        pygame.display.flip()

main()
        
        