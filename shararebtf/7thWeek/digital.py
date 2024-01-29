import time
import datetime as dt
import turtle

tm = turtle.Turtle()


sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

while True:
	tm.ht()
	tm.clear()
	tm.write(str(hr).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2), font=("Arial Narrow", 35, "bold"))
	tm.write(dt.date.today(), font=("Arial Narrow", 7, "bold"))
	time.sleep(1)
	sec += 1

	if sec == 60:
		sec = 0
		min += 1

	if min == 60:
		min = 0
		hr += 1

	if hr == 13:
		hr = 1
