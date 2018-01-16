# RaspberryPi_Vision_2018
Code for raspberry pi running python and grip to do vision processing

The steps I followed are listed below.


STEP 1. Install and setup of raspbian lite
1. Installed Raspbian stretch light
2. Changed password, hostname, memory split to 16
3. Enable SSH, and I2c
4. Setup networks on lite. had to copy files from old raspberry pi sd. 
5. Connect via SSH and putty
6. Update and upgrade everything-----
STEP 2.  Install opencv
7. Follow  www.pyimagesearch.com to install opencv, and python3
8.  Just finished numpy install. On step #5
9. Continue setting up opencv on Raspberry Pi. just about to start step 6. 
10. Had to run “sudo make install” instead of “make install”
11. Command is not “site-packages” it is “dist-packages”
12. Removed python2.7 from Raspbery Pi
13. Installed pynetworktables on Pi
14. Update & upgraded Raspberry Pi
15. Finished opencv install guide successfully 
16. Read image to computer with win32DiskImager-----
STEP 3. Get pynetworktables working
17. Setup Robrio with latest Image  note:The Roborio image and Robotpy versions have to match
18. Installed RobotPy on Roborio [These insructions](http://robotpy.readthedocs.io/en/stable/install/robot.html#install-robotpy)    note: Pynetworktables is included in the Robotpy install
19. Installed pyfrc with pip3 on Rpi   note: Pynetworktables is included in the pyfrc install
20. Used the example code to test the connection between the Rpi and Roborio on our local network
21. Connected Rpi and Roborio to FRC radio via ethernet cable
22. Conected to the FRC radio from windows machine and ssh into the Rpi 
23. Gave the Rpi a static ip using Method 2 of these instructions note:We reverted back to an DHCP assigned address. Static IP was giving us errors.
24. Created a bash file on the Rpi to 
25. scan the network and find the Roborio’s ip address
26. Made V3 opencv rpi image
