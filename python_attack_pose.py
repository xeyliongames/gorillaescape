from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeSphere
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Ax1
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Display.SimpleGui import init_display

def attack_pose():
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Basic body and limbs
    torso = BRepPrimAPI_MakeCylinder(10, 40).Shape()
    head = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 50), 8).Shape()
    arm = BRepPrimAPI_MakeCylinder(gp_Pnt(-15, 0, 30), 3, 25).Shape()

    # Pole weapon
    pole = BRepPrimAPI_MakeCylinder(gp_Pnt(0, 10, 30), 2, 60).Shape()
    
    # Rotate the pole for a horizontal strike
    trsf = gp_Trsf()
    trsf.SetRotation(gp_Ax1(gp_Pnt(0, 10, 30), gp_Pnt(1, 0, 0)), 1.57)
    rotated_pole = BRepBuilderAPI_Transform(pole, trsf).Shape()

    # Combine shapes
    body = torso
    body = BRepBuilderAPI_Transform(body, trsf).Shape()
    body = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 50), 8).Shape()
    
    # Show the pose
    display.DisplayShape(body, update=True)
    display.DisplayShape(rotated_pole, update=True)
    start_display()

attack_pose()
