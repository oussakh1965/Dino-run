from gamefiles.modules.MVP import *
import pygame


def test_create_obstacle():
    obstacletypes = [['big1', .48, .95], ['big2', .99, .95], ['big3', 1.02, .95],
                     ['small1', .4, .71], ['small2', .68, .71], [
                         'small3', 1.05, .71],
                     ['bird1', .97, .68, 233], [
        'bird2', .97, .68, 233-40*.63],
        ['bird3', .97, .68, 160]]

    names = ["big1", "big2", "big3", "small1", "small2", "small3", "bird"]
    rects = [pygame.Rect(600, 235-obstacle[2]*40, obstacle[1]
                         * 40, obstacle[2]*40) for obstacle in obstacletypes[:6]]
    rects += [pygame.Rect(600, obstacle[3]-obstacle[2]*40, obstacle[1]
                          * 40, obstacle[2]*40) for obstacle in obstacletypes[6:]]
    name, rect = create_obstacle()
    assert name in names
    assert rect in rects


def test_detplayer():
    game_state_1 = {'jumping': False, 'pos': 'down',
                    'player_pos': [[80, 235], [0, 0]]}
    game_state_2 = {'jumping': True, 'pos': 'normal',
                    'player_pos': [[80, 235], [0, 0]]}
    game_state_3 = {'jumping': False, 'pos': 'normal',
                    'player_pos': [[80, 235], [0, 0]]}
    player_1 = pygame.Rect(80, 235-40*.63, 40*1.25, 40*.63)
    player_2 = pygame.Rect(80, 235-40, 40*.93, 40)
    player_3 = pygame.Rect(80, 235-40, 40*.93, 40)
    assert detplayer(game_state_1) == player_1
    assert detplayer(game_state_2) == player_2
    assert detplayer(game_state_3) == player_3
