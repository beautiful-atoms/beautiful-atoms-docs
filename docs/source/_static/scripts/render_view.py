from ase.build import fcc111
from batoms import Batoms
import numpy as np
from batoms.utils.butils import removeAll
removeAll()

atoms = fcc111("Au", size=(8, 8, 4), vacuum=0)
au111 = Batoms(label="au111", from_ase=atoms)
au111.cell[2, 2] += 10
au111.cell.draw()
au111.get_image(viewport=[0, 0, 1], output="figs/gallery_top_view.png")
au111.get_image(viewport=[1, 0, 0], output="figs/gallery_side_view.png")
au111.render.camera.type = "PERSP"
au111.get_image(viewport=[1, -0.3, 0.1],
                output="figs/gallery_persp_view.png")
