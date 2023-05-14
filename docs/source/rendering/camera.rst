

===================
Camera
===================


One can change parameters for the default camera by. 

>>> ch4.render.camera.type = "PERSP"
>>> ch4.render.camera.lens = 100

Viewpoint
=============

The ``viewport`` keyword is used to set the direction of camera. By default, the camera will look at the center of a Batoms object from the viewport direction.

>>> h2o.render.viewport = [0, 0, 1]
>>> # from b axis of Au (111) surface
>>> au111.render.viewport = au111.cell[1]
>>> # Look at any surface with the Miller index (hkl)
>>> import numpy as np
>>> au111.render.viewport = np.dot([h, k, l], au111.cell)


.. list-table::
   :widths: 25 25 25 25

   * - Top view (``z``)
     - Front view (``x``)
     - Right view (``y``)
     - Other viewport (``x, y, z``)
   * - [0, 0, 1]
     - [1, 0, 0]
     - [0, 1, 0]
     - [1, -0.3, 0.1]
   * -  .. image:: ..//images/render_direction_top.png 
     -  .. image:: ..//images/render_direction_front.png 
     -  .. image:: ..//images/render_direction_right.png 
     -  .. image:: ..//images/render_direction_any.png 



Camera Type
=============

- ``PERSP``
- ``ORTHO``



