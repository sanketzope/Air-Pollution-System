import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

a=[]
str1=str(ser.readline())
a=str1.split(",")
Temperature=a[0]
Humidity=a[1]
Airquality=a[2]

Temperature=Temperature[4:]
Humidity=Humidity[3:]
Airquality=Airquality[3:][:-5]

while res:
     cc=str(1234)
     print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://airpollution-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
     
     for i in range(0,4):
             string2="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data1 =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':Airquality,
               'time': datetime.now().strftime("%H:%M")               
          }
             result1 = firebase1.patch('https://airpollution-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app/'+ '/Air quality_data/'+ str(i), data1)
             print(result1)
             
     for i in range(0,4):
             string2="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data1 =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':Humidity,
               'time': datetime.now().strftime("%H:%M")               
          }
             result1 = firebase1.patch('https://airpollution-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app/'+ '/Humidity_data/'+ str(i), data1)
             print(result1)        
             
     for i in range(0,4):
             string1="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':Temperature,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://airpollution-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app/'+ '/Temperature_data/'+ str(i), data)
             print(result)
     

     
     res=0


