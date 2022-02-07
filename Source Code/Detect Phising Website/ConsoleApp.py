from PhisingDetection import getResult, getMultiResult, Mode
from print_dict import pd as printdict
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

"""
n = int(input("Please enter mode you want: "))
if n%3 == 1:
    printdict(getMultiResult("./files/urls.csv",Mode.RANDOM_FOREST))
elif n%3 == 2:
    printdict(getMultiResult("./files/urls.csv",Mode.LOGISTIC_REGRESSION))
else:
    printdict(getMultiResult("./files/urls.csv",Mode.SVM))
"""


while True:
    sleep(2)
    screen_clear()
    print("Detect Phising Website")
    print("#-----------------")
    print("1. Single URL")
    print("2. Multi URLs")
    print("3. Exit")
    n = int(input("--> Your choice: "))
    if(n >3 or n <1):
        print("Error!!!! Please enter Again!!!!!!")
        sleep(2)
        screen_clear()
        continue

    if n == 1:
        sleep(2)
        screen_clear()
        print("Enter Single URL Mode -------------------")
        print("All mode to predict:")
        print("1. Random Forest")
        print("2. Logistic Regression")
        print("2. Support Vector Machine")
        print("----------------------")
        url = input("Enter URL: ")
        n = int(input("Please enter mode you want: "))
        print("--> ",end="")
        if n%3 == 1:
            print("This is ",getResult(url,Mode.RANDOM_FOREST))
        elif n%3 == 2:
            print("This is ",getResult(url,Mode.LOGISTIC_REGRESSION))
        else:
            print("This is ",getResult(url,Mode.SVM))
        input()
        continue
    elif n == 2:
        sleep(2)
        screen_clear()
        print("Enter Multi URLs Mode -------------------")
        print("All mode to predict:")
        print("1. Random Forest")
        print("2. Logistic Regression")
        print("2. Support Vector Machine")
        print("----------------------")
        path = input("Enter your file location: ")
        n = int(input("Please enter mode you want: "))
        print("--> ",end="")
        if n%3 == 1:
            printdict(getMultiResult(path,Mode.RANDOM_FOREST))
        elif n%3 == 2:
            printdict(getMultiResult(path,Mode.LOGISTIC_REGRESSION))
        else:
            printdict(getMultiResult(path,Mode.SVM))
        input()
        continue
    else:
        break