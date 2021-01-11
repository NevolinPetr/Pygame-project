class Enemy(pygame.sprite.Sprite):
    image_boom = load_image('boom.png')
    boom_time = False
    shot_time = 0

    def __init__(self, group, image, pos, health, damage, rate_of_fire):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.health = health
        self.damage = damage
        self.rate_of_fire = rate_of_fire

    def update(self):
        if self.health <= 0:
            self.image = self.image_boom
            self.boom_time = pygame.time.get_ticks()
        if self.boom_time and pygame.time.get_ticks() - self.boom_time >= 1000:
            self.kill()
        collision_list = pygame.sprite.spritecollide(self, bullets, False)
        if collision_list:
            for elem in collision_list:
                if not elem.enemy:
                    self.health -= elem.damage
        if pygame.time.get_ticks() - self.shot_time > self.rate_of_fire * 1000:
            Bullet(bullets, image='bullet1.jpg', enemy=True,
                   pos=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height),
                   speed=1, damage=1)
            self.shot_time = pygame.time.get_ticks()
