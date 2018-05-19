import sys
import pygame
from button import Button

def keydown_events(event):
    """Keydown events actions"""
    if event.key == pygame.K_q:
        sys.exit()    


def mouse_event(ship, buttons):
    """Reaction on any mouse event.""" 
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0] == 1:
        ship.throwStuff(mouse_pos)
        for button in buttons:
            button.update_me(mouse_pos, True)
            if button.action == "start":
                button.kill()
                ship.game_stats.game_started = True
    else:
        for button in buttons:
            button.update_me(mouse_pos, False)
        

def check_events(ship, buttons):
    """Reaction on events thrown by keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            keydown_events(event)
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(ship, buttons)
        
        elif event.type == pygame.MOUSEMOTION:
            mouse_event(ship, buttons)
        
def check_collisions(game_stats, screen, ship, buttons):
    if game_stats.game_started == True and game_stats.game_over == False:
        if (ship.rect.left <= 0 or 
            ship.rect.top <= 0 or 
            ship.rect.right >= ship.screen_rect.right or 
            ship.rect.bottom >= ship.screen_rect.bottom):
        
            game_stats.game_over = True
            game_stats.game_started = False
            
            #Create game over button
            end_button = Button(screen, "Game over", action="gameOver")
            end_button.rect.centerx = ship.screen_rect.centerx
            end_button.rect.centery = ship.screen_rect.centery
            buttons.add(end_button)
        
    
def update_screen(background,  buttons, game_objects):
    """Update images on screen then flip screen"""
    
    #Update background
    background.update()
    
    #Update objects
    game_objects.update()
    
    #Update buttons
    buttons.update()
    
    #Swith last modified screen
    pygame.display.flip()  
