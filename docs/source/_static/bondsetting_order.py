from ase.build import molecule
from batoms import Batoms
from batoms.utils.butils import removeAll
from math import pi
removeAll()

co2 = Batoms('co2', from_ase = molecule('CO2'))
co2.bonds.setting[('C', 'O')].width = 0.05
co2.bonds.setting[('C', 'O')].order = 2
co2.rotate(pi/2, 'Y')
co2.model_style = 1
co2.get_image(viewport = [0, 1, 0], output = 'figs/bondsetting_order.png')