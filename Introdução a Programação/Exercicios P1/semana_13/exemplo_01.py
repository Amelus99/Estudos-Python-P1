from datetime import datetime
from datetime import timedelta
import time

agora = datetime.now()
print(agora)

print("{}/{}/{}".format(agora.day, agora.month, agora.year))
print("{}:{}:{}".format(agora.hour, agora.minute, agora.second))

time.sleep(2)

alteracao = timedelta(hours=16)
print(agora + alteracao)
