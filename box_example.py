# my_script.py
import freecad_env

import FreeCAD
import Part

doc = FreeCAD.newDocument("Demo")

box = Part.makeBox(10, 20, 30)  # width, length, height
Part.show(box)

doc.recompute()
doc.saveAs("output/box_example.FCStd")
