import time
from clewareampel import ClewareAmpel

ampel = ClewareAmpel()
ampel.all_on()
time.sleep(1)
ampel.green_only()
time.sleep(1)
ampel.yellow_only()
time.sleep(1)
ampel.red_only()
time.sleep(1)
ampel.green_on()
time.sleep(1)
ampel.red_off()
time.sleep(1)
ampel.all_off()
