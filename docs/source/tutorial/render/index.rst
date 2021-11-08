.. _render:

====================
Rendering structure
====================

After you have created a structure, you can export nice images for publications or presentations by rendering.

The :mod:`Render <batoms.render>` object controls various settings such as the viewpoint and the resolution of the generated image.


>>> from ase.build import molecule
>>> from batoms import Batoms
>>> atoms = molecule('CH4')
>>> ch4 = Batoms(label = 'ch4', atoms = atoms)
>>> ch4.render.run(direction = [1, 0, 0], 
...    engine = 'eevee', resolution_x = 1000, output = 'ch4.png')

Please refer to the following modules to see the details.


.. toctree::
   :maxdepth: 1
   
   engine
   camera
   light
