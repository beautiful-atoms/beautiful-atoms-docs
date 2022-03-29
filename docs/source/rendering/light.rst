

===================
Light
===================

The :class:`Lights` object is used to store and set all parameters related with light.Possible keywords are: ``light_type``, ``energy`` and ``direction`` and ``lock_to_camera``. 

You can print the default light by:

>>> ch4.render.lights

One can change parameters for a light by. 

>>> ch4.render.lights["Default"].type = "POINT"
>>> ch4.render.lights["Default"].energy = 1000

One can ``remove`` or ``add`` a light by:

>>> ch4.render.lights.add("front", direction = [1, 0, 0])
>>> ch4.render.lights.remove("front")

Light direction
================

Light's direction is based on the viewport of camera. Here is the coordinate system for ligh:

- The viewport direction of camera is the z axis;
- right side of camera is x axis;
- up side of camer is the y axis; 




Light type
================

- ``SUN``
- ``POINT``
- ``SUN``
- ``SPOT``
- ``AREA``