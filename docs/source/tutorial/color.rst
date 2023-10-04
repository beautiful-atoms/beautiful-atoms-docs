.. _color:


===================
Color setting
===================

Color in ``Batoms`` is float array of 4 items in [0, 1]. The four values are represented as: [``Red``, ``Green``, ``Blue``, ``Alpha``]. Transparency is controlled by the ``Alpha`` value.

Batom and Batoms
=====================

Take CH\ :sub:`4`\  molecule as a example.

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> ch4 = molecule("CH4")
>>> ch4 = Batoms(label = "ch4", from_ase = ch4)
>>> ch4.get_image(viewport = [1, 1, 4], output = "color_ch4_0.png")

.. image:: /images/color_ch4_0.png
   :width: 5cm

The :class:`Batom` object has a ``color`` attribute. One set the ``color`` by:

>>> ch4["H"].color = [0, 0, 0.8, 1.0]
>>> ch4["C"].color = [0.8, 0, 0, 1.0]

.. image:: /images/color_ch4_1.png
   :width: 5cm

Make transparency for ``H`` atoms by setting ``Alpha`` value ``< 1``:

>>> ch4["H"].color = [0, 0, 0.8, 0.2]

.. image:: /images/color_ch4_2.png
   :width: 5cm


Color by attributes
===================
It is useful to color atoms by their attributes (e.g. positions, charges). For example, one can color atoms by their z coordinate:


.. code-block:: python

   from ase.build import bulk
   from batoms import Batoms
   import numpy as np
   au = bulk("Au", cubic=True)*[5, 5, 5]
   au = Batoms(label = "au", from_ase = au)
   # add z coordinate as a new attribute, normalized it to [0, 1]
   z = au.positions[:, 2]
   au.set_attributes({"z_coor": (z-np.min(z))/(np.max(z)-np.min(z)) })
   # color atoms by their z coordinate
   au.species.color_by_attribute("z_coor")
   au.get_image(viewport = [1, 0, 0], output = "color_by_z_coordinate.png")

.. image:: /images/color_by_z_coordinate.png
   :width: 5cm


Bond
===================

One can print the default color by:

>>> ch4.bond.settings[("C", "H")].color1[:]

One can change color for bond pair ``C-H`` by:

>>> ch4.bond.settings[("C", "H")].color1 = [0.8, 0.1, 0.3, 0.5]
>>> ch4.bond.settings[("C", "H")].color2 = [0.1, 0.3, 0.2, 1.0]
>>> ch4.model_style = 1

``color1`` is for the first species in the bond pair (``C``), and ``color2`` is for the second species (``H``).

.. list-table::
   :widths: 50 50

   * -  |color3|
     -  |color4|




Polyhedra
================

One can print the default color by:


>>> ch4.polyhedras.setting["C"].color[:]

One can change color for Polyhedra ``C`` by:

>>> ch4.polyhedras.setting["C"].color = [0.8, 0.1, 0.3, 0.8]
>>> ch4.bond.settings[("C", "H")].polyhedra = True
>>> ch4.model_style = 2

.. list-table::
   :widths: 50 50

   * -  |color5|
     -  |color6|


.. image:: 
   :width: 5cm

.. |color0|  image:: /images/color_ch4_0.png
   :width: 5cm
.. |color1|  image:: /images/color_ch4_1.png
   :width: 5cm
.. |color2|  image:: /images/color_ch4_2.png
   :width: 5cm
.. |color3|  image:: /images/color_ch4_3.png
   :width: 5cm
.. |color4|  image:: /images/color_ch4_4.png
   :width: 5cm
.. |color5|  image:: /images/color_ch4_5.png
   :width: 5cm
.. |color6|  image:: /images/color_ch4_6.png
   :width: 5cm