"""
Asset Management for Car Recommendation Tool

Module Description ================== This module is responsible for managing the graphical assets and fonts used in
the car recommendation and visualization tool. It initializes the Pygame library and sets up essential components for
the user interface, including color constants, image assets, and fonts of various sizes for text rendering.

The assets managed in this module are utilized across the application to create a visually appealing and consistent
user interface. This includes the loading and scaling of images used as icons and emblems within the application,
and the definition of fonts for text elements in different sections of the GUI.

Key Components:
- Color constants for the UI theme.
- Loading and scaling of image assets for icons and emblems.
- Initialization and setup of fonts for different text elements.

The module makes extensive use of the Pygame library for managing these graphical assets, which are essential for the
visual aspects of the car recommendation tool.
Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2024 CSC111 Students Winter (Yaseen Sadat, Muhammad Aneeq, Umer Farooqui, Zarif Ali)

"""

import pygame

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_GRAY = (171, 170, 184, 255)
GRAY = (236, 236, 236, 255)
D_PURPLE = (45, 44, 84, 255)
PURPLE = (71, 71, 135, 255)

location_emblem = pygame.transform.scale(pygame.image.load('graphics/location_emblem.png'), (45, 40))
phone_emblem = pygame.transform.scale(pygame.image.load('graphics/phone_img.png'), (35, 25))
clock_emblem = pygame.transform.scale(pygame.image.load('graphics/clock_img.png'), (35, 25))


t_font_1 = pygame.font.Font('graphics/newyork.ttf', 35)
t_font_2 = pygame.font.Font('graphics/newyork.ttf', 100)
s_font_1 = pygame.font.Font('graphics/london.otf', 20)
s_font_2 = pygame.font.Font('graphics/london.otf', 25)
s_font_3 = pygame.font.Font('graphics/london.otf', 40)
s_font_4 = pygame.font.Font('graphics/london.otf', 45)
s_font_5 = pygame.font.Font('graphics/london.otf', 35)
s_font_6 = pygame.font.Font('graphics/london.otf', 30)
