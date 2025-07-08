import freecad_env






# Parameters
stringer_thickness = 38.1  # mm
first_rise_height = 184.15
rise_height = 184.15
num_rise = 4
run_depth = 254.0
num_run = 3
kicker_depth = 101.6
kicker_height = 50.8

import FreeCAD, Part

import FreeCAD as App
import Part, PartDesign, Sketcher
from FreeCAD import Vector

doc_name="StairStringerFixed"

doc = App.newDocument(doc_name)
# App.setActiveDocument(doc_name)
# App.ActiveDocument=App.getDocument(doc_name)

body=doc.addObject('PartDesign::Body','Body')
body.Label = 'Body'

sketch=body.newObject('Sketcher::SketchObject','Sketch')
sketch.AttachmentSupport = (doc.getObject('XY_Plane'),[''])
sketch.MapMode = 'FlatFace'

sketch.addGeometry(Part.LineSegment(App.Vector(28.786367,0.000000,0),App.Vector(18.101997,0.000000,0)),False)
sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1)) 
sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,2,-1))
# sketch.addConstraint(Sketcher.Constraint('Horizontal',0)) 

sketch.addGeometry(Part.LineSegment(App.Vector(18.101997,0.000000,0),App.Vector(18.248360,7.090004,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,1,1)) 
sketch.addConstraint(Sketcher.Constraint('Vertical',1)) 

sketch.addGeometry(Part.LineSegment(App.Vector(18.248360,7.090004,0),App.Vector(0.000000,6.650920,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
sketch.addConstraint(Sketcher.Constraint('PointOnObject',2,2,-2)) 
sketch.addConstraint(Sketcher.Constraint('Horizontal',2)) 

sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,6.650920,0),App.Vector(0.000000,13.922371,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',2,2,3,1)) 
sketch.addConstraint(Sketcher.Constraint('PointOnObject',3,2,-2)) 
# sketch.addConstraint(Sketcher.Constraint('Vertical',3)) 

sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,13.922371,0),App.Vector(29.782467,14.664711,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',3,2,4,1)) 
sketch.addConstraint(Sketcher.Constraint('Horizontal',4)) 

sketch.addGeometry(Part.LineSegment(App.Vector(29.782467,14.664711,0),App.Vector(30.000813,27.547087,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',4,2,5,1)) 
sketch.addConstraint(Sketcher.Constraint('Vertical',5)) 

sketch.addGeometry(Part.LineSegment(App.Vector(30.000813,27.547087,0),App.Vector(48.996853,27.765432,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',5,2,6,1)) 
sketch.addConstraint(Sketcher.Constraint('Horizontal',6))

sketch.addGeometry(Part.LineSegment(App.Vector(48.996853,27.765432,0),App.Vector(49.215199,14.228024,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',6,2,7,1)) 
sketch.addConstraint(Sketcher.Constraint('Vertical',7))

sketch.addGeometry(Part.LineSegment(App.Vector(49.215199,14.228024,0),App.Vector(28.786367,0.000000,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',7,2,8,1)) 
sketch.addConstraint(Sketcher.Constraint('Coincident',8,2,0,1))

# sketch.delConstraint(10)#11
# sketch.delConstraint(2)#3
# 35
# 33
# 31
# 29
# 27
# 25
# 23
# 21

# run depth - kicker depth
sketch.addConstraint(Sketcher.Constraint('Distance',0,1,0,2,12.381088))
# sketch.addConstraint(Sketcher.Constraint('DistanceX',0,2,0,1,12.381088))

# kicker_height
sketch.addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,6.276437))
# sketch.addConstraint(Sketcher.Constraint('Distance',1,1,1,2,6.276437)) 

# kicker_depth
sketch.addConstraint(Sketcher.Constraint('Distance',2,1,2,2,19.517277))
# sketch.addConstraint(Sketcher.Constraint('DistanceX',2,2,2,1,19.517277)) 

# rise_height - kicker_height
sketch.addConstraint(Sketcher.Constraint('Distance',3,1,3,2,7.964808)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceY',3,1,3,2,7.964808)) 


# run_depth
sketch.addConstraint(Sketcher.Constraint('Distance',4,1,4,2,25.252468)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceX',4,1,4,2,25.252468)) 

# rise_height
sketch.addConstraint(Sketcher.Constraint('Distance',5,1,5,2,11.672087)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceY',5,1,5,2,11.672087)) 

# run_depth
sketch.addConstraint(Sketcher.Constraint('Distance',6,1,6,2,23.596853)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceX',6,1,6,2,23.596853)) 


# end rise reverse
sketch.addConstraint(Sketcher.Constraint('Distance',7,1,7,2,14.346976))
# sketch.addConstraint(Sketcher.Constraint('DistanceY',7,2,7,1,14.346976)) 


pad=body.newObject('PartDesign::Pad','Pad')
pad.Profile = (sketch, ['',])
pad.Length = 10
pad.ReferenceAxis = (sketch,['N_Axis'])
sketch.Visibility = False

pad.Length = 9.525000
pad.TaperAngle = 0.000000
pad.UseCustomVector = 0
pad.Direction = (0, 0, 1)
pad.ReferenceAxis = (sketch, ['N_Axis'])
pad.AlongSketchNormal = 1
pad.Type = 0
pad.UpToFace = None
pad.Reversed = 0
pad.Midplane = 0
pad.Offset = 0

sketch.Visibility = False
body.Visibility = True
pad.Visibility = True


doc.recompute()


file_name="stair"
output_folder="output/"
doc_file_name=f"{output_folder}/{file_name}.FCStd"
doc.saveAs(doc_file_name)

__objs__ = []
__objs__.append(body)
import importers.importOBJ

obj_file_name=f"/home/admi/Desktop/projects/freecad-scripting/{output_folder}/{file_name}.obj"
if hasattr(importers.importOBJ, "exportOptions"):
    options = importers.importOBJ.exportOptions(obj_file_name)
    importers.importOBJ.export(__objs__,obj_file_name, options)
else:
    importers.importOBJ.export(__objs__, obj_file_name)

del __objs__


__objs__ = []
__objs__.append(body)
import Mesh
stl_file_name=f"/home/admi/Desktop/projects/freecad-scripting/{output_folder}/{file_name}.stl"
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(stl_file_name)
    Mesh.export(__objs__, stl_file_name, options)
else:
    Mesh.export(__objs__, stl_file_name)

del __objs__


__objs__ = []
__objs__.append(body)

import ImportGui
step_file_name=f"/home/admi/Desktop/projects/freecad-scripting/{output_folder}/{file_name}.step"

if hasattr(ImportGui, "exportOptions"):
    options = ImportGui.exportOptions(step_file_name)
    ImportGui.export(__objs__, step_file_name, options)
else:
    ImportGui.export(__objs__, step_file_name)

del __objs__


