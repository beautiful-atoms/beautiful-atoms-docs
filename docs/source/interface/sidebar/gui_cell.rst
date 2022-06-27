.. _gui-cell:


==============
Cell panel
==============

The ``Cell`` panel is used to set propeties related with the unit cell.

.. image:: /images/gui_cell.png
   :width: 5 cm
   :align: right


Cell
==========
In the Cell parameters box, lattice parameters are input in by three axes: a, b, and c ( unit of Å).


Transformation of the unit cell
===================================
Transform crystal axes by specifying 4 × 4 matrix (first 3x3 is rotation and the last 3 × 1 is translation).

- Select the objects.
- Input the transformation matrix.
- Clicking the Apply Transform.

The transformation matrix is also used to convert primitive lattice to complex lattice.

Supercell
============
Supercell is special case of transformation. In this case, the rotation matrix is a diagonal matrix.

For example, we make a [4, 4, 1] supercell for a Au (111) surface.

.. image:: /images/gui_cell_2.png
   :width: 20 cm


Boundary
==========
Atoms are searched within a boundary defined by ranges along a, b, and c axes. 
Search atoms outside the boundary is controled by the ``search`` keyword in :class:`Bondsetting`.


