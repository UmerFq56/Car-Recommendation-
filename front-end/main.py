"""
Car Recommendation and Visualization Tool

Module Description ================== This module serves as the entry point to a car recommendation and visualization
application. It utilizes the Pygame library to create an interactive graphical user interface (GUI), allowing users
to explore car data and receive recommendations based on their preferences. The main components include a slider for
input, display of car statistics, and visualization of recommendation results.

The module integrates with several other modules to manage data handling and recommendation logic:
- `assets.py`: Manages loading and processing of graphical assets and car data.
- `tree.py`: Implements data structures and algorithms for organizing and querying car data.
- `project_graphs.py`: Contains graph-based logic for generating car recommendations.

Key functionalities include event handling for user input, rendering of UI elements, and displaying the results of
the recommendation algorithm.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2024 CSC111 Students Winter (Yaseen Sadat, Muhammad Aneeq, Umer Farooqui, Zarif Ali)
"""

from assets import *
from tree import *
from project_graphs import *

pygame.init()

display_info = pygame.display.Info()
window_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Project 2")

direct_selections = ['x', 'x', 'x', 'x', 'x']
undirect_selections = ['0', '0', '0', '0']

# Engine
eng_items = ['V4', 'V6', 'V8', 'V10', 'V12', 'Electric']
eng_top_txt = "None Selected"
eng_opt_active = False
eng_item_box_rect = pygame.Rect(50, 320, 250, 40)
eng_item_rects = [pygame.Rect(70, 360 + i * 40, 200, 40) for i in range(len(eng_items))]

# Horse Power
hp_items = ['0-449', '450-620', '620+']
hp_top_txt = "None Selected"
hp_opt_active = False
hp_item_box_rect = pygame.Rect(350, 320, 250, 40)
hp_item_rects = [pygame.Rect(370, 360 + i * 40, 200, 40) for i in range(len(hp_items))]

# Price
pr_items = ['$0-$49,999', '$50,000-$99,999', '$100,000-$199,999', '$200,000+']
pr_top_txt = "None Selected"
pr_opt_active = False
pr_item_box_rect = pygame.Rect(650, 320, 250, 40)
pr_item_rects = [pygame.Rect(670, 360 + i * 40, 200, 40) for i in range(len(pr_items))]

# Torque
tq_items = ['0-499', '500-750', '750+']
tq_top_txt = "None Selected"
tq_opt_active = False
tq_item_box_rect = pygame.Rect(950, 320, 250, 40)
tq_item_rects = [pygame.Rect(970, 360 + i * 40, 200, 40) for i in range(len(hp_items))]

# Car Type
ct_items = ['Sedan', 'SUV', 'Sports', 'Luxury']
ct_top_txt = "None Selected"
ct_opt_active = False
ct_item_box_rect = pygame.Rect(1250, 320, 250, 40)
ct_item_rects = [pygame.Rect(1270, 360 + i * 40, 200, 40) for i in range(len(ct_items))]


def drop_down_menu_ct() -> None:
    """
    Function to draw the fifth dropdown menu.
    """
    pygame.draw.rect(screen, D_GRAY, ct_item_box_rect)
    pygame.draw.rect(screen, BLACK, ct_item_box_rect, 4)
    text_surf_5 = s_font_2.render(ct_top_txt, True, WHITE)
    centered_x_5 = ct_item_box_rect.x + (ct_item_box_rect.width - text_surf_5.get_width()) // 2
    centered_y_5 = ct_item_box_rect.y + (ct_item_box_rect.height - text_surf_5.get_height()) // 2
    screen.blit(text_surf_5, (centered_x_5, centered_y_5))

    if ct_opt_active:
        for i, item in enumerate(ct_items):
            item_rect = ct_item_rects[i]
            pygame.draw.rect(screen, D_GRAY, item_rect)
            pygame.draw.rect(screen, BLACK, item_rect, 4)
            item_text_surf = s_font_2.render(item, True, WHITE)
            centered_x = item_rect.x + (item_rect.width - item_text_surf.get_width()) // 2
            centered_y = item_rect.y + (item_rect.height - item_text_surf.get_height()) // 2
            screen.blit(item_text_surf, (centered_x, centered_y))


def drop_down_menu_tq() -> None:
    """
    Function to draw the fourth dropdown menu.
    """
    pygame.draw.rect(screen, D_GRAY, tq_item_box_rect)
    pygame.draw.rect(screen, BLACK, tq_item_box_rect, 4)
    text_surf_4 = s_font_2.render(tq_top_txt, True, WHITE)
    centered_x_4 = tq_item_box_rect.x + (tq_item_box_rect.width - text_surf_4.get_width()) // 2
    centered_y_4 = tq_item_box_rect.y + (tq_item_box_rect.height - text_surf_4.get_height()) // 2
    screen.blit(text_surf_4, (centered_x_4, centered_y_4))

    if tq_opt_active:
        for i, item in enumerate(tq_items):
            item_rect = tq_item_rects[i]
            pygame.draw.rect(screen, D_GRAY, item_rect)
            pygame.draw.rect(screen, BLACK, item_rect, 4)
            item_text_surf = s_font_2.render(item, True, WHITE)
            centered_x = item_rect.x + (item_rect.width - item_text_surf.get_width()) // 2
            centered_y = item_rect.y + (item_rect.height - item_text_surf.get_height()) // 2
            screen.blit(item_text_surf, (centered_x, centered_y))


def drop_down_menu_pr() -> None:
    """
    Function to draw the third dropdown menu.
    """
    pygame.draw.rect(screen, D_GRAY, pr_item_box_rect)
    pygame.draw.rect(screen, BLACK, pr_item_box_rect, 4)
    text_surf_3 = s_font_2.render(pr_top_txt, True, WHITE)
    centered_x_3 = pr_item_box_rect.x + (pr_item_box_rect.width - text_surf_3.get_width()) // 2
    centered_y_3 = pr_item_box_rect.y + (pr_item_box_rect.height - text_surf_3.get_height()) // 2
    screen.blit(text_surf_3, (centered_x_3, centered_y_3))

    if pr_opt_active:
        for i, item in enumerate(pr_items):
            item_rect = pr_item_rects[i]
            pygame.draw.rect(screen, D_GRAY, item_rect)
            pygame.draw.rect(screen, BLACK, item_rect, 4)
            item_text_surf = s_font_2.render(item, True, WHITE)
            centered_x = item_rect.x + (item_rect.width - item_text_surf.get_width()) // 2
            centered_y = item_rect.y + (item_rect.height - item_text_surf.get_height()) // 2
            screen.blit(item_text_surf, (centered_x, centered_y))


def drop_down_menu_hp() -> None:
    """
    Function to draw the second dropdown menu.
    """
    pygame.draw.rect(screen, D_GRAY, hp_item_box_rect)
    pygame.draw.rect(screen, BLACK, hp_item_box_rect, 4)
    text_surf_2 = s_font_2.render(hp_top_txt, True, WHITE)
    centered_x_2 = hp_item_box_rect.x + (hp_item_box_rect.width - text_surf_2.get_width()) // 2
    centered_y_2 = hp_item_box_rect.y + (hp_item_box_rect.height - text_surf_2.get_height()) // 2
    screen.blit(text_surf_2, (centered_x_2, centered_y_2))

    if hp_opt_active:
        for i, item in enumerate(hp_items):
            item_rect = hp_item_rects[i]
            pygame.draw.rect(screen, D_GRAY, item_rect)
            pygame.draw.rect(screen, BLACK, item_rect, 4)
            item_text_surf = s_font_2.render(item, True, WHITE)
            centered_x = item_rect.x + (item_rect.width - item_text_surf.get_width()) // 2
            centered_y = item_rect.y + (item_rect.height - item_text_surf.get_height()) // 2
            screen.blit(item_text_surf, (centered_x, centered_y))


def dropdown_menu_eng() -> None:
    """
     Function to draw the engineering dropdown menu
    """
    pygame.draw.rect(screen, D_GRAY, eng_item_box_rect)
    pygame.draw.rect(screen, BLACK, eng_item_box_rect, 4)
    text_surf = s_font_2.render(eng_top_txt, True, WHITE)
    centered_x = eng_item_box_rect.x + (eng_item_box_rect.width - text_surf.get_width()) // 2
    centered_y = eng_item_box_rect.y + (eng_item_box_rect.height - text_surf.get_height()) // 2
    screen.blit(text_surf, (centered_x, centered_y))

    if eng_opt_active:
        for i, item in enumerate(eng_items):
            item_rect = eng_item_rects[i]
            pygame.draw.rect(screen, D_GRAY, item_rect)
            pygame.draw.rect(screen, BLACK, item_rect, 4)
            item_text_surf = s_font_2.render(item, True, WHITE)
            centered_x = item_rect.x + (item_rect.width - item_text_surf.get_width()) // 2
            centered_y = item_rect.y + (item_rect.height - item_text_surf.get_height()) // 2
            screen.blit(item_text_surf, (centered_x, centered_y))


class Slider:
    """
    A slider UI component for Pygame applications, allowing users to select a value within a specified range.

    The slider is drawn on a Pygame surface and consists of a horizontal line with a movable thumb indicating the
    current value. Users can drag the thumb left or right to adjust the value. This class also supports drawing
    additional fixed position indicators on the screen.

    Instance Attributes:
        - rect (pygame.Rect): The rectangle defining the slider's line position and size.
        - min_value (float|int): The minimum value the slider can represent.
        - max_value (float|int): The maximum value the slider can represent.
        - value (float|int): The current value of the slider, initially set to `min_value`.
        - thumb_rect (pygame.Rect): The rectangle defining the slider's thumb position and size.
        - dragging (bool): A flag indicating whether the thumb is currently being dragged.

    Representation Invariants:
        - self.min_value < self.max_value
        - self.min_value <= self.value <= self.max_value
        - self.rect.width > 0 and self.rect.height > 0
        - self.thumb_rect.width > 0 and self.thumb_rect.height > 0

    """
    rect: pygame.Rect
    min_value: Union[int, float]
    max_value: Union[int, float]
    value: Union[int, float]
    thumb_rect: pygame.Rect
    dragging: bool

    def __init__(self, x: int, y: int, w: int, h: int, min_value: Union[int, float],
                 max_value: Union[int, float]) -> None:
        self.rect = pygame.Rect(x, y, w, h)
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.thumb_rect = pygame.Rect(x, y - h // 2, h, h)
        self.dragging = False

    def draw(self, screens: pygame.Surface) -> None:
        """
        Draws the slider and fixed position indicators on the specified Pygame surface.
        """
        pygame.draw.line(screens, GRAY, self.rect.topleft, self.rect.topright, 5)
        pygame.draw.circle(screens, D_PURPLE, self.thumb_rect.center, self.thumb_rect.width // 2)
        pygame.draw.rect(screens, BLACK, (5, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (315, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (395, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (705, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (790, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (1100, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (1185, 690, 10, 25))
        pygame.draw.rect(screens, BLACK, (1495, 690, 10, 25))

    def handle_event(self, event: pygame.event.Event, undirect_select: list[Any], index: int) -> None:
        """
        Handles Pygame events related to the slider, such as mouse clicks and dragging.

        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.thumb_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.thumb_rect.centerx = max(min(event.pos[0], self.rect.right), self.rect.left)
            self.value = self.min_value + (self.max_value - self.min_value) * (
                    (self.thumb_rect.centerx - self.rect.left) / self.rect.width)
            undirect_select[index] = str(int(self.value))

    def get_value(self):
        """
         Returns the current value of the slider
        """
        return self.value

    def draw_value(self, screens: pygame.Surface, font: Any) -> None:
        """
        Draws the current value of the slider near the thumb for easy viewing.
        """
        value_surf = font.render(str(int(self.value)), True, GRAY)
        value_rect = value_surf.get_rect(center=(self.thumb_rect.centerx, self.thumb_rect.top - 20))
        screens.blit(value_surf, value_rect)


reliability_slider = Slider(15, 700, 300, 20, 0, 100)
rating_slider = Slider(405, 700, 300, 20, 0, 100)
zero_sixty_slider = Slider(800, 700, 300, 20, 0, 100)
max_speed_slider = Slider(1195, 700, 300, 20, 0, 100)


def start_screen() -> None:
    """
    Runs the main event loop for the start screen of a car dealership application.

    This function creates and manages the start screen interface, allowing users to interact with various UI elements
    to specify their car search preferences. It uses Pygame for rendering the interface, which includes drop-down
    menus for selecting engine type, horsepower range, price range, torque range, and car type, as well as sliders
    for adjusting reliability, rating, 0-60 times, and max speed preferences.
    """

    global eng_top_txt, eng_opt_active, direct_selections, undirect_selections
    global hp_top_txt, hp_opt_active
    global pr_top_txt, pr_opt_active
    global tq_top_txt, tq_opt_active
    global ct_top_txt, ct_opt_active
    search_button_rect = pygame.Rect(650, 800, 200, 50)

    error_message_displayed = False
    redo_message_displayed = False
    running = True

    while running:
        for event in pygame.event.get():
            rating_slider.handle_event(event, undirect_selections, 0)
            reliability_slider.handle_event(event, undirect_selections, 1)
            zero_sixty_slider.handle_event(event, undirect_selections, 2)
            max_speed_slider.handle_event(event, undirect_selections, 3)

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if search_button_rect.collidepoint(event.pos):
                    if all(selection != 'x' for selection in direct_selections):
                        all_fitting_cars = car_guesser('car_data_set.csv', direct_selections)
                        all_cars = car_dict('car_data_set.csv')
                        ranked_list = car_ranker(undirect_selections, all_fitting_cars, all_cars)
                        if ranked_list is None:
                            redo_message_displayed = True
                        else:
                            search_screen(all_cars, ranked_list)
                            running = False
                    else:
                        error_message_displayed = True
                elif eng_item_box_rect.collidepoint(event.pos):
                    eng_opt_active = not eng_opt_active
                    hp_opt_active = False
                    pr_opt_active = False
                    tq_opt_active = False
                    ct_opt_active = False
                elif eng_opt_active:
                    for rect, item in zip(eng_item_rects, eng_items):
                        if rect.collidepoint(event.pos):
                            eng_top_txt = item
                            eng_opt_active = False
                            direct_selections[0] = item
                            break
                elif hp_item_box_rect.collidepoint(event.pos):
                    hp_opt_active = not hp_opt_active
                    eng_opt_active = False
                    pr_opt_active = False
                    tq_opt_active = False
                    ct_opt_active = False
                elif hp_opt_active:
                    for rect, item in zip(hp_item_rects, hp_items):
                        if rect.collidepoint(event.pos):
                            hp_top_txt = item
                            hp_opt_active = False
                            direct_selections[1] = item
                            break
                elif pr_item_box_rect.collidepoint(event.pos):
                    pr_opt_active = not pr_opt_active
                    eng_opt_active = False
                    hp_opt_active = False
                    tq_opt_active = False
                    ct_opt_active = False
                elif pr_opt_active:
                    for rect, item in zip(pr_item_rects, pr_items):
                        if rect.collidepoint(event.pos):
                            pr_top_txt = item
                            pr_opt_active = False
                            direct_selections[2] = item
                            break
                elif tq_item_box_rect.collidepoint(event.pos):
                    tq_opt_active = not tq_opt_active
                    eng_opt_active = False
                    pr_opt_active = False
                    hp_opt_active = False
                    ct_opt_active = False
                elif tq_opt_active:
                    for rect, item in zip(tq_item_rects, tq_items):
                        if rect.collidepoint(event.pos):
                            tq_top_txt = item
                            tq_opt_active = False
                            direct_selections[3] = item
                            break
                elif ct_item_box_rect.collidepoint(event.pos):
                    ct_opt_active = not ct_opt_active
                    eng_opt_active = False
                    pr_opt_active = False
                    hp_opt_active = False
                    tq_opt_active = False
                elif ct_opt_active:
                    for rect, item in zip(ct_item_rects, ct_items):
                        if rect.collidepoint(event.pos):
                            ct_top_txt = item
                            ct_opt_active = False
                            direct_selections[4] = item
                            break
                    else:
                        eng_opt_active = False
                        hp_opt_active = False
                        pr_opt_active = False
                        tq_opt_active = False
                        ct_opt_active = False
            if error_message_displayed:
                select_all_text = s_font_1.render('Invalid! Make sure you selected all keys', True, GRAY)
                screen.blit(select_all_text, (625, 770))
                pygame.display.update()
                pygame.time.wait(1000)
                error_message_displayed = False
            if redo_message_displayed:
                select_all_text = s_font_1.render('Sorry nothing matching the criteria, try again.', True, GRAY)
                screen.blit(select_all_text, (625, 770))
                pygame.display.update()
                pygame.time.wait(1000)
                redo_message_displayed = False

        screen.fill(PURPLE)
        pygame.draw.rect(screen, D_PURPLE, (0, 0, window_size[0], 200))
        pygame.draw.rect(screen, BLACK, (0, 200, window_size[0], 10))

        deluxe_text = pygame.transform.rotate(t_font_1.render('DELUXE', True, GRAY), 90)
        auto_text = t_font_1.render('AUTO', True, GRAY)
        sales_text = t_font_2.render('SALES', True, GRAY)
        screen.blit(deluxe_text, (20, 25))
        screen.blit(auto_text, (55, 30))
        screen.blit(sales_text, (55, 65))

        screen.blit(location_emblem, (1185, 30))
        screen.blit(phone_emblem, (1190, 100))
        screen.blit(clock_emblem, (1190, 160))
        location_text = s_font_1.render('321 Bloor St W, Toronto, 0N, M1CL5G  ', True, GRAY)
        phone_text = s_font_1.render('Sales: (416) 784-3312', True, GRAY)
        hours_text = s_font_1.render('Open Today from 9:00 AM - 7:00 PM ', True, GRAY)
        screen.blit(location_text, (1240, 45))
        screen.blit(phone_text, (1240, 107))
        screen.blit(hours_text, (1240, 167))

        engine_text = s_font_2.render('Select an Engine Type', True, GRAY)
        screen.blit(engine_text, (65, 250))
        dropdown_menu_eng()
        hp_text = s_font_2.render('Select a Horsepower Range', True, GRAY)
        screen.blit(hp_text, (350, 250))
        drop_down_menu_hp()
        pr_text = s_font_2.render('Select a Price Range', True, GRAY)
        screen.blit(pr_text, (670, 250))
        drop_down_menu_pr()
        tq_text = s_font_2.render('Select a Torque Range', True, GRAY)
        screen.blit(tq_text, (965, 250))
        drop_down_menu_tq()
        ct_text = s_font_2.render('Select a Car Type', True, GRAY)
        screen.blit(ct_text, (1280, 250))
        drop_down_menu_ct()
        rl_text = s_font_1.render('How much do you care about reliability?', True, GRAY)
        screen.blit(rl_text, (20, 620))
        reliability_slider.draw(screen)
        reliability_slider.draw_value(screen, s_font_2)
        rt_text = s_font_1.render('How much do you care about rating?', True, GRAY)
        screen.blit(rt_text, (420, 620))
        rating_slider.draw(screen)
        rating_slider.draw_value(screen, s_font_2)
        zs_text = s_font_1.render('How much do you care about the 0-60?', True, GRAY)
        screen.blit(zs_text, (810, 620))
        zero_sixty_slider.draw(screen)
        zero_sixty_slider.draw_value(screen, s_font_2)
        mx_text = s_font_1.render('How much do you care about max speed?', True, GRAY)
        screen.blit(mx_text, (1200, 620))
        max_speed_slider.draw(screen)
        max_speed_slider.draw_value(screen, s_font_2)

        search_button_text = 'Search'
        pygame.draw.rect(screen, (34, 139, 34), search_button_rect, 0, 15)
        text_surf = s_font_2.render(search_button_text, True, WHITE)
        text_rect = text_surf.get_rect(center=search_button_rect.center)
        screen.blit(text_surf, text_rect)

        pygame.display.update()


def search_screen(all_cars: dict[str, Any], ranked_list: list[tuple[str, Any]]) -> None:
    """
    Displays the search results screen after a car search has been made.

    This function takes the user to a new screen where the top recommended car based on their preferences is
    highlighted, along with its key details and an image. Additionally, it displays a list of similar cars with their
    images, prices, and similarity scores to the top recommendation. Users can interact with a 'Back' button to
    return to the start screen and adjust their preferences or make a new search.

    The screen layout includes detailed information about the best fitting car, such as engine type, horsepower,
    torque, price, and more. Similar cars are displayed on the right side of the screen with basic information and
    similarity scores to help users compare their options.
    """
    search_running = True
    back_button_rect = pygame.Rect(50, 850, 100, 50)

    while search_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                search_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    start_screen()
                    search_running = False

        screen.fill(PURPLE)
        pygame.draw.rect(screen, D_PURPLE, (0, 0, window_size[0], 200))
        pygame.draw.rect(screen, BLACK, (0, 200, window_size[0], 10))
        pygame.draw.rect(screen, BLACK, (500, 620, window_size[0] - 500, 10))
        pygame.draw.rect(screen, BLACK, (500, 200, 10, window_size[1] - 200))
        pygame.draw.rect(screen, BLACK, (920, 200, 10, 420))
        pygame.draw.rect(screen, GRAY, back_button_rect)
        back_text = s_font_2.render('Back', True, BLACK)

        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)

        auto_text = t_font_2.render('Here Are Our Options For You!', True, GRAY)
        screen.blit(auto_text, (100, 40))

        text_1 = s_font_4.render('The Best Fitting Car', True, GRAY)
        screen.blit(text_1, (50, 300))

        car = ranked_list[0][0]
        graph = load_complete_graph('car_data_set.csv')
        reccom_cars = graph.recommend_cars(car)
        car_image = pygame.transform.scale(pygame.image.load(ranked_list[0][1][1]), (350, 300))
        car_image_1 = pygame.transform.scale(pygame.image.load(os.path.join(all_cars[reccom_cars[0][0]][4] + '.jpg')),
                                             (300, 250))
        car_image_2 = pygame.transform.scale(pygame.image.load(os.path.join(all_cars[reccom_cars[1][0]][4] + '.jpg')),
                                             (200, 150))
        car_image_3 = pygame.transform.scale(pygame.image.load(os.path.join(all_cars[reccom_cars[2][0]][4] + '.jpg')),
                                             (200, 150))
        car_image_4 = pygame.transform.scale(pygame.image.load(os.path.join(all_cars[reccom_cars[3][0]][4] + '.jpg')),
                                             (200, 150))
        car_image_5 = pygame.transform.scale(pygame.image.load(os.path.join(all_cars[reccom_cars[4][0]][4] + '.jpg')),
                                             (200, 150))

        screen.blit(car_image, (50, 360))
        screen.blit(car_image_1, (1050, 270))
        screen.blit(car_image_2, (530, 700))
        screen.blit(car_image_3, (770, 700))
        screen.blit(car_image_4, (1010, 700))
        screen.blit(car_image_5, (1250, 700))
        stat_text = s_font_5.render('Stats:', True, GRAY)
        name_text = s_font_4.render(f'{car}', True, GRAY)
        eng_surf = s_font_2.render(f"Engine: {all_cars[car][5]}", True, GRAY)
        hp_surf = s_font_2.render(f"Horse Power: {all_cars[car][6]}", True, GRAY)
        tq_surf = s_font_2.render(f"Torque: {all_cars[car][8]}", True, GRAY)
        pr_surf = s_font_4.render(f"Price: ${all_cars[car][7]}", True, GRAY)
        ct_surf = s_font_2.render(f"Car Type: {all_cars[car][9]}", True, GRAY)
        zts_surf = s_font_2.render(f"Zero to Sixity (mph): {all_cars[car][2]} seconds", True, GRAY)
        ms_surf = s_font_2.render(f"Max Speed: {all_cars[car][3]} mph", True, GRAY)
        rt_surf = s_font_2.render(f"Certified Rating Score: {all_cars[car][0]} / 10", True, GRAY)
        rl_surf = s_font_2.render(f"Certified Reliability Score: {all_cars[car][1]} / 5", True, GRAY)
        score_surf = s_font_2.render(f"Our Calculated Performance Score: {ranked_list[0][1][2]} ", True, (0, 255, 0))
        sim_text = s_font_5.render('Our Most Similar Car', True, GRAY)
        sim1_text = s_font_6.render('Other Similar Cars', True, GRAY)

        name1_text = s_font_2.render(f'{reccom_cars[0][0]}', True, GRAY)
        pr1_text = s_font_2.render(f'Price: $ {all_cars[reccom_cars[0][0]][7]}', True, GRAY)
        sm1_text = s_font_2.render(f'Similarity Score: {reccom_cars[0][1]}', True, GRAY)

        name2_text = s_font_2.render(f'{reccom_cars[1][0]}', True, GRAY)
        pr2_text = s_font_2.render(f'Price: $ {all_cars[reccom_cars[1][0]][7]}', True, GRAY)
        sm2_text = s_font_2.render(f'Similarity Score: {reccom_cars[1][1]}', True, GRAY)
        name3_text = s_font_2.render(f'{reccom_cars[2][0]}', True, GRAY)
        pr3_text = s_font_2.render(f'Price: $ {all_cars[reccom_cars[2][0]][7]}', True, GRAY)
        sm3_text = s_font_2.render(f'Similarity Score: {reccom_cars[2][1]}', True, GRAY)
        name4_text = s_font_2.render(f'{reccom_cars[3][0]}', True, GRAY)
        pr4_text = s_font_2.render(f'Price: $ {all_cars[reccom_cars[3][0]][7]}', True, GRAY)
        sm4_text = s_font_2.render(f'Similarity Score: {reccom_cars[3][1]}', True, GRAY)
        name5_text = s_font_2.render(f'{reccom_cars[4][0]}', True, GRAY)
        pr5_text = s_font_2.render(f'Price: $ {all_cars[reccom_cars[4][0]][7]}', True, GRAY)
        sm5_text = s_font_2.render(f'Similarity Score: {reccom_cars[4][1]}', True, GRAY)

        screen.blit(name_text, (70, 700))
        screen.blit(pr_surf, (70, 760))

        screen.blit(stat_text, (550, 220))
        screen.blit(sim_text, (1050, 220))
        screen.blit(sim1_text, (520, 650))

        screen.blit(eng_surf, (550, 260))
        screen.blit(ct_surf, (550, 300))
        screen.blit(hp_surf, (550, 340))
        screen.blit(tq_surf, (550, 380))
        screen.blit(zts_surf, (550, 420))
        screen.blit(ms_surf, (550, 460))
        screen.blit(rt_surf, (550, 500))
        screen.blit(rl_surf, (550, 540))
        screen.blit(score_surf, (550, 580))

        screen.blit(name1_text, (1050, 530))
        screen.blit(pr1_text, (1050, 560))
        screen.blit(sm1_text, (1050, 590))

        screen.blit(name2_text, (530, 860))
        screen.blit(pr2_text, (530, 890))
        screen.blit(sm2_text, (530, 920))
        screen.blit(name3_text, (770, 860))
        screen.blit(pr3_text, (770, 890))
        screen.blit(sm3_text, (770, 920))
        screen.blit(name4_text, (1010, 860))
        screen.blit(pr4_text, (1010, 890))
        screen.blit(sm4_text, (1010, 920))
        screen.blit(name5_text, (1250, 860))
        screen.blit(pr5_text, (1250, 890))
        screen.blit(sm5_text, (1250, 920))

        pygame.display.update()


def main() -> None:
    """
    start a new screen
    """
    start_screen()


if __name__ == "__main__":
    main()
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E1136'],
        'extra-imports': ['assets', 'tree_file', 'project_graphs'],
        'allowed-io': ['search_screen', 'start_screen', 'handle_event'],
        'max-nested-blocks': 4
    })
