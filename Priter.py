import pygame
import random

pygame.init()


Sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2



Blue = pygame.Color("blue")
LightBlue = pygame.Color("lightblue")
Darkblue = pygame.Color("darkblue")



Yellow = pygame.Color("yellow")
Magenta = pygame.Color("magenta")
orange = pygame.Color("orange")
white = pygame.Color("white")


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(Sprite_color_change_event, {"sprite": self}))
            pygame.event.post(pygame.event.Event(background_color_change_event))
    def change_color(self):
        self.image.fill(random.choice([Yellow, Magenta, orange, white]))


def change_background_color():
    global background_color
    background_color = random.choice([Blue, LightBlue, Darkblue])


all_sprites_list = pygame.sprite.Group()

spl = Sprite(white, 20, 30)

spl.rect.x = random.randint(0, 480)
spl.rect.y = random.randint(0, 370)
all_sprites_list.add(spl)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary sprite")
background_color = Blue
screen.fill(background_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == Sprite_color_change_event:
            spl.change_color()
        elif event.type == background_color_change_event:
            change_background_color()
            

    all_sprites_list.update()
    screen.fill(background_color)
    all_sprites_list.draw(screen)


    pygame.display.flip()
    clock.tick(240)

pygame.quit()