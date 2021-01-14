class Hero(pygame.sprite.Sprite):
    image_boom = load_image('boom.png')
    boom_time = False

    def __init__(self, group, image, pos, health, damage, image_bullet):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.health = health
        self.damage = damage
        self.image_bullet = image_bullet
        self.rect_bullet = self.image.get_rect()

    def update(self, *args):
        vx = 0
        vy = 0
        if self.health <= 0:
            self.image = self.image_boom
            self.boom_time = pygame.time.get_ticks()
        if self.boom_time and pygame.time.get_ticks() - self.boom_time >= 1000:
            self.kill()
        collision_list = pygame.sprite.spritecollide(self, bullets, False)
        if collision_list:
            for elem in collision_list:
                if elem.enemy:
                    self.health -= elem.damage
        if args and args[0].type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                vy = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                vy = 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                vx = 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                vx = -1
            if event.key == pygame.K_RETURN:
                Bullet(bullets, image='bullet1.jpg', enemy=False,
                       pos=(self.rect.x + (self.rect.width - self.rect_bullet.width) // 2,
                            self.rect.y - self.rect_bullet.height), speed=1, damage=1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            Bullet(bullets, image='bullet1.jpg', enemy=False,
                   pos=(self.rect.x + (self.rect.width - self.rect_bullet.width) // 2,
                        self.rect.y - self.rect_bullet.height), speed=1, damage=1)
        self.rect = self.rect.move(vx, vy)

