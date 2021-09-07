from datetime import datetime
from dateutil import relativedelta

agora = datetime.now()
print(agora)

alteracao = relativedelta.relativedelta(hours=2, days=2, years=1, weeks=1)
print(agora + alteracao)
