from random import randint
import pygame as pg
import sys

pg.time.set_timer(pg.USEREVENT, 3000)

W = 400
H = 400
WHITE = (255, 255, 255)
CARS = ('car1.png', 'car2.png', 'car3.png')
# для хранения готовых машин-поверхностей
CARS_SURF = []

# надо установить видео режим
# до вызова image.load()
sc = pg.display.set_mode((W, H))

for i in range(len(CARS)):
    CARS_SURF.append(
        pg.image.load(CARS[i]).convert_alpha())


class Car(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(1, 3)

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()


class MyCar(pg.sprite.Sprite):
    def __init__(self, x, surf):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, H - 100))
        # у машин будет разная скорость
        self.speed = 1

    def update(self):
        # self.rect.x += self.speed
        pass


cars = pg.sprite.Group()

# добавляем первую машину,
# которая появляется сразу

Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
my_car = MyCar(W // 2, CARS_SURF[0])
sc.blit(my_car.image, my_car.rect)
go_left = False
go_right = False
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
            # print(my_car.rect)
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                go_left = True
            elif i.key == pg.K_RIGHT:
                go_right = True
        elif i.type == pg.KEYUP and (i.key == pg.K_LEFT or i.key == pg.K_RIGHT):
            go_left = False
            go_right = False

    sc.fill(WHITE)
    cars.draw(sc)
    if go_left:
        my_car.rect.x -= 3
    elif go_right:
        my_car.rect.x += 3
    sc.blit(my_car.image, my_car.rect)
    pg.display.update()

    if not (pg.sprite.spritecollideany(my_car, cars) == None):
        sys.exit()

    pg.time.delay(20)

    cars.update()