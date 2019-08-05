from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *
import time
import random
import os
import datetime

set_config('01','12','1E')

time.sleep(3.5)

aux = time.time()


panel = getPanel()
print("Panel", panel)

elapsed = time.time() - aux

print("Elapsed time: ", elapsed)




