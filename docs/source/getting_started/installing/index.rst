.. _download_and_install:

============
Installation
============

Requirements
============
* Blender_ 3.0 or newer, please install Blender first.
* ASE_
* Scikit-image_

Optional:

* spglib_
* Pymatgen_
* matplotlib_
* openbabel_


.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _pip: https://pypi.org/project/pip/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/
.. _spglib: https://spglib.github.io/spglib/python-spglib.html
.. _matplotlib: https://matplotlib.org/stable/users/installing.html
.. _openbabel: https://open-babel.readthedocs.io/en/latest/index.html
.. _Anaconda: https://docs.anaconda.com/anaconda/install


Use All-Platform Installation script
=====================================
Configuring Blender to use the newly installed environment is slightly different per OS.

.. tabs::

    .. tab:: Windows
        :active:

        .. code-block:: bash

            conda activate blender
            python -m compas_blender.install -v 2.93

        Note that the path ``%PROGRAMFILES%\\Blender Foundation\\Blender 2.93\\2.93`` might be different on your system.
        Check your Blender installation and change the path accordingly.

    .. tab:: OSX

        .. code-block:: bash

            conda activate blender
            python -m compas_blender.install /Applications/blender.app/Contents/Resources/2.93

        Note that the path ``/Applications/blender.app/Contents/Resources/2.93`` might be different on your system.
        Check your Blender installation and change the path accordingly.

    .. tab:: Linux

        .. code-block:: bash

            conda activate blender
            python -m compas_blender.install ~/Blender/2.93

        Note that the path ``~/Blender/2.93`` might be different on your system.
        Check your Blender installation and change the path accordingly.


On Windows and OSX, if Blender is installed in the default location, you can simply provide the version number.

.. code-block:: bash

    conda activate blender
    python -m compas_blender.install -v 2.93


Choose your system
=====================================

.. toctree::
   :maxdepth: 1
   
   linux
   windows
   macos





Please read :ref:`tips` page for more setup.

Others
================================


Pymatgen
----------

If you want to use ``batoms`` with ``Pymatgen``. Rename you blender python folder (``blender-3.0.0-linux-x64/3.0/python``) to ``_python``. Create a virtual environment for your blender using conda::

    conda create --prefix $Path_to_blener/blender-3.0.0-linux-x64/3.0/python python=3.9.7


On Linux, go to the new python directory, e.g. ``blender-3.0.0-linux-x64/3.0/python/bin``, and install ASE_,  scikit-image_ and Pymatgen_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image

    $ ./pip3 install pymatgen


Troubleshooting
================================

Windows
-------------