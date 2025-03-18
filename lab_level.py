from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display

def create_lab_level():
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Cell
    cell = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), gp_Pnt(20, 20, 20)).Shape()

    # Hallway
    hallway = BRepPrimAPI_MakeBox(gp_Pnt(20, 5, 0), gp_Pnt(60, 15, 20)).Shape()

    # Lab Room
    lab_room = BRepPrimAPI_MakeBox(gp_Pnt(60, 0, 0), gp_Pnt(100, 40, 20)).Shape()

    # Vent Shaft
    vent = BRepPrimAPI_MakeBox(gp_Pnt(60, 35, 10), gp_Pnt(90, 38, 14)).Shape()

    # Exit Door
    exit_door = BRepPrimAPI_MakeBox(gp_Pnt(95, 15, 0), gp_Pnt(100, 25, 20)).Shape()

    # Computer Terminal (Interactive Object)
    terminal = BRepPrimAPI_MakeBox(gp_Pnt(70, 10, 0), gp_Pnt(75, 15, 10)).Shape()

    # Combine level pieces
    level = BRepAlgoAPI_Fuse(cell, hallway).Shape()
    level = BRepAlgoAPI_Fuse(level, lab_room).Shape()
    level = BRepAlgoAPI_Fuse(level, vent).Shape()
    level = BRepAlgoAPI_Fuse(level, terminal).Shape()

    # Display the level
    display.DisplayShape(level, update=True)
    start_display()

create_lab_level()
