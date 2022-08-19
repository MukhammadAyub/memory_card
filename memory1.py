from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.direction = ' '

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class PLayer(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

rocky = PLayer('rock.png', 330, 400, 80, 100, 10)

mixer.init()

mixer.music.load('space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))
display.set_caption('Shooter')
background = transform.scale(image.load('back.png'), (700, 500))
clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0, 0))
        rocky.reset()
        rocky.update()
        
        display.update()
        clock.tick(60)
