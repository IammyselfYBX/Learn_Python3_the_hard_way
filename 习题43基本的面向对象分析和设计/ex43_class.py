"""
本代码是p144的代码
根据是上p143~p144的类的结构,我们编写代码实现类的模型
"""
class Scene (object):

    def enter(self):
        pass

class English(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# 这几行代码就是看可不可以运行
a_map = Map('central_corridor')
a_game = English(a_map)
a_game.play()
