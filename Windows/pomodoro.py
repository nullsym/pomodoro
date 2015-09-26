#!/usr/bin/env python2

# Documentation
# https://docs.python.org/3.5/howto/curses.html
# http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
# http://stackoverflow.com/questions/25189554/countdown-clock-0105

import time, sys
import re
import os
import subprocess

###############
# Global vars #
###############
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
# AUDIO1 was downloaded from http://soundbible.com/1795-Electrical-Sweep.html
# and it has a Public Domain license
# AUDIO2 was downloaded from http://soundbible.com/1823-Winning-Triumphal-Fanfare.html
# and it has a Attribution 3.0 license
# AUDIO3 was downloaded from http://soundbible.com/1846-Warbling-Vireo.html
# and it has a Attribution 3.0 license
AUDIO1 = SCRIPT_DIR + "\\1.wav"
AUDIO2 = SCRIPT_DIR + "\\2.wav"
AUDIO3 = SCRIPT_DIR + "\\3.wav"

#############
# Functions #
#############
def play_audio(option):
    if sys.platform == "win32":
        import winsound

        # Check that all the files exist
        if not os.path.isfile(AUDIO1):
            print("Error: The file " + AUDIO1 + " is missing!")
            time.sleep(2)
            system.exit("Error: missing audio file")
        elif not os.path.isfile(AUDIO2):
            print("Error: The file " + AUDIO2 + " is missing!")
            time.sleep(2)
            system.exit("Error: missing audio file")
        elif not os.path.isfile(AUDIO3):
            print("Error: The file " + AUDIO3 + " is missing!")
            time.sleep(2)
            system.exit("Error: missing audio file")

        # Play the sounds
        if option == 1:
            winsound.PlaySound(AUDIO1, winsound.SND_FILENAME)
        elif option == 2:
            winsound.PlaySound(AUDIO2, winsound.SND_FILENAME)
        elif option == 3:
            winsound.PlaySound(AUDIO3, winsound.SND_FILENAME)

    else:
        print("Platform not supported. This script only works on Windows.")


def count_down(seconds):
    while seconds:
        # On the first divmod the quotient will be the minutes and the remainder will be the seconds
        # On the second divmod the quotient will be the hours and the remainder will be the minutes
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        sys.stdout.write("\r" + time_format)
        sys.stdout.flush()
        time.sleep(1)
        seconds = seconds - 1
    # Print newline to avoid weirdness due to carriage return
    print("\n")


def convert_to_seconds(given_time):
    seconds = 0
    m1 = re.search('0*(\d+)h', given_time)
    m2 = re.search('0*(\d+)m', given_time)
    m3 = re.search('0*(\d+)s', given_time)
    # Hours
    if m1:
        seconds = seconds + (int(m1.group(1)) * SECONDS_IN_HOUR)
    # Minutes
    if m2:
        seconds = seconds + (int(m2.group(1)) * SECONDS_IN_MINUTE)
    # Seconds
    if m3:
        seconds = seconds + int(m3.group(1))

    if seconds == 0:
        sys.exit("There was an error with the string you gave me. Aborting.")

    return seconds

########
# Main #
########
while True:
    print("+--------------------+")
    print("| 1) Countdown timer |")
    print("| 2) Pomodoro timer  |")
    print("+--------------------+")
    print("\nNote: To exit out of the loop close the windows or press ctrl+c")
    print("\n")
    # Grab user input
    user_input = raw_input("Choose a mode: ")

    # Countdown timer mode
    if user_input == "1":
        user_input = raw_input("For how long: ")
        count_down(convert_to_seconds(user_input))
        play_audio(1)

    # Pomodoro mode
    elif user_input == "2":
        print("Example: Suppose we want to study for 2 hours, with a 10min break and iterate 2 times. Then we would need to input:\n")
        print("Example input: 2h 10m 2")
        print("------------------------\n")
        input_raw = raw_input("For how long: ")
        input_list = input_raw.split()

        # Continue with the infite loop until user gives proper arguments
        if len(input_list) != 3:
            print("This option must receive three arguments. Try again.")
            continue
        # Continue with the infite loop until user gives proper arguments
        if not input_list[2].isdigit():
            print("The third argument must be  digit. It denotes how many loops you want")
            continue

        # Start pomodoro
        for i in range(int(input_list[2])):
            count_down(convert_to_seconds(input_list[0]))
            play_audio(2)
            count_down(convert_to_seconds(input_list[1]))
            play_audio(3)
            print("Loop %d completed") % i
