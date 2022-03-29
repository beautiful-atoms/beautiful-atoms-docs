from ase.build import molecule
from batoms import Batoms
from batoms.draw import draw_plane
from batoms.utils.butils import removeAll
removeAll()
c6h6 = molecule('C6H6')
c6h6 = Batoms('c6h6', from_ase=c6h6)
c6h6['H'].color = [0.8, 1.0, 0.0, 1.0]
c6h6['C'].color = [0.1, 0.4, 0.9, 1.0]
plane = draw_plane(location=[0, 0, c6h6.get_all_vertices()[:, 2].min() - c6h6.size[0]],
                   size=400, color=(0.4, 0.4, 0.4, 1))
c6h6.render.viewport = [0.5, 0, 1]
c6h6.render.engine = 'cycles'
c6h6.render.resolution = [500, 500]
c6h6.render.lights['Default'].energy = 40
c6h6.render.lights['Default'].direction = [0.3, 0.3, 1]
c6h6.get_image(output='gallery_c6h6_ball.png')
# Bond
c6h6.model_style = 1
c6h6.bonds.bond_order_auto_set()
plane.location = [0, 0, c6h6.get_all_vertices()[:, 2].min() - c6h6.size[0]]
c6h6.get_image(output='gallery_c6h6_bond.png')