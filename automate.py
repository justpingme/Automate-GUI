import pyautogui as gui
from time import sleep


# print(gui.size())


# sleep(3)

# print(gui.position()) 
       
gui.click(1206, 43, 1)

gui.hotkey('command','o', duration=2)

print("###############")
print("\tsearching test.txt file")
gui.locateAllOnScreen("test.txt")
sleep(0.5)

gui.press('t')
sleep(0.5)

print("\topening test.txt file")
gui.hotkey('command','o', duration=2)
sleep(0.5)

gui.hotkey('command','+')
gui.hotkey('command','+')
gui.hotkey('command','+')

print("\twritting Hello, World to test.txt")
gui.write(" Hello, World! ", interval=0.25)
sleep(0.5)


print("\tcmd+s save the test.txt ")
gui.hotkey('command','s', duration=0.25)
sleep(0.5)

print("\tcmd+q close the test.txt ")
gui.hotkey('command','q', duration=0.25)
sleep(0.5)

print("\tcmd+w close the curret window")
gui.hotkey('command','w', duration=0.25)




