import pyautogui as p
import time as t
import random as r

# var = top left corner coords, bottom right corner coords
supply_bounds  = [(873, 923),  (936, 1022)]
# pillory_bounds = [(1050, 1020), (1111, 921)]
location1      = (1178, 609)
location1      = [location1, location1]
location2      = (1291, 714)
location2      = [location2, location2]
skip_bounds    = [(1025, 666), (1063, 682)]
sell1_bounds   = [(1180, 709), (1201, 729)]
sell2_bounds   = [(1278, 809), (1301, 832)]
confirm_bounds = [(1086, 754), (1188, 772)]



def wait(sell):
    t.sleep(r.random()*0.1+1+0.5*sell)

def clik(coords, sell=False):
    wait(sell)
    xval = r.randint(coords[0][0], coords[1][0])
    yval = r.randint(coords[0][1], coords[1][1])
    p.moveTo(x=xval,y=yval)
    t.sleep(0.1)
    p.click()

t.sleep(5)
clik(supply_bounds)
clik(location2)
while p.pixel(60, 131) == (183, 0, 0):
    clik(supply_bounds)
    clik(location1)
    clik(skip_bounds)
    clik(sell2_bounds,True)
    clik(confirm_bounds)
    clik(supply_bounds)
    clik(location2)
    clik(skip_bounds)
    clik(sell1_bounds, True)
    clik(confirm_bounds)