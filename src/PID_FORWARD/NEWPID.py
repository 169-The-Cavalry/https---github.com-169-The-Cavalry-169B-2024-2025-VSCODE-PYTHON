'''import math
import time

# Initialize PID variables
kp = 0.1  # Proportional gain
ki = 0.0  # Integral gain
kd = 0.0  # Derivative gain
error_sum = 0  # Error sum for integral term
previous_error = 0  # Previous error for derivative term


def pid_controller():
    global kp, ki, kd, error_sum, previous_error

    # Calculate error
    current_distance = ((math.fabs(Right_front.position(DEGREES)) / 360) * (2.75 * pi) + ((math.fabs(Left_Front.position(DEGREES)) / 360) * (2.75 * pi) + ((math.fabs(RightMotors.position(DEGREES)) / 360) * (2.75 * pi) + (math.fabs(LeftMotors.position(DEGREES)) / 360) * (2.75 * pi)))) / 4
    error = target_distance - current_distance

    # Calculate PID terms
    proportional_term = kp * error
    integral_term = ki * error_sum
    derivative_term = kd * (error - previous_error)
    previous_error = error

    # Update error sum
    error_sum += error

    # Calculate motor speed
    motor_speed = max_speed * (proportional_term + integral_term + derivative_term)
    motor.set_velocity(motor_speed, vex.MEDIUM)

    # Update PID gains
    if error < 0.1:
        kp += 0.01
        ki += 0.001
        kd += 0.001
    elif error > 0.1:
        kp -= 0.01
        ki -= 0.001
        kd -= 0.001

    # Print PID gains and error
    print(f"KP: {kp}, KI: {ki}, KD: {kd}, Error: {error}")

while True:
    pid_controller()
    time.sleep(0.1)  # Adjust this value to change the PID update rate'''