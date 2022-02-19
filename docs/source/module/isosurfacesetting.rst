.. module:: batoms.isosurfacesetting

=============================
The Isosurfacesetting object
=============================

The :class:`Isosurfacesetting` object is used to store and set all parameters related with volumetric data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``level``, ``color``. 


Here we show a example of draw isosurfaces from cube file.

>>> from ase.io.cube import read_cube_data
>>> from batoms import Batoms
>>> volume, atoms = read_cube_data('docs/source/_static/datas/h2o-homo.cube')
>>> h2o = Batoms('h2o', from_ase = atoms, volume = volume, draw = False)


You can print the default isosurfacesetting by:

>>> h2o.isosurfacesetting

One add a isosurfacesetting by. 

>>> h2o.isosurfacesetting[1] = {'level': 0.002, 'color': [1, 1, 0, 0.5]}
>>> h2o.isosurfacesetting[2] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}
>>> h2o.draw_isosurface()

.. image:: ../_static/figs/volume_h2o.png
   :width: 5cm


List of all Methods
====================

.. autoclass:: Isosurfacesetting
   :members: