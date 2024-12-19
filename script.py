import datetime
import sys

minute = datetime.datetime.now().minute
if minute % 2 == 0:
    print('Current minute is even')
    sys.exit(0)
else:
    print('Current minute is odd')
    sys.exit(1)
