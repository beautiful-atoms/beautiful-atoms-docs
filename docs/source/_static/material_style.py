from batoms.utils.butils import removeAll
from ase.build import molecule
from batoms import Batoms
atoms = molecule('H2O')
for material_style in ['glass', 'mirror', 'emmision']:
    removeAll()
    h2o = Batoms('h2o', from_ase = atoms, material_style = material_style)
    h2o.render.engine = 'cycles'
    h2o.render.lights['Default'].energy = 20
    h2o.get_image(viewport = [0, 0, 1], 
                    output = 'figs/materials_style_%s.png'%material_style)
