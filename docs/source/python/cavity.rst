.. module:: batoms.plugins.cavity

===============================
The Cavity object
===============================

The :class:`Cavity` object is used to search and draw cavity for :class:`Batoms`. It has a ``settings`` attribute (:class:`CavitySettings` object), which stores and set all parameters related to cavity data. Possible keywords for settings are: ``min``, ``max``, ``scale``, ``material_style`` and ``color``. 


Here we show an example of drawing cavities for MOF-5. First, we read a MOF-5 structure.

>>> from ase.io import read
>>> from batoms import Batoms
>>> atoms = read("mof-5.cif")
>>> mof = Batoms(label = "mof", from_ase = atoms)
>>> # make a supercell in a direction.
>>> mof *= [2, 1, 1]
>>> # change width of cell
>>> mof.cell.width = 0.05

There are no default settings, as shown below:

>>> mof.cavity.settings
Name       min   max   scale                color  
------------------------------------------------------------


One can add a setting by:

>>> mof_5.cavity.settings['cave1'] = {'min':6, 'max': 7, 'color': [1, 0, 0, 1]}
>>> mof.cavity.draw()

In this case, only the spheres with radius in the range of 6--7 Å will be drawn.



Auto-search cavity
---------------------
If no setting item is added, the `draw` function will search and draw all cavities automatically.

>>> # remove previous settings
>>> mof_5.cavity.settings.remove('cave1')
>>> mof_5.cavity.settings
Name       min   max   scale                color  
------------------------------------------------------------
>>> mof.cavity.draw()


.. image:: /images/python_cavity_mof_5_0.png
   :width: 10cm

In the case of MOF-5, two different cavities (names are `"0"` and `"1"`) with different radii are found.

>>> mof.cavity.settings
Name       min   max   scale                color  
0      7.000   8.000   1.000   [1.00  0.00  0.00  1.00] 
1      5.000   6.000   1.000   [0.00  1.00  0.00  1.00] 
------------------------------------------------------------

The `min` and `max` parameters are the range of the radius of that cavity. The `scale` parameter is used to change the size of the sphere used to represent the cavity.

One change the settings. 

>>> # change the size of `0` by half of the original.
>>> mof.cavity.settings['0'].scale = 0.5
>>> # change the color of `1`.
>>> mof.cavity.settings['1'].color = [1, 1, 0, 1]
>>> mof.cavity.draw()


.. image:: /images/python_cavity_mof_5_1.png
   :width: 10cm



--

.. note::
   **Small cavity**

   The default smallest cavity to be searched is 4 Å. You can change it by:

   >>> mof.minCave = 3.
   >>> # for a small cave, a small resolution is needed. The default resolution is 1 Å.
   >>> mof.resolution = 0.5
   >>> mof.cavity.draw()

GUI
---------
One can also set the cavity using the GUI panel. Please read :ref:`gui_cavity` page for more setup.


