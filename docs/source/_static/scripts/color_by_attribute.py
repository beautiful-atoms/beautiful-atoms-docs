from ase.build import bulk
from batoms import Batoms
import numpy as np
au = bulk("Au", cubic=True)*[10, 10, 1]
com = au.get_center_of_mass()
au = Batoms(label = "au", from_ase = au)
# calculate some values based on the positions, normalized it to [0, 1]
values = (au.positions[:, 0]-com)**2 + (au.positions[:, 1]-com)**2
# set a new attribute called "color"
au.set_attributes({"color": (values-np.min(values))/(np.max(values)-np.min(values)) })
# color atoms by the attribute "color"
au.species.color_by_attribute("color")
au.get_image(viewport = [0, 0, 1], output = "color_by_attribute.png")