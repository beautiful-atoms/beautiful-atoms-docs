from batoms import Batoms
from ase import Atoms
from ase.build import molecule
from batoms.utils.butils import removeAll, set_world
removeAll()

h2o = molecule('H2O')
images = []
for i in range(20):
    atoms = Atoms()
    for j in [-1, 1]:
        for k in [-1, 1]:
            temp = h2o.copy()
            temp.translate([i/3*j, i*i/100*k, 0])
            atoms = atoms + temp
    images.append(atoms)

h2o = Batoms(label='h2o', from_ase=images)

h2o.render.use_motion_blur = True
h2o.render.camera.ortho_scale = 30
h2o.render.transparent = False
set_world([0.1, 0.1, 0.1, 1.0])
h2o.get_image(engine='eevee',
              frame=10,
              canvas=[30, 15, 10])

