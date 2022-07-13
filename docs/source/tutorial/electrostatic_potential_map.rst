.. _electrostatic_potential_map:

================================
Electrostatic potential maps
================================

The molecular electrostatic potential (MEP) shows the electrostatic potential on the molecular surface. MEP illustrates the charge distributions of molecules three dimensionally.

Quantum chemical methods
============================
One can obtain the eletrostatic potential by DFT calculation using softwares, e.g. CP2K or Gaussian. Here is an example of H\ :sub:`2`\ O. The ``h2o-hartree.cube`` file is the electrostatic potential calculated by DFT.


Example in Python
-------------------------------
>>> from batoms import Batoms
>>> from ase.io.cube import read_cube_data
>>> bpy.ops.batoms.delete()
>>> hartree, atoms = read_cube_data('../tests/datas/h2o-hartree.cube')
>>> batoms = Batoms("h2o", from_ase=atoms)
>>> # add volumetric data
>>> batoms.volumetric_data['hartree'] = -hartree
>>> # set probe to 0 for the Van der Waals surface
>>> batoms.molecular_surface.settings['1'].probe = 0
>>> # color the molecular surface by the volumetric data
>>> batoms.molecular_surface.settings['1'].color_by = 'hartree'
>>> batoms.molecular_surface.draw()
>>> batoms.get_image([-1, 0, 0], output="h2o-MEP.png")

.. image:: /images/h2o_MEP.png
   :width: 10 cm


Example in GUI
-------------------------------
In  :ref:`gui_molecular_surface`, one can choose 'hartree' for the coloring in ``color_by``.

Classic method
======================
Here is a fast way to calculate electrostatic potential maps using classic method, in which the electrostatic potential is calculated using the atomic partial charges. We estimates the atomic partial charges based on `MMFF94`  force field using openbabel.

Example in Python
-------------------------------
Here is an example of H\ :sub:`2`\ O.


>>> from batoms import Batoms
>>> from ase.io.cube import read_cube_data
>>> bpy.ops.batoms.delete()
>>> bpy.ops.batoms.molecule_add(label='h2o', formula='H2O')
>>> batoms = Batoms("h2o")
>>> # set probe to 0 for the Van der Waals surface
>>> batoms.molecular_surface.settings['1'].probe = 0
>>> # color the molecular surface by the volumetric data
>>> batoms.molecular_surface.settings['1'].color_by = 'Electrostatic_Potential'
>>> batoms.molecular_surface.draw()
>>> batoms.get_image([-1, 0, 0], output="h2o_MEP_classic.png")


.. image:: /images/h2o_MEP_classic.png
   :width: 5 cm


Example in GUI
-------------------------------
In  :ref:`gui_molecular_surface`, one can choose 'Electrostatic_Potential' for the coloring in ``color_by``.




