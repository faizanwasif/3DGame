from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

game = Ursina()


grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assests/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/assets_punch_sound.wav', loop=False, autoplay=False)

block_pick    = 1
window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    for i in range(1,5):
        if held_keys[str(i)]:
            block_pick = i


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture): # setting button
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0, random.uniform(0.9, 1)),
            scale = 0.5
        )

    def input(self, key):
        # creating & destroying box or voxel
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(position= self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position= self.position + mouse.normal, texture=brick_texture)
                if block_pick == 3:
                    voxel = Voxel(position= self.position + mouse.normal, texture=stone_texture)
                if block_pick == 4:
                    voxel = Voxel(position= self.position + mouse.normal, texture=dirt_texture)
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, #viewport
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.1,-0.3)
        )

    def active(self):
        self.position = Vec2(0,-0.2)
    def passive(self):
        self.position = Vec2(0.1,-0.3)
# Creating multiple buttons

for z in range(40):#Number of tiles
    for x in range(40):
        voxel = Voxel(position=(x, 0 , z))

# Creating Entity
player = FirstPersonController()
sky = Sky()
hand = Hand()

game.run()

"""Creating first person Charater is super easy in ursina as it has some classes we can make use of"""
