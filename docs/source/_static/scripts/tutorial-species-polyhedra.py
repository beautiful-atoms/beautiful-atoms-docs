from batoms.bio import read
bpy.ops.batoms.delete()
tio2 = read("../tests/datas/tio2.cif")
tio2.replace([0], 'Ti_1')
tio2.bonds.setting
tio2.model_style = 2
tio2.bonds.setting.add(('Ti_1', 'O'))
tio2.bonds.setting
tio2.bonds.setting[('Ti_1', 'O')].polyhedra = True
tio2.bonds.setting
tio2.polyhedras.setting.add('Ti_1')
tio2.polyhedras.setting['Ti_1'].color = (0, 1, 1, 0.8)
tio2.polyhedras.setting
tio2.model_style = 2