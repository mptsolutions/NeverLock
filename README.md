# **NeverLock**: The Virtual Drinking Bird
### _A Simple way keep your desktop from going to sleep_

## **Overview**:
**NeverLock** is a [Python](https://www.python.org/) app that keeps your desktop from going to sleep by periodically pressing keys. This effectively disables auto-lock, screensavers, power-save sleep timers, and usually keeps you *active* in chat apps. It is written using Python 3 and requries the [pyautogui](https://pyautogui.readthedocs.io/) package.

## **Basic Setup**:
1) Make sure you have Python 3 setup correctly
2) Clone this repository:
```
git clone https://github.com/mptsolutions/NeverLock.git
```
3) Install ```pyautogui```
```
pip install pyautogui
```

## **Operation** 
The entire app is contained in the single ```never_look.py``` file, so it can be run as any other basic Python script. 
```
D:\PythonProjects\NeverLock> python never_lock.py
```
At specific intervals, NeverLock will press the ```volume down``` key and then the ```volume up``` key.  These keys have been chosen because they work on most systems and ensure that no open applications are affected. You can leave **NeverLock** running even while you are using the computer and it should not have any affect on what you are doing. Note that on some systems a volume adjustment notification will appear on the screen. Once running, **NeverLock** will display its current settings.  Press the ```enter``` key to stop it.
```
**************************************************
*** NeverLock: The Virtual Drinking Bird       ***
**************************************************
*** Click Frequency: 5 minutes.                ***
*** Run Timer: unlimited minutes.              ***
**************************************************
*** Press [enter] to stop.                     ***
**************************************************
```

## **Options**
### Help Menu
The ```-h``` command-line argument can be used to see the available command-line options.
```
D:\PythonProjects\NeverLock> python never_lock.py -h
```
**NeverLock** will not run when the help menu is displayed.
```
*** NeverLock: The Virtual Drinking Bird       ***
**************************************************
*** Usage Options:                             ***
*** -h: Show the help screen.                  ***
*** -f: Set movement frequency (minutes).      ***
*** -t: Set run timer (minutes).               ***
**************************************************
```

### Run Timer
The ```-t``` command-line argument can be used to set the number of minutes for **NeverLock** to run.  
```
D:\PythonProjects\NeverLock> python never_lock.py -t 20
```
When the specified minutes have elapsed, **NeverLock** will quit on its own.  If this argument is not supplied, **NeverLock** will run indefinitely. To stop **NeverLock** before the run timer has run out, use ```ctrl-C```.
```
**************************************************
*** NeverLock: The Virtual Drinking Bird       ***
**************************************************
*** Click Frequency: 5 minutes.                ***
*** Run Timer: 20 minutes.                     ***
**************************************************
```

### Frequency
The ```-f``` command-line argument can be used to set the number of minutes between key-presses. 
```
D:\PythonProjects\NeverLock> python never_lock.py -f 10
```
If this argument is not supplied, **NeverLock** will press keys every 5 minutes.
```
**************************************************
*** NeverLock: The Virtual Drinking Bird       ***
**************************************************
*** Click Frequency: 10 minutes.               ***
*** Run Timer: unlimited minutes.              ***
**************************************************
*** Press [enter] to stop.                     ***
**************************************************
```
