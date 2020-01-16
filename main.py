import pygame
import pygame.freetype


def main():
    
    pygame.init()
    click = 0
    res = (1000, 640)
    
    screen = pygame.display.set_mode(res)
    yellow = (255,255,0)
    while(True):
        for event in pygame.event.get():
            mb = pygame.mouse.get_pressed()
            if(event.type == pygame.QUIT):
                exit()
        pos = pygame.mouse.get_pos()
        r, g, b1, = 255 , 255, 0, 
        screen.fill((0,0,20))
        pygame.draw.rect(screen, (r,g,b1), (450,270,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,310,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,350,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,390,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,430,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,470,100,30), 4)
        if(pos[0] >= 450 and pos[0] <= 550 ):
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

