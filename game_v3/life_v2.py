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
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centery = height / 2
        self.rect.right = width - 200
        self.speedy = 0 
        self.attacking = False
        self.attack_frame = 0
    

    def attack(self):
        sword = Sword(self.rect.right, self.rect.centery)
        all_sprites.add(sword)
        sword.add(sword)

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]: 
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom > height + 55:
            self.rect.bottom = height + 55
        if self.rect.top < -55: 
            self.rect.top = -55
        if keystate[pygame.K_SPACE]:
            self.image = attack_ani[self.attack_frame]
            if self.attack_frame == 9:
                self.attack_frame = 0
                self.attacking = False
            
            self.attack_frame += 1
            
        


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('attack.png')
        self.rect = self.image.get_rect()
        self.radius = 110
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius) 
        self.rect.centery = y
        self.rect.right = x + 50

    def update(self):
        keystate = pygame.key.get_pressed()
        if not keystate[pygame.K_SPACE]:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cat, (70, 70))
        self.rect = self.image.get_rect()
        self.radius = 24
        
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = width      
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        #hits = pygame.sprite.spritecollide(sword, mobs, False, pygame.sprite.collide_circle)       
        #if hits: 
            #self.kill()
        if self.rect.right > width + 10 or self.rect.top < -25 or self.rect.right > width + 20:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(10, 20)



def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

if __name__ == '__main__':
    size = width, height = 1500, 600
    fps = 60
    player_fly = load_image("player_fly.PNG")
    cat = load_image("cat.png")
    fon = load_image("fon.png")
    background = fon.get_rect()
    #game_over = load_image("game_over.png")
    #end = game_over.get_rect()
    fon1 = load_image('fon1.png')
    fon2 = load_image('fon2.png')
    fon3 = load_image('fon3.png')

    #fon_music = pygame.mixer.Sound(os.path.join('music', 'fon.mp3'))

    font_name = pygame.font.match_font('arial')
    score = 0

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("...")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    

    mobs = pygame.sprite.Group()
    sword = pygame.sprite.Group()
  
    attack_ani = [load_image("player_fly.png"),
                  load_image("player_fly.png"),
                  load_image("player_attack_1.png"),
                  load_image("player_attack_1.png"), 
                  load_image("player_attack_2.png"),
                  load_image("player_attack_2.png"),
                  load_image("player_attack_3.png"),
                  load_image("player_attack_3.png"),
                  load_image("player_fly.png"),
                  load_image("player_fly.png")]
    
    
    player = Player()

    all_sprites.add(player)
    for i in range(8):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    fon1_dx = 0
    fon2_dx = 0
    fon3_dx = 0
    #fon_music.play

    game_over = True
    running = True
    while running:
        screen.blit(fon, (0,0))
        screen.blit(fon1, (fon1_dx,0))
        screen.blit(fon1, (fon1_dx-1500,0))
        fon1_dx += 2
        screen.blit(fon2, (fon2_dx,0))
        screen.blit(fon2, (fon2_dx-1500,0)) 
        fon2_dx += 5
        screen.blit(fon3, (fon3_dx,0))
        screen.blit(fon3, (fon3_dx-1500,0))
        fon3_dx += 10
        if fon1_dx == 1500:
            fon1_dx = 0
        if fon2_dx == 1500:
            fon2_dx = 0
        if fon3_dx == 1500:
            fon3_dx = 0

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.attacking == False:
                        player.attack()
                        player.attacking = True                         
                if event.key == pygame.K_w:
                    player.speedx = -8
                if event.key == pygame.K_s:
                    player.speedx = 8
         
        all_sprites.update()
        '''
        hits = pygame.sprite.groupcollide(mobs, sword, True, True, pygame.sprite.collide_circle) 
        for hit in hits:
            score += 10
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            '''
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)       
        if hits: 
            running = False
        
        
        all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()
    