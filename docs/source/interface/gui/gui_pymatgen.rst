.. _gui_pymatgen:


==============
Pymatgen panel
==============

.. tip::

   :Panel:     :menuselection:`Sidebar region --> Batoms --> Pymatgen`


The ``pymatgen`` panel is used to obtain compounds using the Pymatgen API.


.. image:: /images/gui_pymatgen.png
   :width: 5 cm
   :align: right

To load a structure from MaterialsProject_:

- Input your MaterialsProject API key, please get one from https://www.materialsproject.org/open.
- Find the ID for the structure from MaterialsProject_, input the ID
- click ``Search``


Example
===============

Load MoS\ :sub:`2`\  crystal, then go to the Python console and make a supercell:

>>> mp_2815 *= [6, 6, 1]

.. image:: /images/gui_pymatgen_2.png
   :width: 20 cm

.. _MaterialsProject: https://www.materialsproject.org/


