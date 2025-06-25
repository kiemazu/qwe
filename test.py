import pygame
import math
pygame.init()
size = w, h = 626, 375
screen = pygame.display.set_mode(size)
class Coordinate:
    def __init__(self):
        self.x = 20
        self.f = pygame.font.SysFont('microsofttaile', 30)
        self.color = (0,0,0)
        self.red = (255,255,255)
    def coo_d(self):
        if self.x <= 299:
            self.x += 1
        else:
            self.x -= 0
    def coo_a(self):
        if self.x >= 1:
            self.x -= 1
        else:
            self.x -= 0
    def spawn(self):
        self.text = self.f.render(f'{self.x}', 1, self.color, self.red)
        screen.blit(self.text, (4,4))
class background:
    def __init__(self):
        self.player2 = False
        self.scrol = 0
        self.copy = 2
        self.sko = 4
        self.img = pygame.image.load("fon.jpg").convert()
        self.wdth = self.img.get_width()
    def start(self):
        self.player2 = True
    def scroll_d(self):
        self.scrol -= self.sko
    def scroll_a(self):
        self.scrol += self.sko
    def stop(self):
        self.sko = 0
    def fix(self):
        if self.scrol > 0:
            self.scrol -= self.wdth
        if self.scrol < -self.wdth:
            self.scrol += self.wdth
    def ani(self, screen):
        for i in range(-1, self.copy):
            screen.blit(self.img, (i * self.wdth + self.scrol, 0))
    def crushed(self):
        self.sko = 0
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, file, file2,file3, file4, w, h, w1, h1, hp, str):
        super().__init__()
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.image_l = pygame.image.load(file2).convert_alpha()
        self.image_l = pygame.transform.scale(self.image_l, (w, h))
        self.rect = self.image.get_rect(center = (x,y))
        self.hit_r = []
        self.hit_l = []
        self.cur_cadr = 0
        self.cadr_coun = 0
        self.hp = hp
        self.strengh = str
        self.dx = 0
        self.dy = 0
        self.reload = 0
        self.delay = 30
        self.atack = False
        self.hitted = False
        self.right = True
        self.left = False
        self.move = False
        self.nazemle = False
        self.alive = True
        self.stop = False
        self.victory = False
        self.kadr_count = 0
        self.curr_kadr = 0
        self.speed = 0.2
        self.kadri_r = []
        self.kadri_l = []
        self.kadr_smerti_r = pygame.image.load(file3).convert_alpha()
        self.kadr_smerti_r = pygame.transform.scale(self.kadr_smerti_r, (w1, h1))
        self.kadr_smerti_l = pygame.image.load(file4).convert_alpha()
        self.kadr_smerti_l = pygame.transform.scale(self.kadr_smerti_l, (w1, h1))
    def jump(self):
        if self.alive:
            if (self.nazemle):
                self.dy -= 20
                self.nazemle = False
        else:
            pass
    def prizemlenie(self, *args):
        if not self.nazemle:
            self.dy += 1
        self.rect.y += self.dy
        if self.rect.y > args[0]:
            self.dy = 0
            self.nazemle = True
    def pravo(self):
        self.rect.x += 3
    def levo(self):
        self.rect.x -= 3
    def upd_r(self):
        self.speed = 0.3
        if self.alive:
            self.right = True
            self.left = False
            self.move = True
        if self.move:
            self.kadr_count += self.speed
            if self.kadr_count >= 1:
                self.kadr_count = 0
                self.curr_kadr = (self.curr_kadr + 1) % len(self.kadri_r)
    def upd_l(self):
        self.speed = 0.3
        if self.alive:
            self.left = True
            self.right = False
            self.move = True
        if self.move:
            self.kadr_count += self.speed
            if self.kadr_count >= 1:
                self.kadr_count = 0
                self.curr_kadr = (self.curr_kadr - 1) % len(self.kadri_l)
    def get_hit_r(self):
        self.speed = 0.3
        if self.hitted:
            self.cadr_coun += self.speed
            if self.cadr_coun >= 1:
                self.cadr_coun = 0
                self.cur_cadr  = (self.cur_cadr + 1) % len(self.hit_r)
                if self.cur_cadr == 0:
                    self.hitted = False
    def get_hit_l(self):
        self.speed = 0.3
        if self.hitted:
            self.cadr_coun += self.speed
            if self.cadr_coun >= 1:
                self.cadr_coun = 0
                self.cur_cadr = (self.cur_cadr - 1) % len(self.hit_l)
                if self.cur_cadr == 0:
                    self.hitted = False
    def attack(self, target):
        self.move = False
        if not self.victory:
            if self.alive and self.reload <= 0:
                if self.rect.colliderect(target.rect):
                    target.hp -= self.strengh
                    target.hitted = True
                    self.reload = self.delay
                    if target.hp <= 0:
                        target.death()
                        self.victory = True
            else:
                pass
        else:
            pass
    def death(self):
        if self.hp <= 0:
            self.alive = False
            self.stop = True
    def draw(self):
        if self.alive:
            if not self.hitted:
                if not self.move:
                    if self.right:
                        screen.blit(self.image, self.rect)
                    else:
                        screen.blit(self.image_l, self.rect)
                else:
                    if self.right:
                        screen.blit(self.kadri_r[self.curr_kadr], self.rect)
                    else:
                        screen.blit(self.kadri_l[self.curr_kadr], self.rect)
            else:
                if self.right:
                    screen.blit(self.hit_r[self.cur_cadr], self.rect)
                else:
                    screen.blit(self.hit_l[self.cur_cadr], self.rect)
            self.move = False
        else:
            if self.right:
                screen.blit(self.kadr_smerti_r, self.rect)
            else:
                screen.blit(self.kadr_smerti_l, self.rect)
class Person(Sprite):
    def __init__(self, x, y, file, file2, file3, file4 ,w, h, w1, h1, hp, str,):
        super().__init__(x, y, file, file2,file3, file4, w, h, w1, h1, hp ,str,)
        self.take_weapon = False
        self.me4 = []
        self.qwe = 0
        self.asd = 0
        self.weapon_r = pygame.image.load('img/right/weapon/w_2.png')
        self.weapon_r = pygame.transform.scale(self.weapon_r, (80, 80))
        self.weapon_l = pygame.image.load('img/left/weapon/w_2.png')
        self.weapon_l = pygame.transform.scale(self.weapon_l, (80, 80))
        for i in range(1,9):
            img = pygame.image.load(f'img/right/k_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (80, 80))
            self.kadri_r.append(img)
        for i in range(1,9):
            img = pygame.image.load(f'img/left/k_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (80, 80))
            self.kadri_l.append(img)
        for i in range(1,4):
            img = pygame.image.load(f'img/cat_h_r/h_{i}.png')
            img = pygame.transform.scale(img, (80,80))
            self.hit_r.append(img)
        for i in range(1,4):
            img = pygame.image.load(f'img/cat_h_l/h_{i}.png')
            img = pygame.transform.scale(img, (80,80))
            self.hit_l.append(img)
    def attack(self, target):
        self.move = False
        if not self.victory:
            if self.alive and self.reload <= 0:
                if self.rect.colliderect(target.rect):
                    target.hp -= self.strengh
                    target.hitted = True
                    self.reload = self.delay
                    if target.hp <= 0:
                        target.death()
                        self.victory = True
            else:
                pass
        else:
            pass
    def upd_wea(self):
        self.take_weapon = True
    def get_hit_r(self):
        self.speed = 0.17
        if self.hitted:
            self.cadr_coun += self.speed
            if self.cadr_coun >= 1:
                self.cadr_coun = 0
                self.cur_cadr = (self.cur_cadr + 1) % len(self.hit_r)
                if self.cur_cadr == 0:
                    self.hitted = False
    def get_hit_l(self):
        self.speed = 0.09
        if self.hitted:
            self.cadr_coun += self.speed
            if self.cadr_coun >= 1:
                self.cadr_coun = 0
                self.cur_cadr = (self.cur_cadr + 1) % len(self.hit_l)
                if self.cur_cadr == 0:
                    self.hitted = False
    def draw(self):
        if self.alive:
            if not self.take_weapon:
                if not self.hitted:
                    if not self.move:
                        if self.right:
                            screen.blit(self.image, self.rect)
                        else:
                            screen.blit(self.image_l, self.rect)
                    else:
                        if self.right:
                            screen.blit(self.kadri_r[self.curr_kadr], self.rect)
                        else:
                            screen.blit(self.kadri_l[self.curr_kadr], self.rect)
                else:
                    if self.right:
                        screen.blit(self.hit_r[self.cur_cadr], self.rect)
                    else:
                        screen.blit(self.hit_l[self.cur_cadr], self.rect)
                self.move = False
            else:
                if self.right:
                    screen.blit(self.weapon_r, self.rect)
                else:
                    screen.blit(self.weapon_l, self.rect)
                self.take_weapon = False
        else:
            if self.right:
                screen.blit(self.kadr_smerti_r, self.rect)
            else:
                screen.blit(self.kadr_smerti_l, self.rect)

class NPC(Sprite):
    def __init__(self, x, y, file, file2,file3, file4, w, h, w1, h1, hp , str,):
        super().__init__(x, y, file, file2, file3, file4, w, h, w1, h1, hp, str,)
        self.right = False
        self.left = True
        self.level = 1
        for i in range(1,8):
            img = pygame.image.load(f'img/npc/mush_run_r/m_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (120,120))
            self.kadri_r.append(img)
        for i in range(1,8):
            img = pygame.image.load(f'img/npc/mush_run_l/m_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (120,120))
            self.kadri_l.append(img)
        for i in range(1,5):
            img = pygame.image.load(f'img/npc/hitted_r/h_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (120, 120))
            self.hit_r.append(img)
        for i in range(1,5):
            img = pygame.image.load(f'img/npc/hitted_l/h_{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (120, 120))
            self.hit_l.append(img)
    def run(self, target):
        if not self.stop:
            x = target.rect.x - self.rect.x
            dist = max(1, math.sqrt(x * x))
            self.rect.x += (x/dist) * 2
    def mesto_d(self):
        self.rect.x -= self.speed
    def mesto_a(self):
        self.rect.x += self.speed

fps = pygame.time.Clock()
fon = background()
fon.start()
mush = NPC(700, 236, 'img/npc/npc_death_R/m.png', 'img/npc/npc_death_L/m.png', 'img/npc/npc_death_R/d_8.png','img/npc/npc_death_L/d_8.png', 130, 130, 130 ,119,  4,  0)
c4et = Coordinate()
cat = Person(100, 100, 'img/right/stay.png', 'img/left/stay.png', 'img/dez/de_r.png', 'img/dez/de_l.png',80, 80, 100 ,78,   10,  1  )
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    scrolling = False
    cat_fake_moving = False
    if cat.reload > 0:
        cat.reload -= 1
    if mush.reload > 0:
        mush.reload -= 1
    if cat.hitted:
        if cat.right:
            cat.get_hit_r()
        else:
            cat.get_hit_l()
    if mush.hitted:
        if mush.right:
            mush.get_hit_r()
        else:
            mush.get_hit_l()
    if keys[pygame.K_d]:
        c4et.coo_d()
        if cat.alive:
            cat.upd_r()
        if c4et.x < 200:
            if cat.rect.x < 250:
                if cat.alive:
                    cat.pravo()
                scrolling = False
                cat_fake_moving = False
            if cat.rect.x >= 250:
                if cat.alive:
                    fon.scroll_d()
                scrolling = True
                cat_fake_moving = True
                if mush.alive:
                    mush.rect.x -= 1
                else:
                    mush.rect.x -= 4
        else:
            if cat.rect.x < 550:
                if cat.alive:
                    cat.pravo()
                scrolling = False
                cat_fake_moving = False
            else:
                pass
    if keys[pygame.K_a]:
        c4et.coo_a()
        cat.upd_l()
        if c4et.x >= 80:
            if cat.rect.x > 260:
                if cat.alive:
                    cat.levo()
                scrolling = False
                cat_fake_moving = False
            if cat.rect.x <= 260:
                if cat.alive:
                    fon.scroll_a()
                scrolling = True
                cat_fake_moving = True
                if mush.alive:
                    mush.rect.x += 1
                else:
                    mush.rect.x +=4
        else:
            if cat.rect.x >= 0:
                if cat.alive:
                    cat.levo()
                scrolling = False
                cat_fake_moving = False
            else:
                pass
    if keys[pygame.K_SPACE]:
        cat.jump()
    if mouse[0]:
        cat.atack = True
        cat.upd_wea()
        cat.attack(mush)
    if mush.victory:
        print('loser')
    fon.ani(screen)
    mush.draw()
    if not scrolling:
        mush.run(cat)
    if mush.rect.colliderect(cat.rect):
        mush.attack(cat)
    else:
        if cat.right and mush.left and cat.rect.x <= mush.rect.x and cat_fake_moving:
            if mush.alive:
                mush.run(cat)
            else:
                mush.stop = True
        if cat.left and mush.right and cat.rect.x >= mush.rect.x and cat_fake_moving:
            if mush.alive:
                mush.run(cat)
            else:
                mush.stop = True
        else:
            mush.move = False
    if cat.rect.x <= mush.rect.x:
        mush.upd_l()
    else:
        mush.upd_r()
    c4et.spawn()
    cat.prizemlenie(196)
    cat.draw()
    pygame.display.flip()
    fps.tick(60)
pygame.quit()
