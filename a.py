from datetime import datetime, date
time = datetime.now().time().strftime("%X")
date = datetime.now().date()
print(date, time )