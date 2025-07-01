import pygame


pygame.init()
SCREEN_W, SH = 500, 500

display = pygame.display.set_mode((SCREEN_W, SH))
pygame.display.set_caption("Adding image and background image")

background_image = pygame.transform.scale(pygame.image.load("download.jpeg").convert(), (SCREEN_W, SH))
my_image = pygame.transform.scale(pygame.image.load("my_imaage.png").convert(), (200, 200))
my_text = pygame.font.Font(None, 36).render("Why Am I here?", True, (255, 255, 255))

def game_Loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False
        display.blit(background_image, (0, 0))
        display.blit(my_image, (200, 200))
        display.blit(my_text, (150, 450))
        pygame.display.flip()
        clock.tick(60)

        
    pygame.quit()

if __name__ == "__main__":
    game_Loop()