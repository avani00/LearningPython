import sys
import os
from datetime import datetime
import time
hour_given = int(input('What hour do you want to be notified? (Put in terms of 00) '))
minute_given = int(input('What minute do you want to be notified? (Put in terms of 00) '))
second_given = int(input('What second do you want to be notified? (Put in terms of 00) '))
while True:
	current_hour = datetime.now().hour
	current_minute = datetime.now().minute
	current_second = datetime.now().second
	if current_second == second_given and current_minute == minute_given and current_hour == hour_given:
		break
	else:
		time.sleep(1)
sys.stdout.write('\a')
sys.stdout.flush()
os.system('say "rjgaierfjlzsdkvjlaiorjjaiurwjkgaksdjpaoirjaw"')