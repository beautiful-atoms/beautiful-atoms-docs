.. module:: batoms.bond

========================
The Bond object
========================

The :class:`Bond` object is used draw bond for :class:`Batoms`. It has a ``settings`` attribute (:class:`BondSettings` object), which store and set all parameters related with bonds. Possible keywords for ``settings`` are: ``symbol1``, ``symbol2``, ``min``, ``max``, ``search``, ``polyhedra``, ``color1``, ``color2``, ``bondlinewidth``, ``style``, ``material_style``.


>>> from ase.build import molecule
>>> from batoms import Batoms
>>> ch4 = Batoms('ch4', from_ase = molecule('CH4'))
>>> ch4.model_style = 2

.. image:: /images/bondsetting_ch4_0.png
   :width: 5cm

You can print the default bond.settings by:

>>> ch4.bond.settings

.. image:: /images/bondsetting_ch4_1.png
   :width: 15cm

By defaut, we use default radius (``ase.data.covalent_radii``) for every atoms, and the maximum bondlength is the sum of two radius and then scaled by a default cutoff (1.3). The minimum bondlength is 0.5.


Style
===========
One set the bond style for a bond pair by:

>>> ch4.bond.settings[('C', 'H')].style = '3'

.. image:: /images/bond_style_setting_0.png
   :width: 3cm


One set the bond style for a bond by (Here is the first bond):

>>> ch4.bonds[0].style = '3'

.. image:: /images/bond_style_setting_1.png
   :width: 3cm

Here, four bond models are supported.

.. list-table::
   :widths: 25 25 25 25

   * - ``0``
     - ``1``
     - ``2``
     - ``3``
   * -  .. image:: /images/bondsetting_style_0.png 
     -  .. image:: /images/bondsetting_style_1.png 
     -  .. image:: /images/bondsetting_style_2.png 
     -  .. image:: /images/bondsetting_style_3.png 
  

Polyhedra
==================

One can change setting for a bond pair. For example, to build up coordination polyhedra, the value for ``polyhedra`` should be set to ``True``:

>>> ch4.bond.settings[('C', 'H')].polyhedra = True
>>> ch4.model_style = 2


.. image:: /images/bondsetting_ch4_2.png
   :width: 5cm


Search bond mode
==================
 
 - ``0``  Do not search atoms beyond the boundary
 - ``1``  Search additional atoms if species1 is included in the boundary
 - ``2``  Search bonded atoms of species1 or species2 recursively. This mode is the used for searching molecules.

To change setting for ``search`` by:

>>> tio2.bond.settings[('Ti', 'O')].search = 0
>>> tio2.update_boundary()
>>> tio2.model_style = 2


.. image:: /images/bondsetting_tio2_2.png
   :width: 8cm


Color
==================

One can print the default color by:

>>> ch4.bond.settings[('C', 'H')].color1[:]

One can change color for a bond pair. 

>>> ch4.bond.settings[('C', 'H')].color1 = [0.8, 0.1, 0.3, 0.5]
>>> ch4.bond.settings[('C', 'H')].color2 = [0.1, 0.3, 0.2, 1.0]
>>> ch4.model_style = 1


.. image:: /images/bondsetting_ch4_3.png
   :width: 5cm



High order bond
=====================

One can set bond order for each bond:

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> c6h6 = Batoms("c6h6", from_ase = molecule("C6H6"))
>>> c6h6.model_style = 1
>>> c6h6.bonds[0].order = 2
>>> c6h6.bonds[5].order = 2
>>> c6h6.bonds[9].order = 2

.. image:: /images/bondsetting_order.png
   :width: 5cm


Or one can set the bond order automaticaly based on `pybel <http://openbabel.org/wiki/Bond_Orders>`_:

>>> c6h6.bonds.bond_order_auto_set()


