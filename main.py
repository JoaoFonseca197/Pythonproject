import pygame
import pygame.freetype


def main():
    
    pygame.init()
    click = 0
    res = (1000, 640)
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
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
        my_font.render_to(screen, (480,275), "3x4", (255,255,0))
        my_font.render_to(screen, (480,315), "4x4", (255,255,0))
        my_font.render_to(screen, (480,355), "5x4", (255,255,0))
        my_font.render_to(screen, (480,395), "6x4", (255,255,0))
        my_font.render_to(screen, (480,435), "6x5", (255,255,0))
        my_font.render_to(screen, (480,475), "6x6", (255,255,0))
        my_font.render_to(screen, (130,555), "QUIT", (255,255,0))
        pygame.draw.rect(screen, (r,g,b1), (450,270,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,310,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,350,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,390,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,430,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,470,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (450,470,100,30), 4)
        pygame.draw.rect(screen, (r,g,b1), (100,550,100,30), 4)
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
        elif(pos[0] >= 100 and pos[0] <= 200 ):
            if(pos[1] >= 550 and pos[1] <= 580):
                b1 = 200
                pygame.draw.rect(screen, (r,g,b1), (100,550,100,30), 4)
                if(mb[0]):
                    exit()

       

        pygame.display.flip()

main()
