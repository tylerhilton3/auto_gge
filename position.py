import pyautogui as p
import time as t

t.sleep(4)
x = p.position()[0]
y = p.position()[1]
print(f"coords ({x}, {y})")
print(f"rgb    {p.pixel(x, y)}")
# p.moveTo(1161, 653)