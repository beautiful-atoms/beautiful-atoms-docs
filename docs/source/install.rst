.. _download_and_install:

============
Installation
============

Requirements
============
* Blender_ 2.80 or newer, please install Blender first.
* ASE_

Optional:

* Scikit-image_
* spglib_
* Pymatgen_
* matplotlib_


.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _pip: https://pypi.org/project/pip/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/
.. _spglib: https://spglib.github.io/spglib/python-spglib.html
.. _matplotlib: https://matplotlib.org/stable/users/installing.html
.. _Anaconda: https://docs.anaconda.com/anaconda/install


Install ASE_ inside Blender
===============================

On Linux and MacOS, go to your Blender python directory, e.g. ``blender-2.93-linux-x64/2.93/python/bin``, install pip_::
    
    $ ./python3.9 -m ensurepip
    $ ./python3.9 -m pip install --upgrade pip
    
Install ASE_ and scikit-image_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image

    $ ./pip3 install spglib

On Windows, start Blender (need administrator), open a Python console and run the following code::

    import pip
    pip.main(['install', 'ase'])
    pip.main(['install', 'scikit-image'])

    For ``spglib``, you may need to install Microsoft visual C++ Build Tools.





Install batoms inside Blender
===============================

- Download the source files from https://github.com/superstar54/beautiful-atoms. 

- Extract the file, rename the folder to ``batoms``, and move it to ``blender-2.93.4-linux-x64/2.93/scripts/addons/``. 

- Enable the addon in the Preferences setting. Please vist here to learn how to enable an addon. https://docs.blender.org/manual/en/latest/editors/preferences/addons.html. Or, you can open a Blender Python console, and run the following code to enable the batoms::

    import addon_utils
    addon_utils.enable('batoms', default_set=True)

.. note::
    On Windows, Blender is in folder like ``C:\\Program Files\\Blender Foundation\\Blender\\``.
    On MacOS, Blender is in ``/Applications/Blender.app/Contents/MacOS/Blender``.
    See the directory layout docs. https://docs.blender.org/manual/en/dev/advanced/blender_directory_layout.html#blender-directory-layout

Install batoms-api on your computer
====================================

First install ASE on your computer. On Windows, open Anaconda_ Prompt (suggest to Anaconda_). On Linux, open a terminal, and run::
    
    $ pip3 install --upgrade ase
    $ pip3 install batoms-api

Then set a ``BLENDER_COMMAND`` environment variables. On Linux, set these permanently in your :file:`~/.bashrc` file::

    export BLENDER_COMMAND='<path-to-blender>/blender'

On windows, you can add the system environment variables ``BLENDER_COMMAND`` ::
    
    'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'


Test your installation
======================

Start Blender, in the python console, run:

>>> from batoms import Batoms
>>> h2o = Batoms('h2o', {'O': [[0, 0, 0.40]], 'H': [[0, -0.76, -0.2], [0, 0.76, -0.2]]})


.. image:: _static/figs/batoms-h2o.png
   :width: 3cm
   
If you saw a water molecule, congratulations!


Please read :ref:`tips` page for more setup.

Others
================================


Pymatgen
----------

If you want to use ``batoms`` with ``Pymatgen``. Rename you blender python folder (``blender-2.93-linux-x64/2.93/python``) to ``_python``. Create a virtual environment for your blender using conda::

    conda create --prefix $Path_to_blener/blender-2.93.4-linux-x64/2.93/python python=3.9.2


On Linux, go to the new python directory, e.g. ``blender-2.93-linux-x64/2.93/python/bin``, and install ASE_,  scikit-image_ and Pymatgen_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image

    $ ./pip3 install pymatgen


Troubleshooting
================================

Windows
-------------