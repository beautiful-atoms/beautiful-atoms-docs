.. module:: batoms.polyhedra

===========================
The Polyhedra object
===========================

The :class:`Polyhedra` object is used draw polyhedra for :class:`Batoms`. It has a ``settings`` attribute (:class:`PolyhedraSettings` object), which store and set all parameters related with polyhedra. Possible keywords for ``settings`` are: ``symbol``, ``color`` and ``linewidth``. 



You can print the default polyhedrasetting by:

>>> ch4.polyhedra.settings

One can change color for polyhedra ``C`` by. 

>>> ch4.polyhedra.settings['C'].color = [0.8, 0.1, 0.3, 0.3]
>>> ch4.model_style = 2


