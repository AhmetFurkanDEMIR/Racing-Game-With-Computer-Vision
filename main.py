import demir_ai_API

import pygame
from pygame.locals import *
from random import randint
import sys

import cv2

import keras

from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time

import imutils
from imutils.video import VideoStream


model_path = os.path.join('..', 'snapshots', 'resnet50_csv_20.h5')

model = models.load_model("model.h5", backbone_name='resnet50')

labels_to_names = {0: "R I G H T", 1: "L E F T", 2: "T A K E"}

vs = VideoStream(src=0).start() 

c = 0


pygame.init()
winWidth = 720
winHeight = 720

Game_Window = pygame.display.set_mode((winWidth, winHeight))
Game_Window.blit(pygame.image.load('images/background.jpg'), (0, 0))
pygame.display.update()

while True:

    pressed = False

    for event in pygame.event.get():

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE:

                pressed = True
                break

        elif event.type == pygame.QUIT:

            pygame.quit()
            sys.exit(0)

    if pressed == True:

        break

clock = pygame.time.Clock()
bkg_texture_str = "images/road.png"

background_list = pygame.sprite.Group()
bkg_texture = pygame.transform.scale((pygame.image.load(bkg_texture_str)), (winWidth, winHeight))


class Background(pygame.sprite.Sprite):

    x = 0
    y = 0
    maxspeed = 10

    def __init__(self, texture, x=0, y=0, width=1, height=1):

        super(Background, self).__init__()

        self.image = texture
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        pygame.draw.rect(self.image, (0, 0, 0), [self.x, self.y, width, height])
        self.rect = self.image.get_rect()

    def scroll(self, speed):

        self.y += speed

        if self.y > winHeight:

            self.y = -winHeight

    def update(self, speed):

        self.scroll(speed)

    def draw(self, surface):

        surface.blit(self.image, (self.x, self.y))


class CarSprite(pygame.sprite.Sprite):

    def __init__(self, image, position, speed):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.position = position
        self.speed = speed
        self.right = self.left = False
        self.rect = self.image.get_rect()

    def update(self):

        x, y = self.position

        if self.right:

            if 50 <= x + self.speed <= 670:

                x += self.speed

        elif self.left:

            if 50 <= x - self.speed <= 670:

                x -= self.speed

        self.position = (x, y)
        self.rect.center = self.position


class PadSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):

        super(PadSprite, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.position = position
        self.rect.center = position

    def update(self, speed):

        x, y = self.position
        self.position = (x, y+speed)
        self.rect.center = self.position



def text_objects(text, font):

    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

a = None



while True:

    BkgSprite1 = Background(bkg_texture, 0, winHeight * (-1))
    BkgSprite2 = Background(bkg_texture, 0, 0)
    BkgSprite3 = Background(bkg_texture, 0, winHeight)

    background_list.add(BkgSprite1)
    background_list.add(BkgSprite2)
    background_list.add(BkgSprite3)

    pads_group = pygame.sprite.Group()
    car = CarSprite('images/car.png', (360, 600), 7)
    car_render = pygame.sprite.RenderPlain(car)

    stop = False
    restart = False

    if a == True:
        break

    while True:

        frame = vs.read()
        frame = imutils.resize(frame, width=600)

        image = frame
        draw = image.copy()

        draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

        image = preprocess_image(image)
        image, scale = resize_image(image)

        boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))

        boxes /= scale

        for box, score, label in zip(boxes[0], scores[0], labels[0]):

            if score < 0.8:
                break
                    
            color = label_color(label)
                
            b = box.astype(int)
            draw_box(draw, b, color=color)
                
            caption = "{} {:.3f}".format(labels_to_names[label], score)

            print(labels_to_names[label])

            if labels_to_names[label] == "T A K E":

                stop = False
                car.left = False
                car.right = False


            if labels_to_names[label] == 'R I G H T':

                stop = False
                car.left = False
                car.right = True

            if labels_to_names[label] == "L E F T":

                stop = False
                car.left = True
                car.right = False

            cv2.putText(frame, caption, (b[0], b[1] - 9),cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1)
            cv2.rectangle(frame, (b[0], b[1]), (b[2], b[3]), (0, 255, 0), 2)
       

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        a = None

        if key == ord("q"):
            a = True
            break        

        if len(pads_group) == 0:
            pads_group.add(PadSprite(f'images/pad{randint(1,3)}.png', (randint(70, 650), -50)))

        else:

            if pads_group.sprites()[-1].position[1] >= randint(300, 400):
                oldx = None

                for i in range(0, randint(1, 2)):

                    if oldx is None:
                        oldx = x = randint(70, 650)

                    else:

                        if oldx + 350 < 650:
                            x = oldx + 300

                        else:
                            x = oldx - 300

                    pads_group.add(PadSprite(f'images/pad{randint(1, 3)}.png', (x, -50)))
        hit = pygame.sprite.spritecollide(car, pads_group, False)

        if hit:

            car = CarSprite('images/boom.png', (car.position[0], car.position[1]), 0)
            car_render = pygame.sprite.RenderPlain(car)
            car_render.update()

            BkgSprite1.draw(Game_Window)
            BkgSprite2.draw(Game_Window)
            BkgSprite3.draw(Game_Window)
            pads_group.draw(Game_Window)

            car_render.draw(Game_Window)
            largeText = pygame.font.SysFont("comicsansms", 20)
            TextSurf, TextRect = text_objects("Kaybettiniz, oyunu yeniden başlatmak için space'e basınız", largeText)
            TextRect.center = ((winWidth // 2), (winHeight // 2))
            Game_Window.blit(TextSurf, TextRect)

            while True:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == pygame.KEYUP:

                        if event.key == pygame.K_SPACE:
                            restart = True

                if restart:
                    break

                pygame.display.update()
                clock.tick(15)

        if restart:
            break

        if not stop:

            background_list.update(4)
            pads_group.update(4)

        car_render.update()
        BkgSprite1.draw(Game_Window)
        BkgSprite2.draw(Game_Window)

        BkgSprite3.draw(Game_Window)
        pads_group.draw(Game_Window)
        car_render.draw(Game_Window)


        clock.tick(60)
        pygame.display.flip()


cv2.destroyAllWindows()
vs.stop()