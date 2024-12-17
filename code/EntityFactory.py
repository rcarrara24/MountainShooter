import random

from .Background import Background
from .Const import WIN_WIDTH, WIN_HEIGHT
from .Enemy import Enemy
from .Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'level2bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 60))
            case 'Player2':
                return Player('Player2', (150, WIN_HEIGHT / 2 + 60))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
