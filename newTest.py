import time
from pyduino import Arduino

a = Arduino()
time.sleep(3)
a.set_pin_mode(13, 'O')
a.set_pin_mode(12, 'I')
time.sleep(1)
while True:
    print(a.digital_read(12))
