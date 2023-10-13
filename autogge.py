import pyautogui as p
import time as t
import random as r

# var = bottom left corner coords, top right corner coords
supply_bounds  = [(878, 1019),  (938, 926)]
pillory_bounds = [(1050, 1020), (1111, 921)]
location1      = [(1161, 653), (1161, 653)]
location2      = [(1294, 721), (1294, 721)]
skip_bounds    = [(1021, 684), (1062, 665)]
sell1_bounds   = [(1161, 773), (1186, 748)]
sell2_bounds   = [(1298, 837), (1315, 820)]
confirm_bounds = [(1082, 773), (1182, 753)]



def wait():
    t.sleep(r.random()*0.5+0.7)

def clik(coords):
    wait()
    x1 = coords[0][0]
    x2 = coords[1][0]
    y1 = coords[0][1]
    y2 = coords[1][1]
    xval = r.randint(coords[0][0], coords[1][0])
    yval = r.randint(coords[0][1], coords[1][1])
    p.click(x=xval,y=yval)

t.sleep(5)
clik(supply_bounds)
clik(location2)
while p.pixel(524, 244) == (154, 178, 71):
    clik(supply_bounds)
    clik(location1)
    clik(skip_bounds)
    clik(sell2_bounds)
    clik(confirm_bounds)
    clik(supply_bounds)
    clik(location2)
    clik(skip_bounds)
    clik(sell1_bounds)
    clik(confirm_bounds)