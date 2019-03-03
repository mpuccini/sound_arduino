import sys, serial
import numpy
import matplotlib.pyplot as plt
import pandas as pd
from drawnow import *


temperatureC = []
tempScale = numpy.arange(-10,150,0.5)
soundspeed = []
thl_soundspeed = []
## Here you have to looking for which serial is used by arduino by typing:
## ls /dev/serial/by-id | grep arduino
## ser = serial.Serial("/dev/ttyAMC0",9600)
ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_55739323637351C0D1C2-if00', 9600)

plt.ion()
cnt=0

def makeFig():
  plt.ylim(320, 380)
  plt.xlim(15,50)
  plt.title('Sound speed vs. temperature')
  plt.grid(True)
  plt.xlabel('Temperature (°C)')
  plt.ylabel('Sound speed (m/s)')
  plt.plot(tempScale, 331.3*(1+tempScale/273.15)**0.5, 'g--', label='Theory')
  plt.plot(temperatureC, soundspeed, 'ro', label='Measured')
  plt.plot(temperatureC, thl_soundspeed, 'bo', label='Th. linear')
  plt.legend()

while True:
  while (ser.inWaiting()==0):
    pass
  arduinoString = ser.readline()
  arduinoString = str(arduinoString, 'utf-8')
  arduinoString = arduinoString.replace("\r\n","")
  dataArray = arduinoString.split(' ')
  if (len(dataArray)==2):
    temp = float( dataArray[0])
    sspeed = float( dataArray[1])
    temperatureC.append(temp)
    soundspeed.append(sspeed)
    thl_soundspeed.append(331.3 + 0.606*temp)
    drawnow(makeFig)
    plt.pause(.000001)
    cnt=cnt+1
  else:
    pass
  if (len(temperatureC) > 11):
    if (abs(temperatureC[-1]-temperatureC[-10])/temperatureC[-1] < .01):
      df = pd.DataFrame({'temperature':temperatureC, 'soundspeed': soundspeed})
      df.to_csv('data.csv', index=False)
      plt.savefig('tempVSsoundspeed.pdf')
      plt.close()
      break
  else:
    pass
