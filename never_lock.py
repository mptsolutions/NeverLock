import sys, getopt
import pyautogui
import _thread
from time import sleep

"""
NeverLock: The Virtual Drinking Bird
------------------------------------
NeverLock is a Python app that keeps your desktop from going to 
sleep by periodically pressing keys. This effectively disables 
auto-lock, screensavers, power-save sleep timers, and usually 
keeps you active in chat apps. It is written using Python 3 and 
requries the pyautogui package. For more information see the 
documentation as https://github.com/mptsolutions/NeverLock
"""
class NeverLock:
    def __init__(self, run_options):
        """
        Initialization of the class will attempt to get command-line
        arguments and then start the the key_press function in a new
        thread.
        """
        self.parse_args(run_options)
        if self.help:
            self.display_help()
        else:
            self.display_info()
            _thread.start_new_thread(self.key_press, ())
            if self.stop_timer_minutes != 'unlimited':
                print('')
                sleep(int(self.stop_timer_minutes)*60)
            else:
                self.display_stop()
                input()
            self.display_finished()

    def parse_args(self, options):
        """
        Function to parse command-line arguments.
        """
        self.move_frequency_minutes = 5
        self.stop_timer_minutes = 'unlimited'
        self.help = False
        opts, _ = getopt.getopt(options,"hf:t:")
        for opt, arg in opts:
            if opt == '-f':
                self.move_frequency_minutes = arg
            if opt == '-t':
                self.stop_timer_minutes = arg
            if opt == '-h':
                self.help = True

    def key_press(self):
        """
        Function to press keys at specified intervals
        """
        pyautogui.FAILSAFE = True
        try:
            while True:
                pyautogui.press('volumedown')
                pyautogui.press('volumeup')
                sleep(int(self.move_frequency_minutes)*60)
        except KeyboardInterrupt:
            pass

    def display_title(self):
        """
        Function to display main title
        """
        title = 'NeverLock: The Virtual Drinking Bird'
        print('*'*50)
        print('*** ' + title, end='')
        print(' '*(43-len(title)) + '***')
        print('*'*50)
        
    def display_help(self):
        """
        Function to display help menu
        """
        self.display_title()
        usage_title_line = 'Usage Options:'
        help_line = '-h: Show the help screen.'
        freq_line = '-f: Set key press frequency (minutes).'
        timer_line = '-t: Set run timer (minutes).'
        print('*** ' + usage_title_line, end='')
        print(' '*(43-len(usage_title_line)) + '***')
        print('*** ' + help_line, end='')
        print(' '*(43-len(help_line)) + '***')
        print('*** ' + freq_line, end='')
        print(' '*(43-len(freq_line)) + '***')
        print('*** ' + timer_line, end='')
        print(' '*(43-len(timer_line)) + '***')
        print('*'*50)
        sys.exit(0)

    def display_info(self):
        """
        Function to display run info
        """
        self.display_title()
        move_freq_line = 'Click Frequency: ' + str(self.move_frequency_minutes) + ' minutes.'
        run_timer_line = 'Run Timer: ' + str(self.stop_timer_minutes) + ' minutes.'
        print('*** ' + move_freq_line, end='')
        print(' '*(43-len(move_freq_line)) + '***')
        print('*** ' + run_timer_line, end='')
        print(' '*(43-len(run_timer_line)) + '***')
        print('*'*50)
    
    def display_stop(self):
        """
        Function to display 'stop' message
        """
        stop_line = 'Press [enter] to stop.'
        print('*** ' + stop_line, end='')
        print(' '*(43-len(stop_line)) + '***')
        print('*'*50)

    def display_finished(self):
        """
        Function to display 'finished' message
        """
        finish_line = 'NeverLock has finished.'
        print('*'*50)
        print('*** ' + finish_line, end='')
        print(' '*(43-len(finish_line)) + '***')
        print('*'*50)

if __name__ == "__main__":   

    nl = NeverLock(run_options = sys.argv[1:])
