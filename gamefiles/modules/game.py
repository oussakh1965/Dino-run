'''importing modules'''
import random
import pygame
try:
    from gamefiles.modules.MVP import *
    from gamefiles.modules.theme_files import *
except:
    if __name__ == '__main__':
        from mvp import *
        from theme_files import *
from pygame.locals import *
# from pygame.constants import K_DOWN, K_SPACE, K_UP, KEYDOWN, KEYUP
from pygame import display
import pygame.freetype
##################################################################


def play_game_theme(vel_x, theme):
    '''generates a window where the game is rendered 

    Parameters:
    ---------------
    vel_x : int, acts as staring difficulty , DISCLAIMER : DO NOT USE A FLOAT HERE, IT MAKES THE GAME BUG
    theme : str, indiquates which theme to use

    Returns:
    ---------------
    a bool that idiquates that the game is over (main function uses this to generate gameover screen)
    score_player : int, the score
    main_running : bool, indiquates is the game is closed so it closes the main menue too
    '''
    pygame.init()
    font = pygame.freetype.SysFont('Consolas', 30)
    gamedisplay = pygame.display.set_mode((1200, 600), RESIZABLE)
    screen = pygame.Surface((600, 250))
    clock = pygame.time.Clock()
    assets = load_assets(PLAYER_HEIGHT, theme)
    obstacle_assets = load_obstacles(obstacletypes, PLAYER_HEIGHT, theme)
    step = 100
    skyx = 0
    trackx = 0
    bgx = 0
    snow_list = []
    running_timer = [0, 0]
    obstacle_timer = [0, 0]
    score_player = 0
    clouds = []
    obstacles = []
    cloud_top = 90
    cloud_timer = 0
    game_state = default_state.copy()
    game_state['player_pos'] = [[80, 235], [0, 0]]
    snow_state = 0
    dark_text = True
    darken = [False, 0]
    transition = 255
    while not game_state['crashed']:
        game_state, obstacles, main_running = check_events(
            game_state, obstacles, SPAWNOBSTACLE)
        if score_player > 1000:
            if theme in ['Classic', 'Classic clean']:
                screen.fill('black')
            darken[0] = True
            dark_text = False
        elif score_player > 600:
            snow_state = 2
            if theme in ['Classic', 'Classic clean']:
                screen.fill('black')
        elif score_player > 300:
            if theme in ['Classic', 'Classic clean']:
                screen.fill((transition, transition, transition))
                if transition > 0:
                    transition -= 5
                dark_text = False
            snow_state = 1
        else:
            screen.fill('white')
        if theme == 'xmas':
            skyx = process_sky(assets['sky'], skyx,
                               screen, game_state['game_not_started'])
            bgx = process_background(assets['bg'], bgx, screen,
                                     game_state['game_not_started'])
        else:
            if not game_state['game_not_started']:
                if cloud_timer == cloud_top:
                    clouds.append(create_cloud())
                    cloud_timer = 0
                    cloud_top = random.randint(240, 600)
                else:
                    cloud_timer += 1
            clouds = process_clouds(clouds, screen)
        old_score = score_player
        vel_x, step = difficulty(vel_x, score_player, old_score, step)
        trackx = track_scroll(assets['track'], trackx, vel_x,
                              screen, game_state['game_not_started'])
        game_state, obstacles = create_frame(
            game_state, obstacles, vel_x, screen, theme)
        obstacle_timer = display_obstacles(
            obstacles, obstacle_assets, screen, obstacle_timer)
        running_timer = display_dino(
            game_state['player'], running_timer, game_state, screen, assets)
        if theme == 'xmas':
            snow_list = process_snow(
                snow_list, screen, game_state['game_not_started'], snow_state)
        if darken[0]:
            '''darkens the screen at a cenrtain time and produces a glow that circles the player'''
            coordinate_x, coordinate_y = game_state['player_pos'][0]
            filter_screen = pygame.Surface((600, 250))
            filter_screen.fill((darken[1], darken[1], darken[1]))
            for i in range(20):
                glow = pygame.Surface((600, 250))
                pygame.draw.circle(glow, (3, 3, 2), (coordinate_x+18, coordinate_y-20),
                                   150-3*i)
                filter_screen.blit(glow, (0, 0), special_flags=BLEND_SUB)

            screen.blit(filter_screen, (0, 0), special_flags=BLEND_SUB)
            if darken[1] < 220:
                darken[1] += 2
                # pygame.draw.rect(glow, 'white', pygame.Rect(0, 250, 600, 50))
        score_player = score(game_state, font, screen, dark_text)
        width, height = pygame.display.get_surface().get_size()
        h_1 = width*.416
        surf = pygame.transform.scale(screen, (width, h_1))
        gamedisplay.blit(surf, (0, (height-h_1)/2))
        display.update()
        clock.tick(60)
    if main_running:
        return True, score_player, main_running
    return False, score_player, main_running


#################################################
# runs the game if this script is run
if __name__ == "__main__":
    gameover, player_score, main_running = play_game_theme(5, 'xmas')
    pygame.quit()
    print('game over, your score is : {} '.format(player_score))
