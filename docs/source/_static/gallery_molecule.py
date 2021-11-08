# Ball
from ase.build import molecule
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll
removeAll()
h2o = molecule('H2O')
h2o = Batoms('h2o', atoms = h2o)
h2o['H'].color = [0.8, 1.0, 0.0, 1.0]
plane = draw_plane(location = [0, 0, h2o['H'][0][2] - h2o['H'].size[0]], 
            size = 200, color = (0.1, 0.1, 0.1, 1))
h2o.render.lights['Default'].energy = 25
h2o.render.lights['Default'].direction = [0, 0.3, 1]
h2o.render.run([1, 0, 0.1], engine = 'cycles', output = 'gallery_h2o_ball.png')

# Bond
h2o['O'].scale = 0.6
h2o['H'].scale = 0.6
h2o['H'].color = [0.8, 1.0, 0.0, 1.0]
h2o.bondsetting[('O', 'H')].width = 0.1
h2o.bondsetting[('O', 'H')].style = 0
h2o.bondsetting[('O', 'H')].color1 = [0.1, 0.8, 0.8, 1.0]
h2o.draw_bonds()
h2o.render.run([1, 0, 0.1], engine = 'cycles', output = 'gallery_h2o_bond.png')
