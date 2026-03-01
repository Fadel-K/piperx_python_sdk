#!/usr/bin/env python3
# -*-coding:utf8-*-
# 注意demo无法直接运行，需要pip安装sdk后才能运行
# piper机械臂圆弧模式demo
# 注意机械臂工作空间内不要有障碍
import time
from piper_sdk import *

pose_1 = [277, -270, 235, -90, 10, -125]
pose_2 = [227, 42, 553, -86, 8, -78]
pose_3 = [289, 279, 195, -86, 10, -79]

factor = 1000

pose_1 = [i * factor for i in pose_1]
pose_2 = [i * factor for i in pose_2]
pose_3 = [i * factor for i in pose_3]

if __name__ == "__main__":
    piper = C_PiperInterface_V2("can0", start_sdk_joint_limit=True, start_sdk_gripper_limit=True)
    piper.ConnectPort()
    
    while( not piper.EnablePiper()):
        time.sleep(0.01)
    
    piper.GripperCtrl(0,1000,0x01, 0)
    # 切换至MOVEC模式
    piper.ModeCtrl(0x01, 0x03, 70, 0x00)
    
    # X:135.481
    piper.EndPoseCtrl(*pose_1)
    piper.MoveCAxisUpdateCtrl(0x01)
    time.sleep(0.001)
    
    piper.EndPoseCtrl(*pose_2)
    piper.MoveCAxisUpdateCtrl(0x02)
    time.sleep(0.001)
    
    piper.EndPoseCtrl(*pose_3)
    piper.MoveCAxisUpdateCtrl(0x03)
    time.sleep(0.001)
    
    piper.ModeCtrl(0x01, 0x03, 70, 0x00)
    
    print(piper.GetArmStatus())