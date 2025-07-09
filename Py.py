import pygame
import random

Screen_W, SH = 500, 400
fontsize = 72
Movement_speed = 5


pygame.init()


background_color = pygame.transform.scale(pygame.image.load("Madio.png"), (Screen_W, SH))

font = pygame.font.SysFont("Times New Roman", fontsize)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(
            pygame.Color("dodgerblue")
        )
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, Screen_W - self.rect.width), 0
        )
        self.rect.y = max(
            min(self.rect.y + y_change, SH - self.rect.height), 0
        )

        screen = pygame.display.set_mode((Screen_W, SH))
        pygame.display.set_caption("Sprite Movement")
        all_sprites = pygame.sprite.Group()

        sprite1 = Sprite(pygame.Color("black"), 20, 30)
        sprite1.rect.x, sprite1.rect.y = random.randint(0, Screen_W - sprite1.rect.width), random.randint(0, SH - sprite1.rect.height)
        all_sprites.add(sprite1)

        sprite2 = Sprite(pygame.Color("red"), 20, 30)
        sprite2.rect.x, sprite2.rect.y = random.randint(0, Screen_W - sprite2.rect.width), random.randint(0, SH - sprite2.rect.height)
        all_sprites.add(sprite2)


        running, won = True, False
        clock = pygame.time.Clock()


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN):
                    running = False


        if not won:
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Movement_speed
            y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Movement_speed
            sprite1.move(x_change, y_change)

            if sprite1.rect.colliderect(sprite2.rect):
                all_sprites.remove(sprite2)
                won = True


        screen.blit(background_color, (0, 0))
        all_sprites.draw(screen)

        if won:
            win_text = font.render("You won!", True, pygame.Color("black"))
            screen.blit(win_text, ((Screen_W - win_text.get_width()) // 2, (SH - win_text.get_height()) // 2))


        pygame.display.flip()
        clock.tick(100)


pygame.quit()