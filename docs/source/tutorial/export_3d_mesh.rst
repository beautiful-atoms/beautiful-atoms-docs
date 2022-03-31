
===================
Export 3D mesh
===================

Use :meth:`~Batoms.export_mesh` to save 3D mesh data. Use parameters ``with_cell``, ``with_bond``, ``with_polyhedra``, ``with_boundary`` and ``with_search_bond`` to control the output meshes.

Support formats:

- x3d
- obj
- fbx

.. note::
    After the export_mesh, all Batoms structures become mesh data, thus the python code does not work properly anymore. Thus, this function is suggested to be called at the very end.
    If you want to do anything else with python, please reopen blender and create the structures again.

X3D format
========

.. code:: python

    from ase.build import molecule
    from batoms import Batoms
    from batoms.bio.bio import read
    bpy.ops.batoms.delete()
    c2h6so = Batoms("c2h6so", from_ase=molecule("C2H6SO"))
    c2h6so.model_style = 1
    c2h6so.export_mesh("c2h6so.x3d", with_bond=True)


OBJ format
============

Two files are exported:

- xxx.obj: mesh data;
- xxx.matl: materials data;


.. code:: python

    from batoms.bio.bio import read
    bpy.ops.batoms.delete()
    tio2 = read("../tests/datas/tio2.cif")
    tio2.boundary = 0.01
    tio2.model_style = 2
    tio2.bonds.show_search = True
    tio2.export_mesh("tio2.obj", with_cell=True,
                     with_polyhedra=True,
                     with_boundary=True,
                     with_search_bond=True,
                     with_bond=True)

FBX format
============

.. code:: python

    from batoms.bio.bio import read
    bpy.ops.batoms.delete()
    tio2 = read("../tests/datas/tio2.cif")
    tio2.boundary = 0.01
    tio2.model_style = 2
    tio2.bonds.show_search = True
    tio2.export_mesh("tio2.fbx", with_cell=True,
                     with_polyhedra=True,
                     with_boundary=True,
                     with_search_bond=True,
                     with_bond=True)