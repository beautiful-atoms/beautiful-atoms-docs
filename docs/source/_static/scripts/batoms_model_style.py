from ase.io import read
from batoms.utils.butils import removeAll
from batoms import Batoms

removeAll()
atoms = read("datas/tio2.cif")
tio2 = Batoms(label="tio2", from_ase=atoms, color_style="0")
tio2.boundary = 0.01
tio2.render.resolution = [500, 500]
tio2.render.engine = "workbench"
for model_style in [0, 1, 2, 3]:
    tio2.model_style = model_style
    tio2.crystal_view = True
    tio2.get_image([0, 0, 1], padding=3,
                   output="batoms_model_style_%s.png" % model_style)
