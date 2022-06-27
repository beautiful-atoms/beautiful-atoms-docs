from ase.build import molecule
from batoms import Batoms
ch3choh = molecule('CH3CH2OH')
ch3choh = Batoms('ch3ch2oh', from_ase = ch3choh)
ch3choh.bond.settings[('H', 'O')].min = 2.0
ch3choh.bond.settings[('H', 'O')].max = 3.0
ch3choh.bond.settings[('H', 'O')].width = 0.01
ch3choh.bond.settings[('H', 'O')].style = '1'
ch3choh.model_style = 1

