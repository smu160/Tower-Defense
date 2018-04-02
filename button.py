import pygame
from spritesheet_functions import SpriteSheet

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, wd, ht):
		super().__init__()
		sprite_sheet = SpriteSheet("towers.png")
		self.image = sprite_sheet.get_image(116, 0, 100, 107, "cannon")
		self.image = pygame.transform.scale(self.image, (wd, ht))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.wd = wd
		self.ht = ht
		self.rect.x = x
		self.rect.y = y
		self.rect.width = self.wd 
		self.rect.height = self.ht 

	def update(self, shrink):
		if shrink == "shrink":
			self.rect.width = self.wd - 10
			self.rect.height = self.ht - 10
			self.rect.x = self.x + 5
			self.rect.y = self.y + 5
		else:
			self.rect.width = self.wd
			self.rect.height = self.ht
			self.rect.x = self.x
			self.rect.y = self.y

		
