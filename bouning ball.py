import pygame
import os

fps = 1000
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
yellow = (255,255,0)
width = 700
height = 500
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
screen.fill(white)
clock = pygame.time.Clock()
speed = [1,1]
popayee = pygame.image.load("f1.png")
popayee = pygame.transform.scale(popayee, (80,80))
popayee_rect = popayee.get_rect(x = 100, y=100)
run = True
while run:
    clock.tick(fps)
    popayee_rect = popayee_rect.move(speed)
    if popayee_rect.left < 0 or   popayee_rect.right > width:
        speed[0]=-speed[0]
    if popayee_rect.top < 0 or   popayee_rect.bottom > height:
        speed[1]=-speed[1] 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                screen.fill(yellow)
            if event.key == pygame.K_ESCAPE:
                screen.fill(black)
                run = False
            if event.key == pygame.K_w:
                popayee_rect.y-=10


    '''pressed = pygame.key.get_pressed()
    if pressed[pygame.K_p]:
               popayee_rect.y+=10'''
    screen.fill(white)                       
    screen.blit(popayee, popayee_rect)                                   
    pygame.display.update()   
pygame.quit()            
            


        
