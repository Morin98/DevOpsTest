import datetime
import os

minute = datetime.datetime.now().minute
if minute % 2 == 0:
    print('Current minute is even')
    os.exit(0)
else:
    print('Current minute is odd')
    os.exit(1)
