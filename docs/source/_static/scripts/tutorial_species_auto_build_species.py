from batoms.bio import read
from batoms.draw import draw_plane
from batoms.utils.butils import removeAll, set_world
import bpy

# remove other batoms 
bpy.ops.batoms.delete()

mag = read("magnetite.cif")
# Auto build species based on equivalent_atoms
mag.auto_build_species()
mag.boundary = 0
# Change color for the polyhedra of different species.
mag.polyhedra.settings['Fe'].color[:] = [0.8, 0.8, 0, 1]
mag.polyhedra.settings['Fe_1'].color[:] = [0, 0.8, 0, 1]
mag.polyhedra.settings['Fe_2'].color[:] = [0, 0, 0.8, 1]
mag.model_style = 2
mag.bond.show_search = True
mag.cell.draw()
# ====================================
# Following code is used to set the rendering parameters
# world color
set_world(color = [0.2, 0.2, 0.2, 1.0])
# plane
plane = draw_plane(location = [0, 0, mag.get_all_vertices()[:, 2].min() - max(mag.size)], size = 200, color = (0.9, 0.9, 0.9, 1))
# rendering parameters
mag.render.viewport = [-0.5, -1, 0.2]
mag.render.engine = 'cycles'
mag.render.lights['Default'].energy = 50
mag.render.lights['Default'].direction = [0.1, 0.5, 1]
mag.get_image(output = 'magnetite_polyhedra_species.png')