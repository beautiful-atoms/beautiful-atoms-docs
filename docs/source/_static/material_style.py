from batoms.butils import removeAll
from ase.build import molecule
from batoms import Batoms
atoms = molecule('H2O')
for material_style in ['glass', 'mirror', 'emmision']:
    removeAll()
    h2o = Batoms('h2o', atoms=atoms, material_style=material_style)
    h2o.render.run(direction = [0, 0, 1], 
                    engine = 'cycles', 
                    light_energy = 20,
                    output = 'figs/materials_style_%s.png'%material_style)
