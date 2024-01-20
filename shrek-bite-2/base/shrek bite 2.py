import pygame


pygame.init()

screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width,screen_height))

font = pygame.font.SysFont("Arial",50)
font2 = pygame.font.SysFont("Arial",100)

land = pygame.image.load("img/dirt.jpg")
land = pygame.transform.scale(land, (1200,700))

car = pygame.image.load("img/car.png")
car = pygame.transform.scale(car, (100,100))






speed = 0.5
S, Z = 1, 450





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    screen.blit(land, (0, 0))

    screen.blit(car, (S,Z))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        S += speed
    elif keys[pygame.K_a]:
        S -= speed

    elif keys[pygame.K_s]:
        Z += speed

    elif keys[pygame.K_w]:
        Z -= speed

    if Z < 500:
        S += 1
    else:
        if keys[pygame.K_SPACE]:
            S -= 100


    pygame.display.update()
