import time
from simple_ruuvitag.ruuvi import RuuviTagClient

ruuvi_client = RuuviTagClient()
ruuvi_client.start()

time.sleep(5)
last_datas = ruuvi_client.get_current_datas()
print(last_datas)
ruuvi_client.rescan()
time.sleep(5)
last_datas = ruuvi_client.get_current_datas()
print(last_datas)
time.sleep(5)
