.. module:: batoms.render

===================
The Render object
===================

The :class:`Render` object is to render atomic structure.

.. code:: python

    from ase.build import molecule
    from batoms import Batoms
    from batoms.render import Render
    atoms = molecule('C2H6SO')
    c2h6so = Batoms(label = 'c2h6so', atoms = atoms)
    c2h6so.render = Render(viewport = [1, 0, 0], engine = 'eevee')
    c2h6so.get_image(output = 'images/c2h6so.png')


Parameters
------------

- viewport: specifies the direction of camera.
- engine: specifies the render engine.
- resolution
- animation
- gpu
- run_render
- transparent
- compute_device_type
- studiolight


You can print the parameters for render by:

>>> c2h6so.render


Engine
=============

Three engines can be used:


.. list-table::
   :widths: 25 25 25

   * - BLENDER_WORKBENCH
     - BLENDER_EEVEE
     - CYCLES
   * - Fast
     - Standard
     - Most powerfull, slow
   * -  .. image:: ../_static/figs/render_workbench.png 
     -  .. image:: ../_static/figs/render_eevee.png 
     -  .. image:: ../_static/figs/render_cycles.png 


Viewport
===========
The ``viewport`` keyword is used to set the direction of camera.


.. list-table::
   :widths: 25 25 25 25

   * - Top
     - Front
     - Right
     - Other direction
   * - [0, 0, 1]
     - [1, 0, 0]
     - [0, 1, 0]
     - [1, -0.3, 0.1]
   * -  .. image:: ../_static/figs/render_direction_top.png 
     -  .. image:: ../_static/figs/render_direction_front.png 
     -  .. image:: ../_static/figs/render_direction_right.png 
     -  .. image:: ../_static/figs/render_direction_any.png 



Edit the studio light
=======================

The Workbench engine use the studio light instead of the lights in the scene. You can choose the following studio light



.. list-table::
   :widths: 25 25 25 25 25 25

   * - ``Default``
     - ``basic.sl``
     - ``outdoor.sl``
     - ``paint.sl``
     - ``rim.sl``
     - ``studio.sl``
   * -  .. image:: ../_static/figs/studiolight_Default.png 
     -  .. image:: ../_static/figs/studiolight_basic.sl.png 
     -  .. image:: ../_static/figs/studiolight_outdoor.sl.png 
     -  .. image:: ../_static/figs/studiolight_paint.sl.png 
     -  .. image:: ../_static/figs/studiolight_rim.sl.png 
     -  .. image:: ../_static/figs/studiolight_studio.sl.png 


>>> h2o.render.studiolight = 'paint.sl'

To make your own studio light. Please read: https://docs.blender.org/manual/en/latest/editors/preferences/lights.html#prefs-lights-studio. Please save it, for example ``myown.sl``, then use it by:

>>> h2o.render.studiolight = 'mywon.sl'


Other methods
=============

* :meth:`~Render.set_direction_camera_light`
* :meth:`~Render.get_image`
* :meth:`~Render.motion_blur`



List of all Methods
===================

.. autoclass:: Render
   :members: