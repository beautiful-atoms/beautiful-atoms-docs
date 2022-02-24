from ase.build import molecule
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll
removeAll()
c6h6 = molecule('C6H6')
c6h6 = Batoms('c6h6', from_ase = c6h6)
c6h6['H'].color = [0.8, 1.0, 0.0, 1.0]
c6h6['C'].color = [0.1, 0.4, 0.9, 1.0]
plane = draw_plane(location = [0, 0, c6h6.get_all_vertices()[:, 2].min() - c6h6['C'].size[0]], 
            size = 400, color = (0.4, 0.4, 0.4, 1))
c6h6.render.viewport = [0.5, 0, 1]
c6h6.render.engine = 'cycles'
c6h6.render.lights['Default'].energy = 40
c6h6.render.lights['Default'].direction = [0.3, 0.3, 1]
c6h6.get_image(output = 'figs/gallery_c6h6_ball.png')
# Bond
for i in range(6):
    c6h6.replace('C', 'C_%s'%i, [0])

c6h6.bonds.setting[('C_1', 'C_0')] = {'order': 2, 'style': '0'}
c6h6.bonds.setting[('C_3', 'C_2')] = {'order': 2, 'style': '0'}
c6h6.bonds.setting[('C_5', 'C_4')] = {'order': 2, 'style': '0'}
c6h6.model_style = 1
plane.location = [0, 0, c6h6.get_all_vertices()[:, 2].min() - c6h6['C_0'].size[0]]
c6h6.get_image(output = 'figs/gallery_c6h6_bond.png')
