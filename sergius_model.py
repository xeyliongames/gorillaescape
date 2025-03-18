from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display

def create_sergius():
    # Initialize the display
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Create the head of the figure
    head = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 60), 12).Shape()

    # Create the torso of the figure
    torso = BRepPrimAPI_MakeCylinder(20, 40).Shape()

    # Create the left arm
    left_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-25, 0, 30), gp_Dir(1, 0, 0)), 6, 30).Shape()

    # Create the right arm
    right_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(25, 0, 30), gp_Dir(1, 0, 0)), 6, 30).Shape()

    # Create the left leg
    left_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-10, 0, 0), gp_Dir(0, 0, 1)), 8, 40).Shape()

    # Create the right leg
    right_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(10, 0, 0), gp_Dir(0, 0, 1)), 8, 40).Shape()

    # Create the pole weapon
    pole = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(0, 40, 30), gp_Dir(0, 1, 0)), 2, 60).Shape()

    # Combine shapes to form the body
    body = BRepAlgoAPI_Fuse(torso, head).Shape()
    body = BRepAlgoAPI_Fuse(body, left_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, right_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, left_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, right_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, pole).Shape()

    # Display the complete model
    display.DisplayShape(body, update=True)

    # Start the display loop
    start_display()

# Execute the function to create and display the figure
create_sergius()