#PARAMETER INPUTS
test_time_hours = 10
y_distance_mm = 1200 #MM
feedrate = 6000 #METRES/MIN
acceleration = 130 #MM/SECOND^2

#CALCS
feedrate_mms = feedrate/60

#ACCELERATION SECTION CALCULATOR
acceleration_time_seconds = feedrate_mms / acceleration
accel_and_deccel_sum_time_seconds = (acceleration_time_seconds*2)
acceleration_distance_mm = (acceleration_time_seconds/2)*(feedrate_mms)
accel_and_deccel_sum_distance_mm = (acceleration_distance_mm*2)

#CONSTANT VELOCITY SECTION CALCULATOR
constvel_distance_mm = y_distance_mm - accel_and_deccel_sum_distance_mm
constvel_time_seconds = constvel_distance_mm/feedrate_mms

#RUN COUNT CALCULATOR
run_time_seconds = (constvel_time_seconds + accel_and_deccel_sum_time_seconds)
print(run_time_seconds)
run_time_milliseconds = run_time_seconds*1000
test_time_milliseconds = test_time_hours*60*60*1000
run_count = int(test_time_milliseconds // run_time_milliseconds)
print(run_count)

#WRITE GCODE FILE
#CHANGE "USER"
with open ('C:\\Users\\USER\\Documents\\Black-Wheel-Test\\Output\\Black wheel test.gcode','w') as f:
    f.write("G0\n")
    f.write("G91\n")

    for i in range (0, (run_count)):
        f.write("Y1200 F6000\n")
        f.write("Y-1200 F6000\n")

f.close()