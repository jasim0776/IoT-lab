import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect('Siidisaba7', 'Varst1onuv1!')


# Synchronize clock
import ntptime
ntptime.settime()

# Create a variable for hostname based on MAC address:
import ubinascii as binascii
name = "esp-%s" % binascii.hexlify(wlan.config("mac")[-3:]).decode("ascii")

# Clean up
import gc
gc.collect()


