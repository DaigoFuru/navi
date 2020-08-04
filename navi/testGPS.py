from serial import Serial
from micropyGPS import MicropyGPS
import threading
import time
import csv

gps = MicropyGPS(9, 'dd')                          #generate MicropyGPS object
def rungps():                                      #read from GPS module and refresh gps object
    s = Serial('/dev/serial0', 9600, timeout=10)
    s.readline()
    while True:
        sentence = s.readline().decode('utf-8')    #read GPS data and transform it into string
        if sentence[0] != '$':                     #ignore it if the first character isn't '$'
        	continue
        for x in sentence:
        	gps.update(x)

gpsthread = threading.Thread(target=rungps, args=()) #run the parameter and generate thread
gpsthread.daemon = True
gpsthread.start()                                  #start thread

gps.start_logging('GPSlog.txt')
try:
	while True:
    		if gps.clean_sentences > 20:
        		h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        		print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        		print('latitude: %2.8f, longitude: %2.8f' % (gps.latitude[0], gps.longitude[0]))
        		print('altitude: %f' % gps.altitude)
			#with open('GPSdata.csv', 'a+')as f:
				#gps=['latitude', gps.latitude[0], 'longitude', gps.longitude[0]]
				#f_csv = csv.writer(f)
				#f_csv.writerow(gps)
		time.sleep(2.0)                                #output the data every 2 seconds
except KeyboardInterrupt:
	gps.stop_logging()
