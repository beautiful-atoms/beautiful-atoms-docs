.. module:: batoms.cell

===================
The Bcell object
===================

The :class:`Bcell` object is an object for unit cell. Here is how to creat a cubic unit cell:

>>> from batoms.cell import Bcell
>>> cell = Bcell(label = 'pt', array = [2, 2, 2])

.. image:: ../_static/figs/bcell-pt.png
   :width: 3cm

Here, the ``label`` keyword to specify the name, and ``array`` keyword 
to specify the size. Other possible keyword are: ``location``.

See the cell:

>>> tio2.cell
Cell([[4.6532721519470215, 0.0, 0.0], [0.0, 4.6532721519470215, 0.0], [0.0, 0.0, 2.969202995300293]])

>>> tio2.cell.length
array([4.65327215, 4.65327215, 2.969203  ])

>>> tio2.cell.reciprocal
array([[1.35027248, 0.        , 0.        ],
       [0.        , 1.35027248, 0.        ],
       [0.        , 0.        , 2.11611847]]

Set the cell component:

>>> cell[2, 2] += 3

.. image:: ../_static/figs/bcell-pt-2.png
   :width: 3cm





Other methods
=============
* :meth:`~Bcell.copy`
  
For example, copy cell:
        
>>> cell_new = cell.copy('pt_new')

* :meth:`~Bcell.repeat`

>>> from batoms.cell import Bcell
>>> cell = Bcell(label = 'pt', array = [2, 2, 2])
>>> cell.repeat([3, 1, 1])

.. image:: ../_static/figs/bcell-pt-3.png
   :width: 6cm


List of all Methods
===================

.. autoclass:: Bcell
   :members:
