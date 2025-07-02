import pygame

def main():
    pygame.init()
    SW,SC = 500, 500
    screen = pygame.display.set_mode((SW, SC))
    pygame.display.set_caption("color changing sprite")


    colors = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white"),
    }
    current_color = "red"

    x, y = 30, 30
    SpW, Sph = 60, 60

    clock = pygame.time.Clock()
    
    done = False
    while not done:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                done = True

            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3  

        x = min(max(x, 0), SW - SpW)
        y = min(max(y, 0), SC - Sph)

        if x == 0 : current_color = colors["blue"]
        elif x == SW - SpW: current_color = colors["yellow"]
        elif y == 0: current_color = colors["red"]
        elif y == SC - Sph: current_color = colors["green"]
        else: current_color = colors["white"]


        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, SpW, Sph))

        pygame.display.flip()
        clock.tick(100)

    pygame.quit()

if __name__ == "__main__":
    main()