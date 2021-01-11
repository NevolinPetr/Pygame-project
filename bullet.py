class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, image, enemy, pos, speed, damage):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.enemy = enemy
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
        self.damage = damage

    def update(self):
        self.rect.y += self.speed
        if (pygame.sprite.collide_mask(self, hero) and self.enemy or
                pygame.sprite.spritecollideany(self, enemies) and not self.enemy):
            self.kill()
