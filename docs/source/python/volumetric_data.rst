.. module:: batoms.volumetric_data.VolumetricData

=============================
The VolumetricData object
=============================

The :class:`VolumetricData` object is used to store all parameters related to volumetric data.


Here we show an example of add volumetric data from cube file.

>>> from ase.io.cube import read_cube_data
>>> from batoms import Batoms
>>> volumetric_data, atoms = read_cube_data("../tests/datas/h2o-homo.cube")
>>> h2o = Batoms('h2o', from_ase = atoms)
>>> # add volumetric data
>>> h2o.volumetric_data['homo'] = volumetric_data


Then, one can get the volumetric data by:

>>> data = h2o.volumetric_data['homo']
>>> data.shape
(23, 27, 24)

Multiple volumetric data can be added:

>>> h2o.volumetric_data['test'] = h2o.volumetric_data['homo'] + 1
>>> h2o.volumetric_data
name          npoint        shape  
homo        14904 [   23     27     24] 
test        14904 [   23     27     24] 
------------------------------------------------------------

