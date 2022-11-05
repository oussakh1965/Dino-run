'''imports'''
import pygame
from gamefiles.modules.MVP import *
from gamefiles.modules.theme_files import *
from gamefiles.modules.game import *
###############################################################


def game_over_screen(score):
    '''creates a game_over screen that tells the score

    Parameters :
    -----------------
    player_score: int, player score 

    Returns :
    -----------------
    False makes it so that the main menu stops calling the gameover screen when there is none.
    main_running : bool, closes main menue when game over screen is closed

    '''
    screen = pygame.display.set_mode((1200, 600), RESIZABLE)
    window_running = True
    main_running = True
    while window_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                main_running = False
                window_running = False
            if event.type == KEYDOWN:
                window_running = False
        screen.fill((255, 255, 255))
        text, rect = GAME_FONT.render(
            "GAMEOVER !", (0, 0, 0))
        screen.blit(text, (480, 180))
        text2, rect2 = GAME_FONT.render(
            "Your score is : {}  !".format(score), (0, 0, 0))
        screen.blit(text2, (350, 280))
        text3, rect3 = GAME_FONT.render(
            "Press any key to return to the main menu.", (0, 0, 0))
        screen.blit(text3, (100, 420))
        pygame.display.flip()
    return False, main_running


def animation_menu():
    pygame.init()
    animation, sound = load_animation()
    i = 0
    sound.play()
    screen = pygame.display.set_mode((1200, 600))
    window_running = True
    while window_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                window_running = False
        screen.fill((255, 255, 255))
        screen.blit(animation[i], (350, 50))
        pygame.display.update()
        i += 1
        if i == 44:
            window_running = False
        clock.tick(10)


########################main script####################################
# main menu loop
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600), RESIZABLE)
GAME_FONT = pygame.freetype.Font(os.path.join(
    parpath, "PressStart2P-Regular.ttf"), 24)
text_mvp = GAME_FONT.render_to(screen, (80, 420),
                               "MVP", (0, 0, 0))
text_classic1 = GAME_FONT.render_to(screen, (260, 420),
                                    "Classic 1", (0, 0, 0))
text_classic2 = GAME_FONT.render_to(screen, (590, 420),
                                    "Classic 2", (0, 0, 0))
text_xmas = GAME_FONT.render_to(screen, (910, 420),
                                "Christmas", (0, 0, 0))
main_running = True
gameover = False
player_score = 0
code = [False, False, False]
code1 = ''
while main_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            main_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Use event.pos or pg.mouse.get_pos().
                if text_mvp.collidepoint(event.pos):
                    gameover, player_score, main_running = play_game_mvp(5)
                if text_classic1.collidepoint(event.pos):
                    gameover, player_score, main_running = play_game_theme(
                        5, 'Classic')
                if text_classic2.collidepoint(event.pos):
                    gameover, player_score, main_running = play_game_theme(
                        5, 'Classic clean')
                if text_xmas.collidepoint(event.pos):
                    gameover, player_score, main_running = play_game_theme(
                        5, 'xmas')
        if event.type == KEYUP:
            n = len(code1)
            if n > 10:
                code1 = code1[n-3: n]
            code1 += event.unicode
    if 'sus' in code1:
        code1 = ''
        animation_menu()
    if gameover:
        gameover, main_running = game_over_screen(player_score)
    screen.fill((255, 255, 255))
    text, rect = GAME_FONT.render(
        "Welcome to DINO RUN !", (0, 0, 0))
    screen.blit(text, (340, 150))
    text2, rect2 = GAME_FONT.render(
        "Choose a mode to play :", (0, 0, 0))
    screen.blit(text2, (300, 320))
    GAME_FONT.render_to(screen, (80, 420),
                        "MVP", (0, 0, 0))
    GAME_FONT.render_to(screen, (260, 420),
                        "Classic 1", (0, 0, 0))
    GAME_FONT.render_to(screen, (590, 420),
                        "Classic 2", (0, 0, 0))
    GAME_FONT.render_to(screen, (910, 420),
                        "Christmas", (0, 0, 0))
    pygame.display.flip()

pygame.quit()
