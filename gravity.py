import pygame
from pygame.time import Clock
from pygame.sprite import Group
from game_settings import Settings
from background import Background
from ship import Ship
from game_statistics import Stats
import game_functions as gf
from button import Button

def run_game():

    #Create some groups of objects
    game_objects = Group()
    buttons = Group()
    
    #Initialize game settings and statistics
    game_settings = Settings()
    game_stats = Stats()
    
    #Pygame initiation, and establish screen  
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, 
                                    game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_title)
    
    #Create background object
    background = Background(screen, game_settings)
    
    #Create ship object
    ship = Ship(screen, game_settings, game_stats, game_objects)
    game_objects.add(ship)
    
    #Create start button
    start_button = Button(screen, "Start game", action="start")
    start_button.rect.centerx = int(game_settings.screen_width/2)
    start_button.rect.centery = int(game_settings.screen_height/2)
    buttons.add(start_button)
    
    #Create clock object
    clock = Clock()

    #Update screen           
    gf.update_screen(background, buttons, game_objects)

    while True:
        #Check events key down or key up
        gf.check_events(ship, buttons)
    
        #Check collisions
        gf.check_collisions(game_stats, screen, ship, buttons)
        
        #Update screen           
        gf.update_screen(background,  buttons, game_objects)

        #Wait certain time to achieve 40fps 
        clock.tick(40)

run_game()
