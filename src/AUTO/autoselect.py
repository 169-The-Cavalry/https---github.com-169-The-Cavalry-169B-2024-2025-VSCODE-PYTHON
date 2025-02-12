

def when_started5():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # ---------------------------------------------------------------------------------------------------------------------------------------------------AUTONOMOUS SELECTOR-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    AutoSelect = 0
    while True:
        if AutoSelect == 1:
            controller_1.screen.set_cursor(1, 1)
            AutoSelect = 1
            controller_1.screen.print("RED LEFT RING")
        else:
            if AutoSelect == 2:
                controller_1.screen.set_cursor(1, 1)
                AutoSelect = 2
                controller_1.screen.print("BLUE RIGHT RING")
            else:
                if AutoSelect == 3:
                    controller_1.screen.set_cursor(1, 1)
                    AutoSelect = 3
                    controller_1.screen.print("RED RIGHT STAKE")
                else:
                    if AutoSelect == 4:
                        controller_1.screen.set_cursor(1, 1)
                        AutoSelect = 4
                        controller_1.screen.print("BLUE LEFT STAKE")
                    else:
                        controller_1.screen.clear_screen()
                        controller_1.screen.set_cursor(1, 1)
                        AutoSelect = 0
                        controller_1.screen.print("NO AUTO")
        wait(5, MSEC)

def onevent_controller_1buttonL1_pressed_0():
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    controller_1.screen.clear_screen()
    if AutoSelect == 5:
        AutoSelect = 0
    AutoSelect = AutoSelect + 1
    controller_1.rumble("-.-.")
