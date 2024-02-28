#PARAMETER INPUTS
test_time_hours = 10
axis = "Y"
travel_distance_mm = 1200 #UNIT IS MM
feedrate = 6000 #UNIT IS METRES/MIN - MAXIMUMS ARE X = 8000, Y = 6000, Z = 150

#CALCS
acceleration = 0
feedrate_mms = feedrate/60
if axis == "X" or axis == "x" or axis == "Y" or axis == "y":
    acceleration = 130
elif axis == "Z" or axis == "z":
    acceleration = 200
else:
    print("AXIS DOES NOT EXIST")
    exit()

#ACCELERATION SECTION CALCULATOR
acceleration_time_seconds = feedrate_mms / acceleration
accel_and_deccel_sum_time_seconds = (acceleration_time_seconds*2)
acceleration_distance_mm = (acceleration_time_seconds/2)*(feedrate_mms)
accel_and_deccel_sum_distance_mm = (acceleration_distance_mm*2)

#CONSTANT VELOCITY SECTION CALCULATOR
constvel_distance_mm = travel_distance_mm - accel_and_deccel_sum_distance_mm
constvel_time_seconds = constvel_distance_mm/feedrate_mms

#RUN COUNT CALCULATOR
run_time_seconds = (constvel_time_seconds + accel_and_deccel_sum_time_seconds)*2 #X2 FOR A THERE AND BACK RUN
print(run_time_seconds)
test_time_seconds = test_time_hours*60*60
run_count = int(test_time_seconds // run_time_seconds)
print(run_count)

#WRITE GCODE FILE
#CHANGE "USER"
with open ('C:\\Users\\USER\\Documents\\Black-Wheel-Test\\Output\\Black wheel test.gcode','w') as f:
    f.write("G0\n")
    f.write("G91\n")

    for i in range (0, (run_count)):
        f.write(f"{axis}{travel_distance_mm} F{feedrate}\n")
        f.write(f"{axis}-{travel_distance_mm} F{feedrate}\n")

f.close()