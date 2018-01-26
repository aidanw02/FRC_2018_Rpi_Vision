# RaspberryPi_Vision_2018
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

10. Had to run “sudo make install” instead of “make install”

11. Command is not “site-packages” it is “dist-packages”

12. Removed python2.7 from Raspbery Pi

13. Installed pynetworktables on Pi

14. Update & upgraded Raspberry Pi

16. Read image to computer with win32DiskImager

STEP 3. Get pynetworktables working 
17. Setup Robrio with latest Image  note:The Roborio image and Robotpy versions have to match

18. Installed RobotPy on Roborio [These insructions](http://robotpy.readthedocs.io/en/stable/install/robot.html#install-robotpy)    
note: Pynetworktables is included in the Robotpy install

19. Installed pyfrc with pip3 on Rpi   note: Pynetworktables is included in the pyfrc install

20. Used the example code to test the connection between the Rpi and Roborio on our local network

21. Connected Rpi and Roborio to FRC radio via ethernet cable

22. Conected to the FRC radio from windows machine and ssh into the Rpi 

24. Created a bash file on the Rpi to scan the network and find the Roborio’s ip address or vice versa

26. Made V3 opencv rpi image

STEP 4. Stream camera feed from raspberry pi to dash board
27.Install cscore on raspberry pi 

28. Installed smartdashboard on DS

29. Used example code to stream two camera streams to the dashboard

30. Used our own code to stream three camera feeds to the dash board. One view with stationary line added using opencv
