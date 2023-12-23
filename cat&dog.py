import pygame


pygame.init()

screen_width = 1080
screen_hight = 720

screen = pygame.display.set_mode((screen_width, screen_hight))

img = pygame.image.load("cat&dog/cat.jpg")
img_s = pygame.transform.scale(img, (1080, 720))
img2 = pygame.image.load("cat&dog/dog.jpg")
img2_s = pygame.transform.scale(img2, (1080, 720))


def cat():
    if img_vivod == "Кот":
        screen.blit(img_s, (0, 0))

def dog():
    if img_vivod == "Собака":
        screen.blit(img2_s, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    img_vivod = input("Кот или Собака?: ")

    cat()
    dog()



    pygame.display.update()
