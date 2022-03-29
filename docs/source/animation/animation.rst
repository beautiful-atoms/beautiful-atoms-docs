.. _animation_python:

===================
Python script
===================

Here, we rotate a molecule and save it to a list:

>>> from ase.build import molecule
>>> atoms = molecule("C2H6SO")
>>> images = []
>>> for i in range(20):
>>>     temp = atoms.copy()
>>>     temp.rotate(18*i, "z", center = atoms[0].position)
>>>     images.append(temp)

Then load it to Batoms:

>>> from batoms import Batoms
>>> c2h6so = Batoms(label = "c2h6so", from_ase = images)


Or you can render all images by:

>>> c2h6so.get_image([0, 0, 1], engine = "eevee", animation = True)


Then, on Linux, run following command to convert all png files to a gif file::

    convert -dispose Background *.png animation.gif


.. image:: /images/animation_c2h6so.gif
   :width: 8cm



>>> from batoms.bio import read
>>> images = read("c2h6so-animation.xyz", index = ":")


For ``Espresso`` output file:

>>> from batoms.bio import read
>>> images = read("espresso.pwo", index = ":")



