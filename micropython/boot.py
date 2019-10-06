# This file is executed on every boot (including wake-boot from deepsleep)

import config

def ap_disable():
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

def wifi_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.WIFI_SSID, config.WIFI_PSK)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def wifi_disable():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    print("WiFi disabled")

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)

def disable_repl():
    import uos, machine
    #uos.dupterm(None, 1) # disable REPL on UART(0)

def enable_webrepl():
    import webrepl
    webrepl.start()

def activate_garbage_collection():
    import gc
    gc.collect()
    print('garbage collection activated')

# no_debug()
ap_disable()
# wifi_connect()
wifi_disable()
activate_garbage_collection()
# enable_webrepl()
