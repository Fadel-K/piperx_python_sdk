#!/usr/bin/env python3
# -*-coding:utf8-*-

import time
from piper_sdk import *

pose_1 = [355, 0, 235, -180, 0, -90, 53]
pose_2 = [265, 0, 466, -85, 0, -90, 0]

factor = 1000

if __name__ == "__main__":
    piper = C_PiperInterface_V2(
        can_name="can0",
        start_sdk_joint_limit=True,
        )
    
    piper.ConnectPort()
    
    while (not piper.EnablePiper()):
        time.sleep(0.01)
    
    print("Enabled Piper")
        
    time.sleep(0.01)
            
    # print("1", piper.GetArmStatus())
    count = 0
    
    while count < 2:
        X = round(pose_2[0]*factor)
        Y = round(pose_2[1]*factor)
        Z = round(pose_2[2]*factor)
        RX = round(pose_2[3]*factor)
        RY = round(pose_2[4]*factor)
        RZ = round(pose_2[5]*factor)
        joint_6 = round(pose_2[6]*factor)

        piper.ModeCtrl(0x01, 0x00, 100, 0x00)
        piper.EndPoseCtrl(X,Y,Z,RX,RY,RZ)
        time.sleep(0.2)
        count +=1
        print(count)
    
    print("Started main loop")
    
    while True:
        # print("1", piper.GetArmStatus())
        X = round(pose_1[0]*factor)
        Y = round(pose_1[1]*factor)
        Z = round(pose_1[2]*factor)
        RX = round(pose_1[3]*factor)
        RY = round(pose_1[4]*factor)
        RZ = round(pose_1[5]*factor)
        joint_6 = round(pose_1[6]*factor)
    
        piper.ModeCtrl(0x01, 0x00, 100, 0x00)
        piper.EndPoseCtrl(X,Y,Z,RX,RY,RZ)
        
        piper.GripperCtrl(abs(joint_6), 1000, 0x01, 0)
        
        time.sleep(0.01)
        