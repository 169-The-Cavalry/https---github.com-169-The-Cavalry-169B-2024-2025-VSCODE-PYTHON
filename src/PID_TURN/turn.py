
'''from MAIN_GB.main1 import *'''

'''def turn_heading_velocity_momentum(turn_heading_velocity_momentum__heading, turn_heading_velocity_momentum__velocity, turn_heading_velocity_momentum__momentum):
    global message1, forward_move, Back_move, Stop, turn_right, turn, calibrate, stop_initialize, Auto_Stop, turn_left, start_auto, intake_forward, intake_backward, DOon, LB, DOon2, Blue, Red, Intake_Control, Intake_running, myVariable, volocity, Right_Axis, Left_Axis, IntakeStake, Degree, pi, movement, distance1, time1, rot, turn1, LadyBrown_Up, LadyBrown_score, LadyBrown, Right_turn, Left_turn, DriveState, start, Next, dos, tog, error, output, Kp, Ki, Kd, Dellay, Distance_travled, imput, Proportional, integral, derivitive, direction, Previus_error, AutoSelect, X_Start, Y_Start, Y_End, X_End, Angle, Distnce2, Distance2, Turn_Angle, remote_control_code_enabled, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # CURRENT ACCURATE TURN USING IMU
    Inertial21.set_rotation(0, DEGREES)
    if turn_heading_velocity_momentum__heading > Inertial21.rotation(DEGREES):
        while turn_heading_velocity_momentum__heading - turn_heading_velocity_momentum__momentum > Inertial21.rotation(DEGREES):
            RightMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Right_front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Left_Front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightMotors.spin(REVERSE)
            Right_front.spin(REVERSE)
            LeftMotors.spin(REVERSE)
            Left_Front.spin(REVERSE)
            wait(5, MSEC)
    else:
        while turn_heading_velocity_momentum__heading + turn_heading_velocity_momentum__momentum < Inertial21.rotation(DEGREES):
            RightMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Right_front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftMotors.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            Left_Front.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightMotors.spin(FORWARD)
            Right_front.spin(FORWARD)
            LeftMotors.spin(FORWARD)
            Left_Front.spin(FORWARD)
            wait(5, MSEC)
    RightMotors.stop()
    LeftMotors.stop()
    Right_front.stop()
    Left_Front.stop()
    turn1 = 1'''