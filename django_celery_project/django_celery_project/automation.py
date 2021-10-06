import pyautogui as auto


for i in range(10000000):
    auto.typewrite("Hello World")
    auto.sleep(5)