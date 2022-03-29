from ase.io import read
from batoms import Batoms
from batoms.draw import draw_plane
from batoms.utils.butils import removeAll, set_world
removeAll()
cto = read('datas/catio3.cif')
cto = Batoms('cto', from_ase = cto)
# ball
cto['Ca'].materials = {'Base Color': [0, 1, 0, 1.0], 'Metallic': 0.9, 'Specular': 1.0, 'Roughness': 0.01 }
cto['Ti'].materials = {'Base Color': [0.7, 0.8, 0, 1.0], 'Metallic': 0.2, 'Specular': 0.2, 'Roughness': 0.6 }
cto.bonds.setting[('Ti', 'O')].search = 0
cto.boundary = 0.01
cto.bonds.setting.remove(('Ca', 'O'))
cto.polyhedras.setting['Ti'].color = [0.7, 0.4, 0.0, 1.0]
set_world(color = [0.2, 0.2, 0.2, 1.0])
plane = draw_plane(location = [0, 0, -max(cto.size)], size = 200, color = (0.9, 0.9, 0.9, 1))
cto.render.viewport = [1, -0.3, 0.3]
cto.render.engine = 'cycles'
cto.render.lights['Default'].energy = 30
cto.render.lights['Default'].direction = [0.1, 0.5, 1]
cto.get_image(output = 'gallery_catio3_ball.png')

# bond
cto['O'].scale = 0.2
cto['Ti'].scale = 0.5
cto['Ca'].scale = 0.5
cto.boundary = 0.01
cto.bonds.setting[('Ti', 'O')].style = '0'
cto.bonds.setting[('Ti', 'O')].width = 0.005
cto.bonds.setting[('Ti', 'O')].color1 = [0.1, 0.1, 0.1, 1.0]
cto.model_style = 1
cto.bonds.show_search = True
plane.location = [0, 0, cto.get_all_vertices()[:, 2].min() - max(cto.size)]
cto.get_image(output = 'gallery_catio3_bond.png')

# polyhedra
cto.bonds.setting[('Ti', 'O')].search = 1
cto.bonds.setting[('Ti', 'O')].width = 0.01
cto.polyhedras.setting['Ti'].color = [0.5, 0.0, 0.7, 0.2]
cto.boundary = 0.01
cto.model_style = 2
plane.location = [0, 0, cto.get_all_vertices()[:, 2].min() -max(cto.size) ]
cto.get_image(output = 'gallery_catio3_polyhedra.png')


# polyhedra
cto.bonds.setting[('Ti', 'O')].search = 1
cto.bonds.setting[('Ti', 'O')].width = 0.01
cto.polyhedras.setting['Ti'].color = [0.2, 0.5, 0.7, 1.0]
cto.boundary = 0.01
cto.model_style = 2
plane.location = [0, 0, cto.get_all_vertices()[:, 2].min() - max(cto.size) ]
cto.get_image(output = 'gallery_catio3_polyhedra_2.png')

