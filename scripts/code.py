# This is a sample Python script.
import time


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# Press the green button in the gutter to run the script.
if __name__ == '__code__':
    while (True):
        time.sleep(10)  # 10 seconds.
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
