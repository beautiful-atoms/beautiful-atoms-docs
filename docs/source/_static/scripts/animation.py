from ase.build import molecule
from batoms import Batoms
from batoms.utils.butils import removeAll

removeAll()
atoms = molecule("C2H6SO")
images = []
for i in range(20):
    temp = atoms.copy()
    temp.rotate(18*i, "z")
    images.append(temp)

c2h6so = Batoms(label="c2h6so", from_ase=images)
c2h6so.get_image(animation=True)
