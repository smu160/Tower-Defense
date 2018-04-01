import pygame
from spritesheet_functions import SpriteSheet

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, wd, ht):
		super().__init__()
		sprite_sheet = SpriteSheet("test_tower.png")
		self.image = sprite_sheet.get_image(1, 1, 100, 100, "cannon")
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.wd = wd
		self.ht = ht
		self.rect.x = x
		self.rect.y = y
		self.rect.width = wd
		self.rect.height = ht


		#self.game_display = game_display
		#self.color = color
		#self.wd = wd
		#self.ht = ht
		#self.x = x
		#self.y = y
		#self.image = pygame.Surface([self.wd, self.ht])
		#self.image.fill(color)
		#self.rect = self.image.get_rect()
		#self.rect.x = x
		#self.rect.y = y
		#pygame.draw.rect(self.game_display, self.color, pygame.Rect(self.x, self.y, self.wd, self.ht))

	def update(self, shrink):
		if shrink == "shrink":
			#self.image = pygame.Surface([self.wd - 10, self.ht - 10])
			self.rect.width = self.wd - 10
			self.rect.height = self.ht - 10
			self.rect.x = self.x + 5
			self.rect.y = self.y + 5
			#pygame.draw.rect(self.game_display, self.color, pygame.Rect(self.x + 5, self.y + 5, self.wd - 10, self.ht - 10))
		else:
			#self.image = pygame.Surface([self.wd, self.ht])
			self.rect.width = self.wd
			self.rect.height = self.ht
			self.rect.x = self.x
			self.rect.y = self.y
			#pygame.draw.rect(self.game_display, self.color, pygame.Rect(self.x, self.y, self.wd, self.ht))
		#self.image.fill(self.color)

		# display button image

		
