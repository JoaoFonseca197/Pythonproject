import pygame
import pygame.freetype


def main():
    
    pygame.init()
    click = 0
    res = (1000, 640)
    my_font = pygame.freetype.Font(Noto_Sans.ttf, 24)
    screen = pygame.display.set_mode(res)
    yellow = (255,255,0)
    while(True):
        for event in pygame.event.get():
            c_x,c_y = pygame.mouse.get_pos()
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
        my_font.render_to(screen, (450, 270), "3x4", yellow)
        if(c_x >= 450 and c_x <= 550 ):
            if (c_y >= 270 and c_y <= 300):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,270,100,30), 4)
                if(mb[0]):
                    click += 1
                    print(click)
            elif (c_y >= 310 and c_y <= 340):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,310,100,30), 4)
            elif (c_y >= 350 and c_y <= 380):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,350,100,30), 4)
            elif (c_y >= 390 and c_y <= 420):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,390,100,30), 4)
            elif (c_y >= 430 and c_y <= 460):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,430,100,30), 4)
            elif (c_y >= 470 and c_y <= 500):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (450,470,100,30), 4) 
        

       

        pygame.display.flip()

main()

