===============
Windows
===============

Install ASE_ inside Blender
===============================

On Windows, start Blender (need administrator), open a Python console and run the following code::

    import pip
    pip.main(['install', 'ase'])
    pip.main(['install', 'scikit-image'])

Install batoms inside Blender
===============================

- Download the latest stable release (`beautiful-atoms.zip <https://github.com/superstar54/beautiful-atoms/archive/refs/heads/release/2.0.0.zip>`__).

- Extract the file, rename the folder to ``batoms``, and move it to ``blender-3.0.0-linux-x64/3.0/scripts/addons/``. 

- Enable the addon in the Preferences setting. Please vist here to learn how to enable an addon. https://docs.blender.org/manual/en/latest/editors/preferences/addons.html. Or, you can open a Blender Python console, and run the following code to enable the batoms::

    import addon_utils
    import bpy
    addon_utils.enable('batoms', default_set=True)
    bpy.ops.wm.save_userpref()

.. note::
    On Windows, Blender is in folder like ``C:\\Program Files\\Blender Foundation\\Blender\\``.
    See the directory layout docs. https://docs.blender.org/manual/en/dev/advanced/blender_directory_layout.html#blender-directory-layout


Please watch the following video tutorial: https://www.youtube.com/watch?v=UVi3--UrPwI&list=PLsX0h3VeJhK4zkEz9eUd7--wgBVCV-FIM&index=2.



Install batoms-api on your computer
====================================

First install ASE on your computer. On Windows, open Anaconda_ Prompt (suggest to Anaconda_). On Linux, open a terminal, and run::
    
    $ pip3 install --upgrade ase
    $ pip3 install batoms-api

Then set a ``BLENDER_COMMAND`` environment variables. On windows, you can add the system environment variables ``BLENDER_COMMAND`` ::
    
    'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'



.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _pip: https://pypi.org/project/pip/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/
.. _spglib: https://spglib.github.io/spglib/python-spglib.html
.. _matplotlib: https://matplotlib.org/stable/users/installing.html
.. _Anaconda: https://docs.anaconda.com/anaconda/install

