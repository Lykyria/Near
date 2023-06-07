from typing import Any
import pygame
import random
import sys
import os


oc_sprite = os.path.join(os.path.dirname(__file__), 'data')
sound = os.path.join(os.path.dirname(__file__), 'music')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
fps = 120

clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_fly
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.centery = height / 2
        self.rect.right = width - 200
        self.speedy = 0 
        self.hp = 200 
        self.attack_frame = 0
        self.last_sword = pygame.time.get_ticks()
        self.sword_delay = 250
    
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            if second >= 3200:
                self.speedy = -18
            else:
                self.speedy = -10
        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]: 
            if second >= 3200:
                self.speedy = 18
            else:
                self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.bottom > height + 55:
            self.rect.bottom = height + 55
        if self.rect.top < -55: 
            self.rect.top = -55
        if keystate[pygame.K_a] or keystate[pygame.K_d] or keystate[pygame.K_RIGHT] or keystate[pygame.K_LEFT]:
            self.attack_frame += 1
            self.image = attack_ani[self.attack_frame]
            if self.attack_frame == 4:
                self.attack_frame = 0
            attack_sound.play()
        else:
            self.image = player_fly
            
 
    def attack(self):
        now = pygame.time.get_ticks()    
        if now - self.last_sword > self.sword_delay:
            self.last_sword = now
            sword = Sword(self.rect.right, self.rect.centery)
            all_sprites.add(sword)
            swords.add(sword)    


    def swipe(self):
        dis_attack = Distant_attack(self.rect.right, self.rect.centery)
        all_sprites.add(dis_attack)
        dis_attacks.add(dis_attack)
        

class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('attack.png')
        self.rect = self.image.get_rect()
        self.radius = 110
        self.rect.centery = y
        self.rect.right = x + 50
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.speed = 0
    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if not keystate[pygame.K_a] and (not keystate[pygame.K_LEFT]):
            self.kill()


class Distant_attack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('dis_attack.png')  
        self.rect = self.image.get_rect()
        self.radius = 80
        self.rect.centery = y 
        self.rect.right = x 
        self.speed = -40
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cat, (70, 70))
        self.rect = self.image.get_rect()
        self.radius = 24
        self.last_update = pygame.time.get_ticks()
        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = width      
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > width + 10 or self.rect.top < -25 or self.rect.right > width + 20:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(10, 20)
        if second >= 1570:
            self.kill()


class Mob_two(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cat_2
        self.rect = self.image.get_rect()
        self.radius = 45                                                       
        self.last_update = pygame.time.get_ticks()
        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = width      
        self.speedx = 25 

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > width + 10 or self.rect.top < -25 or self.rect.right > width + 20:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(20, 30)
        if second >= 3000:
            self.kill()


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect()
        self.radius = 300                                                  
        self.last_update = pygame.time.get_ticks()
        self.hp = 100
        self.rect.y = 0
        self.rect.x = - 300  
        self.speedx = 5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x == 10:
            self.speedx = 0
        if self.hp <= 0:
            self.kill()
        if second > 3300 and second < 3400:                                             
            self.image = boss_image_attack
        else:
            self.image = boss_image


class Attack_boss (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('boss_attack.png')
        self.rect = self.image.get_rect()
        self.radius = 35                                                    
        self.last_update = pygame.time.get_ticks()
        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = width      
        self.speedx = 30

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > width + 10 or self.rect.top < -25 or self.rect.right > width + 20:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(20, 30)
        if boss.hp <= 0:
            self.kill()
        
            


def draw_hp_bar_boss(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 1400
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def mob_attack():
    attack_boss = Attack_boss()
    all_sprites.add(attack_boss)
    boss_attack.add(attack_boss)

def new_mob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def new_mob2():
    m2 = Mob_two()
    all_sprites.add(m2)
    mobs_2.add(m2)
    
 
def draw_text(surf, text, size, x, y, color = BLACK):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_hp_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 1400
    BAR_HEIGHT = 10
    fill = (pct / 200) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def sound_fon(second):
    if second == 0:                                                     
        fon_music.play()
    
    if second == 1580:
        fon_music.stop()
        second_stage_music.play()

    if second == 3000:
        second_stage_music.stop()
        boss_music.play()


def game_over_screen():
    screen.blit(game_over_fon,(0,0))
    draw_text(screen, "[F] Заново", 18, width / 2, height * 3 / 4, RED)
    draw_text(screen, "[G] Меню", 18, width / 2, height * 3.2 / 4, RED)
    draw_text(screen, "[P] Выйти", 18, width / 2, height * 3.4 / 4, RED)
    pygame.display.flip()
    dai.play()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    waiting = False
                    dai.stop
                if event.key == pygame.K_g:
                    dai.stop
                    show_go_screen()
                    waiting = False
                if event.key == pygame.K_p:
                    waiting = False
                    pygame.quit()
                    
def show_go_screen():
    screen.blit(fon,(0,0))
    draw_text(screen, "Capturing cats", 64, width / 2, height / 4)
    draw_text(screen, "[F] Начать игру", 18, width / 2, height * 2 / 4)
    draw_text(screen, "[P] Выйти", 18, width / 2, height * 2.3 / 4)
    draw_text(screen, "W, S/ стрелки Вниз, Вверх - передвижение", 13, width / 2, height - 110)
    draw_text(screen, "A/ стрелка Влево - атака против обычных мобов", 13, width / 2, height -90)
    draw_text(screen, "D/ стрелка Вправо - дальняя атака против босса", 13, width / 2, height -70)
    draw_text(screen, "!!! Атаки босса нельзя заблокировать или уничтожить !!!", 13, width / 2, height -50)
    draw_text(screen, "!!! Дальняя атака не работает на обычных мобов !!!", 13, width / 2, height -30)
    pygame.display.flip()
    start.play()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                   start.stop()
                   waiting = False
                if event.key == pygame.K_p:
                    waiting = False
                    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    size = width, height = 1500, 600
    player_fly = load_image("player_fly.PNG")
    cat = load_image("cat.png")
    cat_2 = load_image('cat_2.png')
    boss_image = load_image('boss (1).png')
    boss_image_attack = load_image('boss (2).png')
    fon_boss = load_image('fon_boss.png')

    game_over_fon = load_image('game_over.png')
    fon = load_image("fon.png")
    fon1 = load_image('fon1.png')
    fon2 = load_image('fon2.png')
    fon3 = load_image('fon3.png')
    fon0 = load_image('fon0.png')
    fon6 = load_image('fon4.png')
    fon5 = load_image('fon5.png')
    fon4 = load_image('fon6.png')
    fon_end = load_image('end16.png')
    
    fon_music = pygame.mixer.Sound('music/fon.mp3')
    second_stage_music = pygame.mixer.Sound('music/boss_location.mp3')
    boss_music = pygame.mixer.Sound('music/boss.mp3')
    attack_sound = pygame.mixer.Sound('music/rezkiy-vzmah-ostryim-nojom.wav')
    hit_plyer_sound = pygame.mixer.Sound('music/hit.wav')
    mob_kill = pygame.mixer.Sound('music/cat-meow_mk76iuvu.mp3')
    start = pygame.mixer.Sound('music/kill.mp3')
    dai = pygame.mixer.Sound('music/Track 1.mp3')

    font_name = pygame.font.match_font('arial')

    score = 0   
    second = 0
    frame_score = 0
     
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("ฅ•ω•ฅ")


    all_sprites = pygame.sprite.Group()       
    mobs = pygame.sprite.Group()
    mobs_2 = pygame.sprite.Group()
    boss_attack = pygame.sprite.Group()
    swords = pygame.sprite.Group()
    dis_attacks = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)
   
  
    attack_ani = [load_image("player_fly.png"),
                  load_image("player_attack_1.png"), 
                  load_image("player_attack_2.png"),
                  load_image("player_attack_3.png"),
                  load_image("player_fly.png")]
 
    fon1_dx = 0
    fon2_dx = 0
    fon3_dx = 0

    fon4_dx = 0
    fon5_dx = 0
    fon51_dx = 0
    fon6_dx = 0
    fon_boss_dx = 0
    fon_end_dy = 0
    k = 0
    kx = 0
    kb = 0
    ke = 0

    game_over = False
    running = True
    menu = True
    while running:
        
        screen.fill(RED)
        pygame.draw.circle(screen, WHITE,(70, 70),50)
        if menu:
            show_go_screen()
            menu = False
            dis_attacks = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            mobs_2 = pygame.sprite.Group()
            boss_attack = pygame.sprite.Group()
            swords = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(6):
                new_mob()
            score = 0 
            second = 0

        if game_over:
            game_over_screen()
            game_over = False
            dis_attacks = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            mobs_2 = pygame.sprite.Group()
            boss_attack = pygame.sprite.Group()
            swords = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(6):
                new_mob()
            score = 0 
            second = 0
            fon4_dx = 0
            fon5_dx = 0
            fon51_dx = 0
            fon6_dx = 0
            fon_boss_dx = 0
            fon_end_dy = 0
            k = 0
            kx = 0
            kb = 0
            ke = 0
            fon = load_image("fon.png")
        clock.tick(fps)
        if second == 3200:
            boss = Boss()
            all_sprites.add(boss)

        if second == 3300:
            for i in range(6):
                mob_attack()
        if second == 1600:
            for i in range(6):
                new_mob2()

        sound_fon(second)

        screen.blit(fon, (0,0))
        screen.blit(fon1, (fon1_dx, 0))
        screen.blit(fon1, (fon1_dx - 1500, 0))
        fon1_dx += 2
        screen.blit(fon2, (fon2_dx ,0))
        screen.blit(fon2, (fon2_dx - 1500 ,0)) 
        fon2_dx += 5
        screen.blit(fon3, (fon3_dx ,0))
        screen.blit(fon3, (fon3_dx - 1500 ,0))
        fon3_dx += 8
        if fon1_dx == 1500:
            fon1_dx = 0
        if fon2_dx == 1500:
            fon2_dx = 0
        if fon3_dx == 1500:
            fon3_dx = 0

        second += 1
        print(second)

        if second == 1500:                                                    
            k = 15
            kx = 15
            ky = 15
        if second == 1600:
            fon = fon0

        screen.blit(fon4, (fon4_dx - 1500, 0))
        fon4_dx += kx
        screen.blit(fon5, (fon5_dx - 3000 ,0))
        fon5_dx += k
        screen.blit(fon5, (fon51_dx - 4500, 0)) 
        fon51_dx += k
        screen.blit(fon6, (fon6_dx - 6000 ,0))
        fon6_dx += k
        if fon6_dx == 6000:
            fon5_dx = 1500
        if fon51_dx == 4500:
            fon6_dx = 4500
        if fon5_dx == 1500:
            fon51_dx = 1500
        if fon4_dx == 3000:
            kx = 0  
            fon4_dx = 3000  

        if second == 3000:
            kb = 15
        screen.blit(fon_boss, (fon_boss_dx - 1500 ,0))
        screen.blit(fon_boss, (fon_boss_dx - 3000 ,0))
        fon_boss_dx += kb
        if fon_boss_dx == 3000:
            fon_boss_dx = 1500

        screen.blit(fon_end,(0, fon_end_dy - 600))
        fon_end_dy += ke
        if fon_end_dy >= 600:
            ke = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.attack()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.swipe()
         
        all_sprites.update()
        
        hits = pygame.sprite.groupcollide(mobs, swords, True, True, pygame.sprite.collide_circle) 
        for hit in hits:
            score += 100
            mob_kill.play()
            new_mob()

        hits = pygame.sprite.groupcollide(mobs_2, swords, True, True, pygame.sprite.collide_circle) 
        for hit in hits:
            score += 300
            mob_kill.play()
            new_mob2()
        
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)       
        for hit in hits:
            player.hp -= 1
            hit_plyer_sound.play()
            new_mob() 
            if player.hp <= 0:
                fon_music.stop()
                second_stage_music.stop()
                boss_music.stop()
                game_over = True 
        
        hits = pygame.sprite.spritecollide(player, mobs_2, False, pygame.sprite.collide_circle)       
        for hit in hits:
            player.hp -= 5
            hit_plyer_sound.play()
            new_mob2()
            if player.hp <= 0: 
                fon_music.stop()
                second_stage_music.stop()
                boss_music.stop()
                game_over = True 

        hits = pygame.sprite.spritecollide(player, boss_attack, True, pygame.sprite.collide_circle)       
        for hit in hits:
            player.hp -= 50
            hit_plyer_sound.play()
            if player.hp <= 0:
                fon_music.stop()
                second_stage_music.stop()
                boss_music.stop()
                game_over = True 
        
        hits = pygame.sprite.groupcollide(dis_attacks, boss_attack, True, False, pygame.sprite.collide_circle)

        if second > 3350:
            hits = pygame.sprite.spritecollide(boss, dis_attacks, True, pygame.sprite.collide_circle) 
            for hit in hits:
                boss.hp -= 2 
                if boss.hp <= 0:
                    score += 1000 
                    ke = 6

        all_sprites.draw(screen)
        draw_text(screen, str(score), 20, width // 2, 40)
        draw_hp_bar(screen, 50, 20, player.hp)
        if second > 3300:                                                            
            draw_hp_bar_boss(screen, 50, height - 20, boss.hp)
        
        
        pygame.display.flip()
    pygame.quit()
    