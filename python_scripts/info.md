// Press ctrl shift v for view

# EVERYTHING IN THIS FILE IS OBSERVATIONAL AND NOT CONFIRMED INFORMATION AND CAN BE WRONG

# Arm Joint Angle Limits (Self-calculated max)

J1 - [-155172, 154645]
J2 - [-3699, 194137]
J3 - [-175610, 575]
J4 - [-92607 , 87138]
J5 - [-101058, 90319]
J6 - [8160, 240817]

Gripper (J7) - [1000, 101700]

# Arm joint Angle Limits (Given by Software)

ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 1
  max_angle_limit: 1500
  min_angle_limit: -1500
  max_joint_spd: 300
)
ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 2
  max_angle_limit: 1800
  min_angle_limit: 0
  max_joint_spd: 300
)
ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 3
  max_angle_limit: 0
  min_angle_limit: -1700
  max_joint_spd: 300
)
ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 4
  max_angle_limit: 890 (I think max 865)
  min_angle_limit: -890
  max_joint_spd: 300
)
ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 5
  max_angle_limit: 890
  min_angle_limit: -890
  max_joint_spd: 300
)
ArmMsgFeedbackCurrentMotorAngleLimitMaxSpd(
  motor_num: 6
  max_angle_limit: 1800 (I think 235)
  min_angle_limit: -1800 (I think 810)
  max_joint_spd: 300
)


# POSES
  
## POSE 1 (RANDOM)

### Joint control

Joint 1:-5347
Joint 2:100854
Joint 3:-81462
Joint 4:80352
Joint 5:-5532
Joint 6:119481
grippers_angle: 53100, 53.100

### TCP control

X_axis : 355483
Y_axis : 0
Z_axis : 235183
RX_axis : -179870
RY_axis : -354
RZ_axis : 160001
grippers_angle: 53100, 53.100

# Movement modes
## Mode 0 (P Mode)

It is a position mode that expects continous position controls like a servo / continous position control.
Needs atleast 2 commands for it to act.
Can be delayed / not work if the reverse IK is not clear

## Mode 1 (J Mode)

It is a simple move joint to specific angle program, will always (as long as angle is within limit) work instantly

## Mode 2 (L Mode)

It uses gripper position to move it in a straight line (if possible). It is slower than mode 0, and doesn't need continous control. It will execute command and then wait.


## Mode 3 (C Mode)

It uses gripper position to move it in a straight line (if possible). It is slower than mode 0, and doesn't need continous control. It will execute command and then wait.