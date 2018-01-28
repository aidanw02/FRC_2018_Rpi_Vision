# FRC_2018_Rpi_Vision
Code for raspberry pi running python and grip to do vision processing

"""Please note that this code is in a early development stage and not yet complete!""" 

The steps I followed are listed below.


STEP 1. Install and setup of raspbian lite
1. Installed Raspbian stretch light

2. Changed password, hostname, memory split to 16

3. Enable SSH

4. Setup networks on lite.

5. Connect via SSH and putty

6. Update and upgrade everything

STEP 2. Install opencv
7. Follow  www.pyimagesearch.com to install opencv, and python3 

8. Had to run “sudo make install” instead of “make install”

9. Command is not “site-packages” it is “dist-packages”

 10. Removed python2.7 from Raspbery Pi

 11. Installed pynetworktables on Pi

 12. Update & upgraded Raspberry Pi

 13. Read image to computer with win32DiskImager

STEP 3. Get pynetworktables working 


 14. Setup Robrio with latest Image  note:The Roborio image and Robotpy versions have to match

 15. Installed RobotPy on Roborio [These insructions](http://robotpy.readthedocs.io/en/stable/install/robot.html#install-robotpy)    
 note: Pynetworktables is included in the Robotpy install

 16. Installed pyfrc with pip3 on Rpi   note: Pynetworktables is included in the pyfrc install

 17. Used the example code to test the connection between the Rpi and Roborio on our local network

 18. Connected Rpi and Roborio to FRC radio via ethernet cable

 19. Conected to the FRC radio from windows machine and ssh into the Rpi 

 20. Created a bash file on the Rpi to scan the network and find the Roborio’s ip address or vice versa

 21. Made V3 opencv rpi image

STEP 4. Stream camera feed from raspberry pi to dash board
 22.Install cscore on raspberry pi 

 23. Installed smartdashboard on DS

 24. Used example code to stream two camera streams to the dashboard

 25. Used our own code to stream three camera feeds to the dash board. One view with stationary line added using opencv
     note: Our code is listed above
