import freecad_env

import FreeCAD, Part, Arch
from FreeCAD import Vector

doc = FreeCAD.newDocument("Lumber_Parts")

def add_lumber(name, width_in, height_in, length_ft):
    # Convert inches to mm
    width = width_in * 25.4
    height = height_in * 25.4
    length = length_ft * 304.8  # ft to mm

    box = Part.makeBox(length, width, height)
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = box
    obj.Placement.Base = Vector(0, 0, 0)
    
    # # Add BIM properties for reuse
    arch_obj = Arch.makeStructure(obj)
    arch_obj.Label = name
    arch_obj.IfcType = "Beam"
    return arch_obj

# Add dimensional lumber
add_lumber("2x12", 1.5, 11.25, 8)
add_lumber("2x10", 1.5, 9.25, 8)
add_lumber("2x8", 1.5, 7.25, 8)
add_lumber("2x6", 1.5, 5.5, 8)

# Add plywood sheets
def add_plywood(name, thickness_in):
    sheet = Part.makeBox(2438.4, 1219.2, thickness_in * 25.4)  # 96"x48" in mm
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = sheet
    arch_obj = Arch.makeStructure(obj)
    arch_obj.Label = name
    arch_obj.IfcType = "Plate"
    return arch_obj

add_plywood("Plywood_5_8", 0.625)
add_plywood("Plywood_3_8", 0.375)
add_plywood("Plywood_1", 1.0)

# Add LSL
add_lumber("LSL", 1.75, 11.875, 8)

doc.recompute()

doc.saveAs("output/parts.FCStd")
