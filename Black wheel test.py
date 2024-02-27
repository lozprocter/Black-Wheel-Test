#PARAMETER INPUTS
hours = 10


#STATIC PARAMETERS - DO NOT CHANGE
y_distance_mm = 1200
run_time_millis = 5000
milliseconds = (hours*60*60*1000)
run_count = int(milliseconds // run_time_millis)

with open ('C:\\Users\\ramiz\\Documents\\Black-Wheel-Test\\Output\\Black wheel test.gcode','w') as f:
    f.write("G0\n")
    f.write("G91\n")

    print(run_count)

    for i in range (0, (run_count)):
        f.write("Y1200 F6000\n")
        f.write("Y-1200 F6000\n")

f.close()
