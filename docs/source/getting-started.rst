**********************
Getting Started
**********************


Start Blender, and open a Python console, and run

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> atoms = molecule('H2O')
>>> h2o = Batoms(label = 'h2o', atoms = atoms)


.. image:: _static/figs/h2o-2.png
   :width: 20cm

Rendering the image

>>> h2o.render.run(direction = [1, 0 ,0], engine = 'eevee', output = 'h2o.png')

.. image:: _static/figs/h2o.png
   :width: 5cm


- Use Blender to run the python script in the background

Save the aboved code as a python file (eg. yourfile.py), and run in the command line::
   
   blender -b -P yourfile.py


- Use ``render`` function from ``batoms-api`` to run Blender without run Blender explicitly.

>>> from ase.build import molecule
>>> from batoms_api import render
>>> atoms = molecule('H2O')
>>> render_input = {'direction': [1, 0, 0], 'output': 'h2o.png',}
>>> render(atoms, render_input=render_input)

- Use ``batoms`` from command line::

   $ batoms 'h2o.xyz' -m '1'


