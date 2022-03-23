

===================
Camera
===================


One can change parameters for the default camera by. 

>>> ch4.render.camera.type = "PERSP"
>>> ch4.render.camera.lens = 100

Viewpoint
=============
The ``direction`` keyword is used to set the direction of camera.


.. list-table::
   :widths: 25 25 25 25

   * - Top view (``z``)
     - Front view (``x``)
     - Right view (``y``)
     - Other direction (``x, y, z``)
   * - [0, 0, 1]
     - [1, 0, 0]
     - [0, 1, 0]
     - [1, -0.3, 0.1]
   * -  .. image:: ../../_static/figs/render_direction_top.png 
     -  .. image:: ../../_static/figs/render_direction_front.png 
     -  .. image:: ../../_static/figs/render_direction_right.png 
     -  .. image:: ../../_static/figs/render_direction_any.png 



Camera Type
=============

- ``PERSP``
- ``ORTHO``



