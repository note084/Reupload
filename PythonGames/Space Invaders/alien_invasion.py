import sys

import pygame
from pygame.sprite import Group
from alien import Alien
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from menu import Menu

import game_functions as gf

def run_game():
    #Initialize game and create a screen object.
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "PLAY GAME")

    #Make the high score button
    highscore_button = Button(ai_settings, screen, "HIGH SCORES")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    #Make a ship, group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    menu_Screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    menu = Menu(ai_settings, menu_Screen)


    alien = Alien(ai_settings, screen)

    #Start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, highscore_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, highscore_button, menu)

run_game()