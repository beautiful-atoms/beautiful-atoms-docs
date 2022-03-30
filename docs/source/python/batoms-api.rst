=============
Batoms API
=============


- Use ``render`` function from ``batoms_api`` to run Blender without run Blender explicitly.

>>> from ase.build import molecule
>>> from batoms_api import render
>>> atoms = molecule("H2O")
>>> render_input = {"viewport": [1, 1, 0], "engine": "cycles", "output": "h2o.png",}
>>> render(atoms, render_input=render_input)


- Use ``batoms`` from command line::

   $ batoms "h2o.xyz" -m "1"
