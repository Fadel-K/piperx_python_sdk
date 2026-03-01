
#!/usr/bin/env python3
# -*-coding:utf8-*-

import time
from piper_sdk import *

pose = [0, 90, -90, 90, 0, 90]

pose = [0, 0, 0, 0, 0, 0]

gripper_angle = 53

factor = 1000

if __name__ == "__main__":
    piper = C_PiperInterface_V2(
        can_name="can0",
        judge_flag=True,
        dh_is_offset=1,
        start_sdk_joint_limit=False,
        start_sdk_gripper_limit=False
        )
    
    piper.ConnectPort()
    
    piper.ModeCtrl(ctrl_mode=0x01, move_mode=0x01, move_spd_rate_ctrl=100, is_mit_mode=0x00)
    
    while (not piper.EnablePiper()):
        piper.EnableArm()
        time.sleep(0.01)
    
    print("Enabled Piper")
    
    piper.JointCtrl(pose[0]*factor, pose[1]*factor, pose[2]*factor, pose[3]*factor, pose[4]*factor, pose[5]*factor)
    piper.GripperCtrl(gripper_angle*factor, 1000, 0x01, 0x00)
    
    print("5", piper.GetArmStatus())