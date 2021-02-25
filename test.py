import datetime

msg_create = datetime.datetime(1970, 1, 1)
difference = (datetime.datetime.now() - msg_create).total_seconds()
difference = round(difference)
print(difference)