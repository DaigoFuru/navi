from serial import Serial
import time
import RPi.GPIO as GPIO
import math

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO,GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO,fPWM)
    pwm.start(0)
    
def setDirection(direction):
    duty = 2.5 + direction/360*18
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)




P_SERVO = 37
fPWM = 50

Kp=1
Ki=0
Kd=0
SystemOutput = 0
PidOutput = 0
PIDErrADD = 0
ErrBack = 0
TargetAngle = 0

lat=0
lat_last=0
longi=0
longi_last=0
ang=0

setup()




while True:
    ang=ang+5

    lat=10*math.sin(ang)
    longi=ang
    SystemOutput=math.atan((lat-lat_last)/(longi-longi_last))
    print("Out=",SystemOutput)

    Err=TargetAngle-SystemOutput
    KpWork = Kp*Err
    KiWork = Ki*PIDErrADD
    KdWork = Kd*(Err-ErrBack)
    PidOutput=KpWork+KiWork+KdWork
    PIDErrADD+=Err
    ErrBack=Err

    PidOutput=PidOutput/(math.pi/2)
  
    ServoAngle=90+PidOutput*50
    print("Servo",ServoAngle)
    setDirection(ServoAngle)

    lat_last=lat
    longi_last=longi

    time.sleep(0.5)