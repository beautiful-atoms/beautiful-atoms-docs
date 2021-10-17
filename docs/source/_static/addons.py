import bpy
import addon_utils
import sys
import os
import subprocess


for addon in bpy.context.preferences.addons:
    print(addon.module)

addon_utils.enable('batoms_addon', default_set=True) 

for addon in bpy.context.preferences.addons:
    print(addon.module)
