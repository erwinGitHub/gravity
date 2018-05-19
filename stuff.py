import pygame
from pygame.sprite import Sprite
import random

class Stuff(Sprite):
    """Class which describes one stuff"""
    
    def __init__(self, screen, game_settings, x, y, vx, vy):
        """init object settings"""
        super().__init__()
        
        self.screen = screen
        self.game_settings = game_settings
        self.screen_rect = self.screen.get_rect()
        
        #load stuff image
        self.image = pygame.image.load(self.game_settings.stuff_images[
                            random.randint(0,len(self.game_settings.stuff_images)-1)])
        self.rect = self.image.get_rect()
        
        #Set initial position for stuff
        self.rect.x = x
        self.rect.y = y
        
        #Save precission position of stuff
        self.centerx = x
        self.centery = y
        
        self.vx = vx
        self.vy = vy
        
    def check_edges(self):
        """Method which checks if stuff reached any border."""
        if self.rect.right <= 0 or self.rect.bottom <= 0 or self.rect.left >= self.screen_rect.right or self.rect.top >= self.screen_rect.bottom:
            return False
        else:
            return True
        
        
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update stuff position on screen, then draw it
        If stuff reached screen border them kill this sprite""" 
        
        self.centerx += self.vx
        self.centery += self.vy
        self.rect.centerx = self.centerx      
        self.rect.centery = self.centery      
        
        if self.check_edges():
            self.draw()
        else:
            self.kill()
