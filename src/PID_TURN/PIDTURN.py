

def angle_diff(target, current):
    """
    Computes the shortest (signed) difference between two angles.
    Returns a value between -180 and 180 degrees.
    """
    diff = (target - current + 180) % 360 - 180
    return diff

def pid_turn(degreeChange, max_velocity,timeout=3.0):
    """
    Performs an in-place turn by a relative amount of 'degreeChange' degrees.
    Uses an optimized PID loop with velocity control.
    """

    # Get the current heading and compute the target heading (normalized to 0–359°)
    currentHeading = Inertial21.rotation() % 360
    targetHeading = (currentHeading + degreeChange) % 360

    # ------------------------------
    # PID Tuning Constants
    kP = 0.06
    kI = 0.001
    kD = 0.15
    # ------------------------------

    integral = 0.0
    dt = 0.02           # Loop time (20 ms)
    tolerance = 0.8     # Very precise stopping error in degrees
  # Max motor velocity (percent)
    min_velocity = 15   # Prevents stalling
    ramp_time = 0.5     # Acceleration time in seconds

    start_time = brain.timer.time(SECONDS)

    # Velocity ramp-up
    current_velocity = min_velocity
    velocity_step = (max_velocity - min_velocity) / (ramp_time / dt)

    while True:
        # Read current heading from the IMU
        currentHeading = Inertial21.rotation() % 360

        # Compute error (shortest angle difference)
        error = angle_diff(targetHeading, currentHeading)
        if abs(error) < tolerance:
            break

        # Use the IMU’s angular velocity for the derivative term
        angular_velocity = Inertial21.gyro_rate(XAXIS, VelocityUnits.DPS)
        derivative = -angular_velocity  # IMU gives direct angular velocity

        # Accumulate error for the integral term
        integral += error * dt

        # Compute PID output as velocity
        pid_output = kP * error + kI * integral + kD * derivative

        # Adaptive velocity control: Prevents robot from stalling at low speed
        if abs(pid_output) < min_velocity:
            pid_output = min_velocity * (1 if pid_output > 0 else -1)

        # Velocity ramp-up for smoother acceleration
        if abs(pid_output) > current_velocity:
            current_velocity += velocity_step
        else:
            current_velocity = abs(pid_output)

        # Clamp the velocity
        if current_velocity > max_velocity:
            current_velocity = max_velocity

        # Apply velocity to motors (turning in place)
        LeftMotors.set_velocity(current_velocity, PERCENT)
        Left_Front.set_velocity(current_velocity, PERCENT)
        RightMotors.set_velocity(current_velocity, PERCENT)
        Right_front.set_velocity(current_velocity, PERCENT)

        # Spin the motors
        LeftMotors.spin(FORWARD)
        Left_Front.spin(FORWARD)
        RightMotors.spin(FORWARD)
        Right_front.spin(FORWARD)

        # Timeout condition
        if brain.timer.time(SECONDS) - start_time > timeout:
            break

    # Stop all drive motors
    LeftMotors.stop()
    Left_Front.stop()
    RightMotors.stop()
    Right_front.stop()
