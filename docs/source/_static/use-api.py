from ase.io import read
from batoms import render

atoms = read('datas/tio2.cif')
render_input = {'output': 'tio2',
  }
render(atoms,render_input = render_input)
