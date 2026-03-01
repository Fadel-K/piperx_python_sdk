#!/usr/bin/env python3
# -*-coding:utf8-*-

import time
from piper_sdk import *

if __name__ == "__main__":
    piper = C_PiperInterface_V2(
        can_name="can0",
        start_sdk_joint_limit=True,
        )
    
    piper.ConnectPort()
    
    while (not piper.EnablePiper()):
        time.sleep(0.01)
        
    piper.ModeCtrl(1, 0x04, 50, 0xAD,)
    
    piper.JointMitCtrl(6, 0, 0, 100, 1.2, 1)
    
    # piper.JointMitCtrl(6, 1.57079633, 0, 100, 1.2, 1)