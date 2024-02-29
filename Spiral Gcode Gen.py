#Z DATUM IS STOCK TOP
import numpy as np

#USER INPUTS
toolpath_type = "offset"
step_down = 6
tool_dia = 6
passes = 4
xy_feedrate = 4000
z_feedrate = 150
spindle_speed = 22500
min_line_length = 1
max_line_length = 400
z_clearance = 10

#-------------------------------------------------------

step_over = tool_dia//2
passes_complete = 0
current_pos = [max_line_length/2, max_line_length/2, 0]

def write_line_from_position(f, current_pos, xy_feedrate):
    x_coord = current_pos[0]
    y_coord = current_pos[1]
    z_coord = current_pos[2]
    f.write(f"G1 X{x_coord} Y{y_coord} F{xy_feedrate}\n")

def offset_climb_toolpath():
    while passes_complete < passes:
        f.write(f"Z{z_clearance}\n")
        f.write(f"G0 X{max_line_length/2} Y{max_line_length/2}\n")
        current_pos = np.add(current_pos, [0, 0, -step_down])
        f.write(f"G1 Z{current_pos[2]} F{z_feedrate}\n")
        current_pos = [max_line_length/2, max_line_length/2, current_pos[2]]

        for i in range(min_line_length, max_line_length, step_over*2):
            current_pos = np.add(current_pos, [i, 0, 0])
            write_line_from_position(f, current_pos, xy_feedrate)
            current_pos = np.add(current_pos, [0, i, 0])
            write_line_from_position(f, current_pos, xy_feedrate)
            current_pos = np.add(current_pos, [-i - step_over, 0, 0])
            write_line_from_position(f, current_pos, xy_feedrate)
            current_pos = np.add(current_pos, [0, -i - step_over, 0])
            write_line_from_position(f, current_pos, xy_feedrate)
        passes_complete += 1

def offset_climb_toolpath():

def raster_toolpath():

def climb_toolpath():

def conventional_toolpath():

#WRITE GCODE FILE
#CHANGE "USER"
with open ('C:\\Users\\ramiz\\Documents\\Black-Wheel-Test\\Output\\Spiral.gcode','w') as f:
    #GCODE HEADER
    f.write("G17\n")
    f.write("G21\n")
    f.write("G0\n")
    f.write("G90\n") #ABSOLUTE POSITIONING
    f.write("X0 Y0 Z50")
    f.write(f"M3 S{spindle_speed}\n")
    
    

    f.write("Z50 F750\n")
    f.write("M5\n")
    f.write("M2\n")

f.close()