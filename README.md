# Ultrasonicmapping-ROS

## Introduction ##
This is an attempt to create 2d map of the surrouinding using Ultrasonic Sensor HC-SR804. 

## Files Description ##
- logfilecreater.py: It collects the ulrasound sensor data and angle data from Arduino using topics '/sensorvalues' and '/angle'. The program subscribes to the ros topics and loggs the data to an .txt file.
- plot_polar.py: It removes the noise in the ultrasound sensor data and plots it in a polar plot. The noise in the data is removed by a process called 'Binning by means'.
- plot_cart.py: It is similar to plot_polar.py except that the ultrasound sensor data is converted to cartesion coordinates (x,y). 
- log.txt: A sample of how the data is logged.
