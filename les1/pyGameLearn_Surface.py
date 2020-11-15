
"""
Proof of concept gfxdraw example

Заготовка окна

"""

import pygame
import pygame.gfxdraw
color_light_green = (122, 222, 0)
color_sem_green = (122, 122, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 225, 0)
color_pink = (230, 50, 230)
color_black = (0, 0, 0)


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Работаем с Surface")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        print(type(self._display_surf))
        self._display_surf.fill(color_sem_green)
        self._running = True
        # s = pygame.Surface(self._display_surf.get_size(), pygame.SRCALPHA, 32)

        sub_surface = pygame.Surface((200, 150))
        sub_surface.fill(color_white)
        # Делаем прозрачность
        sub_surface.set_alpha(200)
        pygame.draw.rect(self._display_surf, (0, 255, 0), (0, 80, 300, 40))
        self._display_surf.blit(sub_surface, (50, 25))

        pygame.display.update()

    def on_event(self, event):
        # печатаем события
        # print(pygame.QUIT)
        # print(event)
        # print(event.type)
        if event.type == pygame.QUIT:
            self._running = False

        # Обработка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q" or event.unicode == "й":
                self._running = False


    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self, fps_display: int):
        clock = pygame.time.Clock()
        sub_surface2 = pygame.Surface((300, 300))
        sub_surface2.fill(color_red)
        sub_surface3 = pygame.Surface((100, 150))
        sub_surface3.fill(color_white)
        sub_surface3.set_alpha(200)
        sub_surface4 = pygame.Surface((50, 50))
        sub_surface4.fill(color_black)
        pygame.draw.circle(sub_surface4, color_white, (20, 20), 10)
        x = 0
        y = 0
        while self._running and (x < 400):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()

            x += 2
            y += 1
            self._display_surf.fill(color_sem_green)
            sub_surface2.fill(color_red)

            sub_surface2.blit(sub_surface4, (x, 150 - y))
            sub_surface2.blit(sub_surface3, (x, y))
            self._display_surf.blit(sub_surface2, (x, y))

            pygame.display.update()

            clock.tick(fps_display)
        self.on_cleanup()


if __name__ == "__main__":
    fps = 25
    theApp = App()
    theApp.on_init()
    theApp.on_execute(fps)
