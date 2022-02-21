from ase.io import read
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll, set_world
removeAll()
atoms = read('datas/mof-5.cif')
mof = Batoms(label = 'mof-5', atoms = atoms)
mof['H'].color = [0.6, 0, 1.0, 1.0]
mof['C'].color = [0.0, 0.6, 0.1, 1.0]
mof.polyhedras.setting['Zn'].color = [0.1, 0.4, 0.7, 1.0]
mof.model_style = 2
mof.draw_cavity_sphere(9.0, boundary = [[0.2, 0.8], [0.2, 0.8], [0.2, 0.8]])
mof.draw_cell()
set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, 0], size = 200, color = (0.9, 0.9, 0.9, 1))
mof.render.viewport = [1, -0.3, 0.3]
mof.render.engine = 'cycles'
mof.render.lights['Default'].energy = 30
mof.render.lights['Default'].direction = [0.1, 0.5, 1]
mof.get_image(output = 'figs/gallery_cavity.png')

