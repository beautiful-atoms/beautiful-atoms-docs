.. module:: batoms.isosurface.isosurfacesetting

=============================
The Isosurface object
=============================

The :class:`Isosurface` object is used to draw isosurface for :class:`Batoms`. It has a ``settings`` attribute (:class:`IsosurfaceSettings` object), which stores and sets all parameters related to volumetric data. Possible keywords for ``settings`` are: ``level``, ``color``. 


Here we show an example of drawing isosurfaces from cube file.

>>> from ase.io.cube import read_cube_data
>>> from batoms import Batoms
>>> volume, atoms = read_cube_data('docs/source/_static/datas/h2o-homo.cube')
>>> h2o = Batoms('h2o', from_ase = atoms, volume = volume)


You can print the default setting by:

>>> h2o.isosurface.settings

One add a setting by. 

>>> h2o.isosurface.settings[1] = {'level': 0.002, 'color': [1, 1, 0, 0.5]}
>>> h2o.isosurface.settings[2] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}
>>> h2o.isosurface.draw()

.. image:: /images/volume_h2o_isosurface.png
   :width: 5cm


