
============================
Cavity
============================


Sphere model
--------------

The :meth:`~Batoms.plugins.cavity.Cavity` class is used to draw a sphere to represent a cavity in porous materials. We find the cavity with a grid based algorithm. Here we search cavity in the MOF-5 crystal.


>>> from ase.io import read
>>> from batoms import Batoms
>>> from batoms.draw import draw_plane
>>> atoms = read("docs/source/_static/datas/mof-5.cif")
>>> mof = Batoms(label = "mof", from_ase = atoms)
>>> mof["H"].color = [0.6, 0, 1.0, 1.0]
>>> mof["C"].color = [0.0, 0.6, 0.1, 1.0]
>>> mof.polyhedra.settings["Zn"].color = [0.1, 0.4, 0.7, 1.0]
>>> mof.model_style = 2
>>> mof.cavity.draw()


.. image:: /images/gallery_cavity.png
   :width: 15cm


Polyhedral model
-----------------
In order to represent the cavity by a polyhedral model, we add a ghost site (species ``X``) at the center of a cavity. Then set the bond between ``X`` and atoms at the corners of the cage by ``bonds.setting``.


>>> from ase.build import molecule
>>> from batoms import Batoms
>>> from batoms.draw import draw_plane
>>> c60 = molecule("C60")
>>> pos = c60.get_center_of_mass()
>>> c60 = Batoms(label = "c60", from_ase = c60)
>>> c60["C"].color = [0.1, 0.1, 0.1, 1.0]
>>> c60.bond.settings[("C", "C")].color1 = [0.2, 0.8, 0.1, 1.0]
>>> c60.bond.settings[("C", "C")].type = "0"
>>> # we add a ghost site (species ``X``) at the center of a cavity
>>> x = Batoms("x", {"X":[pos]})
>>> c60 = c60 + x
>>> # add bond ()`X", "C`), and set polyhedra to True
>>> c60.bond.settings[("X", "C")] = {"species1": "X", "species2": "C", "min": 0, "max": 10, "search": 2, "polyhedra": True}
>>> c60.polyhedra.settings["X"].color = [0.4, 0.4, 0, 1.0]
>>> c60.model_style = 1
>>> # draw polyhedral model manually and not show the edge
>>> c60.draw_polyhedras(show_edge = False)

.. image:: /images/gallery_c60.png
   :width: 15cm
