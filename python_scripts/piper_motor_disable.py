import time
from piper_sdk import *

if __name__ == "__main__":
    piper = C_PiperInterface_V2()
    piper.ConnectPort()
    time.sleep(0.1)
    
    while( not piper.EnablePiper()):
        time.sleep(0.01)
        
    piper.ModeCtrl(0x01, 0x01, 30, 0x00)
    piper.JointCtrl(0, 0, 0, 0, 0, 0)
    piper.GripperCtrl(0, 1000, 0x01, 0)
    
    motor_num = int(input("Motor number: "))
    
    piper.DisableArm(motor_num)
    print(f"Info: Motor {motor_num} disabled successfully")
    
    if (input("Press 'z' to zero this joint at this position")=='z'):
        piper.JointConfig(motor_num, 0xAE)
        piper.EnableArm(motor_num)