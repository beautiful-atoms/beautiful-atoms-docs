.. module:: batoms.cell

===================
The Bcell object
===================

The :class:`Bcell` object is an object for unit cell. Here is how to creat a cubic unit cell:

>>> from batoms.cell import Bcell
>>> cell = Bcell(label = 'pt', array = [3.98, 3.98, 3.98])

.. image:: /images/bcell-pt.png
   :width: 3cm

Here, the ``label`` keyword to specify the name, and ``array`` keyword to specify the size. Other possible keyword are: ``location``.

See the cell:

>>> cell
Cell([[3.98, 0.0, 0.0], [0.0, 3.98, 0.0], [0.0, 0.0, 3.98]])

>>> cell.length
array([3.98000002, 3.98000002, 3.98000002])

>>> cell.reciprocal
array([[1.57868977, 0.        , 0.        ],
       [0.        , 1.57868977, 0.        ],
       [0.        , 0.        , 1.57868977]]

Set the cell component:

>>> cell[2, 2] += 5

.. image:: /images/bcell-pt-2.png
   :width: 3cm



More details
=======================
A cell contains eight vertices, and is a three-dimensional object. However, only the first four vertices are independent. Therefore, editing these four vertices will change the positoins of other four vertices as well.

.. image:: /images/bcell_vertices.png
   :width: 6cm

The cell vectors are caculated by:

- a = vertices[1] - vertices[0]
- b = vertices[2] - vertices[0]
- c = vertices[3] - vertices[0]

In this case, the origin is translated to vertices[0]. While the orientation is reserved. 


Other methods
=============
* :meth:`~Bcell.copy`
  
For example, copy cell:
        
>>> cell_new = cell.copy('pt_new')

* :meth:`~Bcell.repeat`

>>> from batoms.cell import Bcell
>>> cell = Bcell(label = 'pt', array = [2, 2, 2])
>>> cell.repeat([3, 1, 1])

.. image:: /images/bcell-pt-3.png
   :width: 6cm


List of all Methods
===================

.. autoclass:: Bcell
   :members:
