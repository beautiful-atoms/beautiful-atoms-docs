from ase.io.cube import read_cube_data
from batoms import Batoms
volume, atoms = read_cube_data('docs/source/_static/datas/h2o-homo.cube')
h2o = Batoms('h2o', from_ase = atoms, volume = volume, draw = False)
h2o.isosurfacesetting[1] = {'level': 0.002, 'color': [1, 1, 0, 0.5]}
h2o.isosurfacesetting[2] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}
h2o.draw_isosurface()
