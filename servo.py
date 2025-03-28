'''
-This module allows creation of robot objects for 2 or 4 wheeled robots.
-The motor driver used is the L298n.
-The base package used is the Rpi GPIO
-The Object Motor needs to be created first
-Then the move() function can be called to operate the motors
 move(speed,turn,delay)
-Speed and turn range from -1 to 1
-Delay is in seconds.
'''



'''


Core Functionality

    Steering Control (-0.5 to +0.5)

        Left Turn: Press LEFT arrow → Steering increases to +0.5 (gradual, +0.02/frame).

        Right Turn: Press RIGHT arrow → Steering decreases to -0.5.

        Auto-Centering: Releases → Smoothly decays to 0 (multiplied by 0.9/frame).

    Throttle Control

        Forward: UP arrow → Throttle +0.5 (50% max speed).

        Reverse: DOWN arrow → Throttle -0.25 (25% max speed).

        Stop: SPACE → Resets throttle and steering to 0.

    Data Collection

        Logs steering, throttle, and Pixy2 line vectors to a CSV file for training.


'''

'''
PWM Frequency: 200 Hz (adjustable in GPIO.PWM setup).

Direction Control: Uses In1/In2 pins to set motor polarity.


'''






#max_pwm=200
#class servo():
    #def __init__(self,EnaA):

        #self.pwm= GPIO.PWM(self.EnaA, max_pwm);
        #self.pwm.start(0);
        #self.mySpeed=0

    #def move(self,speed=0.4,turn=0,t=0):
        #base_pwm =50
        #current_steering_angle=turn*70
        #desired_steering_angle=
        #Speed = base_pwm-kp*(desired_steering_angle-current_steering_angle)
        # Speed = base_pwm+kp*(desired_steering_angle-current_steering_angle)


#if Speed>200: Speed =200
        #elif Speed<-200: Speed = -200

        #self.pwmChangeDutyCycle(abs(Speed))


    #def stop(self,t=0):
        #self.pwm.ChangeDutyCycle(0);
        #self.pwm.ChangeDutyCycle(0);
        #self.mySpeed=0
        #sleep(t)

#def main():
    #servo.move(0.5,0,2)
    #servo.stop(2)

#if __name__ == '__main__':
    #servo=servo()
    #main()