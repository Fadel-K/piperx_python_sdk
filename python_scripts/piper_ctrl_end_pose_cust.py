#!/usr/bin/env python3
# -*-coding:utf8-*-

import time
from piper_sdk import *

pose = [355, 0, 235, -180, 0, 160]
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
    
    while (not piper.EnablePiper()):
        piper.EnableArm()
        time.sleep(0.01)
    
    
    print("Enabled Piper")
        
    # time.sleep(0.01)
    
    piper.ModeCtrl(0x01, 0x00, 50, 0x00)
    
    while True:
        print("1", piper.GetArmStatus())
        print("3", piper.EndPoseCtrl(pose[0]*factor, pose[1]*factor, pose[2]*factor, pose[3]*factor, pose[4]*factor, pose[5]*factor))
    
        print("4", piper.GripperCtrl(gripper_angle*factor, 1000, 0x01, 0x00))
        
        time.sleep(0.01)
        