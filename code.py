import time
import sys
import serial
import pyautogui
if __name__ == "__main__":
    try:
        board = serial.Serial(sys.argv[1], 9600)
        previos_command_one = -1
        previos_command_two = -1
        data = -1
        while 1:

            data = ord(board.readline().decode('utf-8')[0])
            if data == 48 or data == 49:
                if data != previos_command_one:
                    print("data one is : {0}".format(data))

                    pyautogui.click(button='left')

                    previos_command_one = data

            if data == 50 or data == 51:
                if data != previos_command_two:
                    print("data two is : {0}".format(data))

                    pyautogui.click(button='right')

                    previos_command_two = data

    except Exception as e:
        print(e)
