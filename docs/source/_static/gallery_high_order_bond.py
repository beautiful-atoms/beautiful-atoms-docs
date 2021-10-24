from ase.build import molecule
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll
removeAll()
c6h6 = molecule('C6H6')
c6h6 = Batoms('c6h6', atoms = c6h6)
c6h6['H'].color = [0.8, 1.0, 0.0, 1.0]
c6h6['C'].color = [0.1, 0.4, 0.9, 1.0]

draw_plane(location = [0, 0, c6h6['C'][0][2] - c6h6['C'].size[0]], size = 400, color = (0.1, 0.1, 0.1, 1))
c6h6.render.light_type = 'POINT'
c6h6.render.lock_light_to_camera = False
c6h6.render.light_energy = 50000
c6h6.render.light_loc = [10, 0, 10]
c6h6.render.camera_loc = [10, 0, 20]
c6h6.render.run(engine = 'cycles', ortho_scale = 10, ratio = 0.8, output = 'figs/gallery_c6h6_ball.png')


# Bond
for i in range(6):
    c6h6.replace('C', 'C_%s'%i, [0])

c6h6.bondsetting['C_1-C_0'].order = 2
c6h6.bondsetting['C_3-C_2'].order = 2
c6h6.bondsetting['C_5-C_4'].order = 2
c6h6.model_type = 1
draw_plane(location = [0, 0, c6h6['C_0'][0][2] - c6h6['C_0'].size[0]], size = 400, color = (0.1, 0.1, 0.1, 1))
c6h6.render.light_type = 'POINT'
c6h6.render.lock_light_to_camera = False
c6h6.render.light_energy = 50000
c6h6.render.light_loc = [10, 0, 10]
c6h6.render.camera_loc = [10, 0, 20]
c6h6.render.run(engine = 'cycles', ortho_scale = 10, ratio = 0.8, output = 'figs/gallery_c6h6_bond.png')
