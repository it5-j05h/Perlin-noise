from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

class Chunkrender(Entity):
    def __init__(self, position=(0,0,0),child=Entity()):
        super().__init__(
            position=position,
            child = child

            #scripts = self.add_script((crender(target=self.position))),
        )


    def update(self):
        rendrange = 100
        global pposx
        global pposz
        rlimitxP = pposx + rendrange
        rlimitxN = pposx - rendrange
        rlimitzP = pposz + rendrange
        rlimitzN = pposz - rendrange
        chunkx = self.position[0]
        chunkz = self.position[2]
        if chunkx < rlimitxP and chunkx > rlimitxN and chunkz < rlimitzP and chunkz > rlimitzN:
            self.child.enable()
            #self.visible = False



def gen_god():
    god = random.randint(1000, 9999)
    random.seed(god)
    print(god)

def spawn_shroom(x,y,chunknode):
    Entity(model="assets/plumpshrooms", texture='assets/shroom_color2', position=(x * 10, -.6, y * 10), parent=chunknode)
    Entity(model="assets/plumpshrooms", texture='assets/shroom_color2', position=((x * 10)-3, -.6, y * 10), parent=chunknode)
    Entity(model="assets/plumpshrooms", texture='assets/shroom_color2', position=((x * 10)-3, -.6, (y * 10)-3), parent=chunknode)

def spawn_oak(x,y,chunknode):
    Entity(model="assets/lowpolytree", texture='assets/normtreetex', position=(x * 5, 0, y * 5), parent=chunknode)
def spawn_pine(x,y,chunknode):
    Entity(model="assets/lowpolypine", texture='assets/backed', position=(x*5, 0, y*5), parent=chunknode)

def gen_chunk(chunkx,chunkz):
    chunknode = Entity(position=(chunkx, 0, chunkz),enabled=False)
    rendnode = Chunkrender(position=(chunkx, 0, chunkz),child=chunknode)
    chunk = Entity(model='cube', color=color.green, scale=(100, 1, 100), collider='cube', position=(chunkx, -1, chunkz), parent=chunknode)
    mapsize = 2
    for x in range(mapsize):
        for y in range(mapsize):
            chance = random.randint(0,9)
            if chance == 5:
                spawn_oak(x, y, chunknode)
            elif chance == 4:
                spawn_pine(x, y, chunknode)
            elif chance == 1 or 0:
                spawn_shroom(x, y, chunknode)










def gen_world():
    worldlimit = 10
    for cx in range(-worldlimit,worldlimit+1):
        for cy in range(-worldlimit,worldlimit+1):
            gen_chunk(cx*50,cy*50)

def update():
    global pposx
    global pposz
    pposx = player.getX()
    pposz = player.getZ()




if __name__ == '__main__' :
    Sky(texture='sky_sunset')
    player = FirstPersonController()
    player.setPos(0, -1, 0)
    gen_god()
    gen_world()
    update()
    app.run()