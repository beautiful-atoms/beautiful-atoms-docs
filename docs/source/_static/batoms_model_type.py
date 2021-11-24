from ase.io import read
from batoms.butils import removeAll
from batoms import Batoms

removeAll()
atoms = read('datas/tio2.cif')
tio2 = Batoms(label = 'tio2', atoms = atoms, color_style='VESTA')
tio2.boundary = 0.01
tio2.draw_cell()
tio2.render.resolution = [500, 500]
tio2.render.engine = 'eevee'
for model_type in [0, 1, 2, 3]:
    tio2.model_type = model_type
    tio2.get_image([0, 0, 1], output = 'batoms_model_type_%s.png'%model_type)
