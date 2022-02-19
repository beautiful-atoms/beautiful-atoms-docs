**********************
Getting Started
**********************


Start Blender, and open a Python console, and run

.. code:: python
   
   from batoms import Batoms
   h2o = Batoms('h2o',
               species = ['O', 'H', 'H'], 
               positions= [[0, 0, 0], [0, -0.76, -0.6], [0, 0.76, -0.6]])

.. image:: _static/figs/getting_started_h2o.png
   :width: 20cm

Rendering the image

.. code:: python

   h2o.get_image(viewport = [1, 0 ,0], engine = 'eevee', output = 'h2o.png')

.. image:: _static/figs/getting_started_h2o_2.png
   :width: 5cm


- Use Blender to run the python script in the background

Save the aboved code as a python file (eg. yourfile.py), and run in the command line::
   
   blender -b -P yourfile.py

- Use ``render`` function from ``batoms_api`` to run Blender without run Blender explicitly.

>>> from ase.build import molecule
>>> from batoms_api import render
>>> atoms = molecule('H2O')
>>> render_input = {'viewport': [1, 1, 0], 'engine': 'cycles', 'output': 'h2o.png',}
>>> render(atoms, render_input=render_input)

- Use ``batoms`` from command line::

   $ batoms 'h2o.xyz' -m '1'
