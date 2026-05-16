import pygame
pygame.init()
Screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("1v1 Sim")
frps = 40
clock = pygame.time.Clock()
b = []
m_b = 4
R3 = pygame.image.load("C:/Users/vijay/OneDrive/Desktop/Python Game Developer/images/R3.webp")

R3 = pygame.transform.scale(R3,(1000,500))
R4 = pygame.image.load("C:/Users/vijay/OneDrive/Desktop/Python Game Developer/images/R6.png")
R4 = pygame.transform.scale(R4,(120,80))
R4 = pygame.transform.rotate(R4,360)
pygame.display.update()
R = pygame.Rect(750,250,100,60)

def img_add(R):
    Screen.blit(R3,(0,0))
    Screen.blit(R4,(R.x,R.y))
    for i in b:
        pygame.draw.rect(Screen,"red",i)
    pygame.display.update()
def move_spaceship(keys,R):
    if keys[pygame.K_LEFT] and R.x > 0:
        R.x = R.x - 1
    if keys[pygame.K_RIGHT] and R.x < 900:
        R.x = R.x + 1
    if keys[pygame.K_UP] and R.y >= 0:
        R.y = R.y - 1
    if keys[pygame.K_DOWN] and R.y <=440:
        R.y = R.y + 1

def move_bullets(R,b):
    for i in b:
        i.y = i.y - 2.3
        if i.y < 0:
            b.remove(i)
            #score = score - 1
        if i.colliderect(R):
            #score = score -1
            b.remove(i)



















































while(1):
    clock.tick(290)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
             if i.key == pygame.K_SPACE:
                 if len(b) < m_b:
                     bb = pygame.Rect(R.x,R.y - 50,5,10)
                     b.append(bb)

    img_add(R) 
    move_bullets(R,b)
    keys = pygame.key.get_pressed()
    pygame.display.update()
    move_spaceship(keys,R)

    pygame.display.update()
