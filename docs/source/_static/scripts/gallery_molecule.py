# Ball
from ase.build import molecule
from batoms import Batoms
from batoms.draw import draw_plane
from batoms.utils.butils import removeAll
removeAll()
h2o = molecule('H2O')
h2o = Batoms('h2o', from_ase = h2o)
h2o['H'].color = [0.8, 1.0, 0.0, 1.0]
# add a plane to show the shadow
plane = draw_plane(location = [0, 0, min(h2o.positions[:, 2]) - h2o.size[1]], 
            size = 200, color = (0.1, 0.1, 0.1, 1))
# direction of camera
h2o.render.viewport=[1, 0, 0.1]
h2o.render.engine = 'cycles'
h2o.render.lights['Default'].energy = 25
# direction of light
h2o.render.lights['Default'].direction = [0, 0.3, 1]
h2o.get_image(output = 'gallery_h2o_ball.png')

# Bond
h2o['O'].scale = 0.6
h2o['H'].scale = 0.6
h2o['H'].color = [0.8, 1.0, 0.0, 1.0]
h2o.bond.settings[('O', 'H')].width = 0.1
h2o.bond.settings[('O', 'H')].style = '0'
h2o.bond.settings[('O', 'H')].color1 = [0.1, 0.8, 0.8, 1.0]
h2o.model_style = 1
h2o.get_image(output = 'gallery_h2o_bond.png')
