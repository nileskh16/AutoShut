# AutoShut
The automated python script to shut the PC down and practically stop working for that office day.

1. The drive.py files simply runs in the background lurking behind many processes and checks the current the current  time and if time exceeds or crosses over the predefined time then BOOM!!!! it shuts down computer with comprehensive message for the user. 
2. As the script is called from control.bat file the file should be stored in the sam directory as the python script.
3. auto.vs script file triggers the control.bat file on sytem boot up and start up and revives the script to check the current time.
As, the auto.vbs file is supposed to automaticcaly start on start up you have to manipulate some configuration by creating a shortcut in the C:\Users\<User_Name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup folder.
