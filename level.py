import pygame



def main():
    verde = (0,255,0)
    azul = (0,0,255)
    lilas =(177,33,199)
    vermelho = (255,0,0)
    cores = [verde,azul,lilas,vermelho]
    pygame.init()
    
    res = (1000, 640)
    
    screen = pygame.display.set_mode(res)

    while(True):
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                exit()

        r, g, b1, = 255 , 255, 0, 
        screen.fill((0,0,20))
        pygame.draw.rect(screen, cores[0], (465,100,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (465,210,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (465,320,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (465,430,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (365,100,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (365,210,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (365,320,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (365,430,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (565,100,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (565,210,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (565,320,70,100), 4)
        pygame.draw.rect(screen, (r,g,b1), (565,430,70,100), 4)
        pygame.display.flip()

main()
        
        