================================
Volumetric data and isosurface
================================

The :mod:`Isosurfacesetting <batoms.isosurfacesetting>` object is used to store and set all parameters related with volumetric data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``level``, ``color``. 

Isosurface
---------------------

Here we show a example of draw isosurfaces from cube file.

>>> from ase.io.cube import read_cube_data
>>> from batoms import Batoms
>>> volume, atoms = read_cube_data('docs/source/_static/datas/h2o-homo.cube')
>>> h2o = Batoms('h2o', atoms = atoms, volume = volume, draw = False)


You can print the default isosurfacesetting by:

>>> h2o.isosurfacesetting

Change the default setting by:

>>> h2o.isosurfacesetting[1].level = 0.001

Delete a isosurfacesetting by:

>>> h2o.isosurfacesetting.delete(1)

Add a new isosurfacesetting by:

>>> h2o.isosurfacesetting[2] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}
>>> h2o.draw_isosurface()

The first value ``-0.002`` is the level for the isosurface, the second value ``[0, 0, 0.8, 0.5]`` is the color. The last value of the color ``0.5`` is used to set the ``transparency``.

The name of a isosurfacesetting can be any string, for example:

>>> h2o.isosurfacesetting['negative'] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}


.. image:: ../_static/figs/volume_h2o_isosurface.png
   :width: 10cm


.. note::
   If the atoms and the isosurface are not in the same place, probably because the cube file has a origin not at (0, 0, 0). Please read the origin and shift the atoms:

   >>> cube = read('test.cube', format='cube', read_data=True, full_output=True)
   >>> volume = cube['data']
   >>> atoms = cube['atoms']
   >>> origin = cube['origin']
   >>> atoms.translate(-origin[0:3])
   >>> h2o = Batoms('h2o', atoms = atoms, volume = volume, draw = False)


2D slicing
---------------------
To add 2D slices of volumetric data in the model, add a plane with ``slicing`` as ``True``.

>>> from batoms.batoms import Batoms
>>> from batoms.bio import read
>>> h2o = read('h2o-homo.cube')
>>> h2o.isosurfacesetting.delete(1)
>>> h2o.draw_isosurface()
>>> h2o.planesetting[(0, 0, 1)] = {'distance': 6, 'slicing': True}
>>> h2o.get_image(viewport = [0, 0, 1], engine = 'cycles')

Change render engine to ``EEVEE`` or ``CYCLES``, and use ``viewport shading`` to see the colored plane.

.. image:: ../_static/figs/volume_h2o_slicing_bwr.png
   :width: 8cm


.. note::
   One can choose colormap by setting ``cmap``. Please vist https://matplotlib.org/stable/tutorials/colors/colormaps.html to see the possible camp.

   >>> h2o.draw_lattice_plane(cmap = 'hot')

   .. image:: ../_static/figs/volume_h2o_slicing_hot.png
      :width: 8cm

