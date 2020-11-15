
"""
Proof of concept gfxdraw example

Рисуем примитивы

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
        pygame.display.set_caption("")
        # pygame.display.set_mode((600, 400)) запускаем окно, можно с флагами
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        # set_mode возвращает display surface - оснавная поверхность
        # обновляем её методами pygame.display.flip() и pygame.display.update()
        self._display_surf.fill((122, 122, 0))
        self._running = True
        # s = pygame.Surface(self._display_surf.get_size(), pygame.SRCALPHA, 32)
        # Рисуем статичную картинку
        sc = self._display_surf

        pygame.draw.rect(sc, (255, 255, 255), (20, 320, 100, 75))
        pygame.draw.rect(sc, color_light_green, (150, 320, 100, 75), 3, 0, 10, 0, 5)

        pygame.draw.line(sc, color_light_green, [10, 30], [290, 15], 3)
        pygame.draw.line(sc, color_white, [10, 50], [290, 35])
        pygame.draw.aaline(sc, color_white, [10, 70], [290, 55])

        pygame.draw.polygon(sc, color_white, [[150, 10], [180, 50], [90, 90], [30, 30]])
        pygame.draw.polygon(sc, color_white, [[250, 110], [280, 150], [190, 190], [130, 130]])
        pygame.draw.polygon(sc, color_light_green, [[350+100, 20], [180+100, 50], [190+100, 190], [30+100, 30]],10)
        # замыкаем линию True aalines - можно применить для сглаживания края полигона
        pygame.draw.aalines(sc, color_white, True, [[250, 110], [280, 150], [190, 190], [130, 130]])
        pygame.draw.lines(sc, color_light_green, False, [[10, 10], [140, 70], [280, 20]], 2)

        pygame.draw.circle(sc, color_yellow, (400, 100), 50)
        pygame.draw.circle(sc, color_pink, (600, 100), 50, 10)

        pygame.draw.ellipse(sc, color_light_green, (210, 250, 280, 100))
        pygame.draw.ellipse(sc, color_white, (210, 150, 280, 100), 20)
        pygame.gfxdraw.aaellipse(sc, 110, 150, 140, 50, color_white)

        pi = 3.14
        pygame.draw.arc(sc, color_white, (10, 50, 280, 100), 0, pi)
        pygame.draw.arc(sc, color_red, (50, 30, 200, 150), pi, 2 * pi, 5)
        # Указывается прямоугольник, описывающий эллипс, из которого вырезается дуга. Четвертый и пятый аргументы –
        # начало и конец дуги, выраженные в радианах. Нулевая точка справа.
        pygame.display.update()
        # Если функции update() не передавать аргументы, то будут обновляться значения всей поверхности окна.
        # Однако можно
        # передать более мелкую прямоугольную область или список таковых. В этом случае обновляться будут только они.
        #
        # Функция flip() решает проблему иным способом. Она дает выигрыш, если в set_mod()
        # были переданы определенные флаги
        # (аппаратное ускорение + полноэкранный режим – pygame.HWSERFACE|pygame.FULLSCREEN, двойная буферизация –
        # pygame.DOUBLEBUFF, использование OpenGL – pygame.OPENGL). Возможно, все флаги можно комбинировать вместе
        # (через |).
        # При этом, согласно документации, аппаратное ускорение работает только в полноэкранном режиме.
        pygame.time.delay(3000)

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

    def on_render(self, str_cycle_counter: str, x, y, r: int):
        pygame.display.set_caption("Цикл " + str_cycle_counter)
        # рисуем круг
        self._display_surf.fill(color_black)
        pygame.draw.circle(self._display_surf, color_red, (x, y), r)
        # обновляем окно
        pygame.display.update()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self, fps_display: int):
        # Вариант инициализации внутри метода on_execute, у нас в главной процедуре
        # if self.on_init() == False:
        #    self._running = False
        clock = pygame.time.Clock()
        cycle_counter = 1
        # координаты круга
        # скрываем за левой границей
        r = 30
        x = 0 - r
        # выравнивание по центру по вертикали
        win_width = 640
        y = win_width // 2  # TODO self._display_surf.get_size() - использовать для определения ширины
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            # альтернативный способ вызова цикла обработки событий
            # while True:
            # for i in pygame.event.get():
            #   if i.type == pygame.QUIT:
            #       return (можно использовать для выхода при вызове из функции (как тут) выходим из функции, программа
            # прерывается)
            # Пустые циклы для развития
            self.on_loop()
            self.on_render(str(cycle_counter), x, y, r)
            # Если круг полностью скрылся
            # за правой границей,
            if x >= win_width + r:
                # перемещаем его за левую
                x = 0 - r
            else:  # Если еще нет,
                # на следующей итерации цикла
                # круг отобразится немного правее
                x += 2
            # Задержка цикла для экономии ресурсов
            # 1) pygame.time.delay(20) принимает задержку в миллисекундах (1000 мс = 1 с) - не надо объект Clock
            # но лучше clock.tick(60) задержка рассчитывается сама (60 раз в сек)
            clock.tick(fps_display)
            if cycle_counter < 20:
                cycle_counter += 1
            else:
                cycle_counter = 1
        self.on_cleanup()


if __name__ == "__main__":
    fps = 20
    theApp = App()
    theApp.on_init()
    theApp.on_execute(fps)
