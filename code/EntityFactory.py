from .Background import Background
from .Const import WIN_WIDTH


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1':
                list_bg = []
                for i in range(9):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg

