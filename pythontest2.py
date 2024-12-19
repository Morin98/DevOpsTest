import datetime
import sys

second = datetime.datetime.now().second
if second > 30:
    print('Current second is between 31 and 59')
    sys.exit(0)
else:
    print('Current second is between 1 and 30 ')
    sys.exit(1)
