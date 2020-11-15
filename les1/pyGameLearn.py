
"""
Proof of concept gfxdraw example

Заготовка окна

"""

import pygame
import pygame.gfxdraw
color_light_green = (122, 222, 0)
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
        self._display_surf.fill((122, 122, 0))
        self._running = True
        # s = pygame.Surface(self._display_surf.get_size(), pygame.SRCALPHA, 32)
        pygame.display.update()
        # Если функции update() не передавать аргументы, то будут обновляться значения всей поверхности окна. Однако
        # можно
        # передать более мелкую прямоугольную область или список таковых. В этом случае обновляться будут только они.
        # Функция flip() решает проблему иным способом. Она дает выигрыш, если в set_mod() были переданы определенные
        # флаги
        # (аппаратное ускорение + полноэкранный режим – pygame.HWSERFACE|pygame.FULLSCREEN, двойная буферизация –
        # pygame.DOUBLEBUFF, использование OpenGL – pygame.OPENGL). Возможно, все флаги можно комбинировать вместе
        # (через |).
        # При этом, согласно документации, аппаратное ускорение работает только в полноэкранном режиме.

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

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self, fps_display: int):
        clock = pygame.time.Clock()
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(fps_display)
        self.on_cleanup()


if __name__ == "__main__":
    fps = 25
    theApp = App()
    theApp.on_init()
    theApp.on_execute(fps)
