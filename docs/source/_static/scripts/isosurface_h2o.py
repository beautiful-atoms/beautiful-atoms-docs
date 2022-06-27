from ase.io.cube import read_cube_data
from batoms import Batoms
from batoms.utils.butils import removeAll
removeAll()

volume, atoms = read_cube_data("datas/h2o-homo.cube")
h2o = Batoms("h2o", from_ase=atoms, volume=volume)
h2o.isosurface.settings[1] = {"level": 0.002, "color": [1, 1, 0, 0.5]}
h2o.isosurface.settings[2] = {"level": -0.002, "color": [0, 0, 0.8, 0.5]}
h2o.isosurface.draw()
