import datetime

minute = datetime.datetime.now().minute
if minute % 2 == 0:
    print('Current minute is even')
else:
    print('Current minute is odd')
