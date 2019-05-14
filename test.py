import time
from datetime import datetime, timedelta
import os

now_hour = time.localtime().tm_hour
# print(now_hour)
pre_date = str(datetime.today().date() - timedelta(days=1))
result_path = f'D:\\sina\\{pre_date}'
if not os.path.exists(result_path):
    print(1)
else:
    print(2)