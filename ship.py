import pygame
from pygame.sprite import Sprite
from stuff import Stuff
import random

class Ship(Sprite):
    """Class which describes ship"""

    def __init__(self, screen, game_settings, game_stats, game_objects):
        """Ship initiation and its initial position"""
        
        super().__init__()
        
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.game_stats = game_stats
        self.game_objects = game_objects
        self.image = pygame.image.load(self.game_settings.ship_image)
        self.rect = self.image.get_rect()
        self.current_weigth = self.game_settings.ship_weigth
        
        #Set ship initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #Variables which tells if ship is moveing
        self.vx = 0.0
        self.vy = 0.0
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Update ship position"""
        self.centerx += self.vx    
        self.centery += self.vy    
        
        #update rectanlge position
        self.rect.centerx = self.centerx    
        self.rect.centery = self.centery    
        
        #draw ship
        self.draw()
        
    def throwStuff(self, mouse_pos):
        if self.game_stats.game_started:
            v2x = self.game_settings.speedFactor * (mouse_pos[0] - self.centerx)
            v2y = self.game_settings.speedFactor * (mouse_pos[1] - self.centery)
            self.current_weigth -= self.game_settings.stuff_weigth
            v1x = -(self.game_settings.stuff_weigth/self.current_weigth) * v2x
            v1y = -(self.game_settings.stuff_weigth/self.current_weigth) * v2y
        
            v_x = self.vx + v2x
            v_y = self.vy + v2y
        
            self.vx += v1x
            self.vy += v1y
        
            stuff = Stuff(self.screen, self.game_settings, self.centerx, self.centery, v_x, v_y)
            self.game_objects.add(stuff)
