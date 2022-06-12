.. module:: batoms.light

===========================
The Lights object
===========================

The :class:`Lights` object is used to store and set all parameters related with polyhedra. It is a collection of :class:`Light` objects. It should always bind with a :class:`Render` object. Possible keywords are: ``light_type``, ``energy`` and ``direction`` and ``lock_to_camera``. 

You can print the default light by:

>>> ch4.render.lights

One can change parameters for a light by. 

>>> ch4.render.lights['Default'].type = 'POINT'
>>> ch4.render.lights['Default'].energy = 1000

One can ``remove`` or ``add`` a light by:

>>> ch4.render.lights.add('front', direction = [1, 0, 0])
>>> ch4.render.lights.remove('front')

