------------------------------------
 Rose Lab Worm Motion Data Analysis
------------------------------------
 Author - Joshua Ketterl
 Contact - jketterl@gmail.com
 Last Modified - 5/15/2018

 Use of this code constitutes agreement to the FreeBSD software license 
 https://en.wikipedia.org/wiki/FreeBSD_Documentation_License

--------------
 Instructions
--------------
 1) Remove all files you do not want evaluated from Input folder

 2) Place files to evaluate in the Input Folder. They must all have the same fps to get accurate data

 3) Open up jupyter lab by opening a command prompt and typing "jupyter lab". Info about jupyter lab here: http://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html

4) Open "JoshuaScript.ipynb" in jupyter lab

 5) Set fps, seconds, and output_name accordingly in config section of code, near the top
	- fps represents the setting on the microscope when the video was taken
	- seconds is the number of seconds of video to evaluate

 6) Run script in Jupyter lab by selecting the code and pressing Shift+Enter. Excel files will output to the JoshuaScript folder.



-----------------------
 Common / Known Issues
-----------------------
 1) The seconds / fps values are incorrect. Will not crash but data will be inaccurate

 2) a file exists in Input folder which does not have the 'features_timeseries' attribute

 3) permission error - The excel file the script is trying to write to is open or otherwise being used by another application

 4) Table headers in output are centered in their cells and go off screen, but this shouldn't affect visualization