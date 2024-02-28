#USER INPUTS
step_down = 6
tool_dia = 6
passes = 2
min_line_length = 5
max_line_length = 50

#-------------------------------------------------------

step_over = tool_dia//2
passes_complete = 0


#WRITE GCODE FILE
#CHANGE "USER"
with open ('C:\\Users\\USER\\Documents\\Black-Wheel-Test\\Output\\Spiral.gcode','w') as f:
    f.write("G0\n")
    f.write("G90\n")
    f.write("X0 Y0 Z5\n")
    f.write("G0\n")
    f.write("G91\n")
    f.write("Z-5\n")

    while passes_complete < passes:
        f.write(f"Z-{step_down}\n")
        for i in range(min_line_length, max_line_length, step_over*2):
            f.write(f"X{i} F6000\n")
            f.write(f"Y{i} F6000\n")
            f.write(f"X-{i+step_over} F6000\n")
            f.write(f"Y-{i+step_over} F6000\n")
        passes_complete += 1

f.close()