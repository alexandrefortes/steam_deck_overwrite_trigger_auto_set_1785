import sys, os, platform
from time import sleep
from controller_if import ControllerInterface

def kill_steam():
    if platform.system() == 'Linux':
        os.system('killall steam > /dev/null')
        sleep(1.0)

def connect_cb(hid_dev_mgr):
    global connected
    connected = True

eps = ((10462, 4613), )
sleep(0.2)
cntrlr_mgr = ControllerInterface(eps, connect_cb)

connection_tries = 10
connected = False

while not connected:
    if connection_tries > 0:
        connection_tries -= 1
        sleep(0.1)

if connection_tries <= 0:
    cntrlr_mgr.shutdown()
    sys.exit(0)
else:
    sleep(0.1)
    cntrlr_mgr.load_default_mappings()
    cntrlr_mgr.load_default_settings()
    cntrlr_mgr.trigger_cancel_cal()

def main():
    left_trigger_cal = cntrlr_mgr.trigger_get_cal(0)
    right_trigger_cal = cntrlr_mgr.trigger_get_cal(1)
    lmax = 1785
    rmax = 1785
    lmin = left_trigger_cal[2]
    rmin = right_trigger_cal[2]
    kill_steam()
    cntrlr_mgr.trigger_set_cal(0, lmax, lmin, left_trigger_cal[3])
    cntrlr_mgr.trigger_set_cal(1, rmax, rmin, right_trigger_cal[3])
    cntrlr_mgr.shutdown()
    os._exit(0)

main()