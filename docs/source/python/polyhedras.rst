.. module:: batoms.polyhedra.polyhedrasetting

===========================
The Polyhedrasetting object
===========================

The :class:`Polyhedrasetting` object is used to store and set all parameters related with polyhedra. Possible keywords are: ``symbol``, ``color`` and ``linewidth``. 



You can print the default polyhedrasetting by:

>>> ch4.polyhedras.setting

One can change color for polyhedra ``C`` by. 

>>> ch4.polyhedras.setting['C'].color = [0.8, 0.1, 0.3, 0.3]
>>> ch4.model_style = 2


