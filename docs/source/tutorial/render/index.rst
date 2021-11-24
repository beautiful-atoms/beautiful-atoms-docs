.. _render:

====================
Rendering structure
====================

After you have created a structure, you can export nice images for publications or presentations by rendering.

The :mod:`Render <batoms.render>` object controls various settings such as the viewport and the resolution of the generated image.

In order to render a :class:`Batoms` object, you need to attach a :class:`Render`  object to your :class:`Batoms` object. Then we asked for the image.

.. code:: python

   from ase.build import molecule
   from batoms import Batoms
   atoms = molecule('CH4')
   ch4 = Batoms(label = 'ch4', atoms = atoms)
   ch4.render.viewport = [1, 0, 0]
   ch4.render.engine = 'eevee'
   ch4.render.resolution = [1000, 1000]
   ch4.get_image(output = 'ch4.png')


Parameters



Please refer to the following modules to see the details.


.. toctree::
   :maxdepth: 1
   
   engine
   camera
   light
