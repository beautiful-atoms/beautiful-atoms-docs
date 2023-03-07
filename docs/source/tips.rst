.. _tips:

=======
Tips
=======

The following setting will make manipulating more easy, thus are strongly suggested.

Save the startup file
===========================
In Blender, click on the ``File`` dropdown, ``Defaults`` and click ``Save Startup File``. This will save the entire scene for the startup. For example, delete the ``Cube``, and open a python console, then save this scene as startup. 


This is the startup scene of mine:

.. image:: /images/startup.png
   :width: 20cm



3-button-mouse and Numpad
==========================
For laptop without mouse, open preference panel and select:

- Emulate Numpad
- Emulate 3 Button Mouse

After that, you can:

- To rotate the view, press Alt + Left Mouse button and drag.
- To pan the view, press Shift + Alt + Left Mouse button and drag.


.. image:: /images/tips_keyboard.png
   :width: 15cm



Change rotation and zoom center of viewport to selected object
===============================================================

Open preference panel and select:

- Orbit Around Selection
- Zoom to Mouse Position

.. image:: /images/tips_navigation.png
   :width: 15cm



The following tips are optional.


Grid setting
=======================

https://www.katsbits.com/codex/grid/

you can deselect ``Grid`` and ``Floor``.



Python
=============

.. note::

   You could avoid install inside Blender by setting bl to use system python package::

    export BLENDER_COMMAND='blender --python-use-system-env'


Troubleshooting during installation
==============

Here are our advices to some of the issues (albeit rare) you may encounter during the setup:

1. Error: `ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.30' not found`

Newer versions of `scipy` and `numpy` distributed by conda-forge are compiled using 
gcc-toolchain and requires the up-to-date dynamic library to run them. You may specify the 
`LD_LIBRARY_PATH` to let Blender know where to find these libraries instead of your system's default:

```bash
export LD_LIBRARY_PATH=$CONDA_DIR/lib:$LD_LIBRARY_PATH
```

