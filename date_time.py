import datetime as dt

date_ = dt.datetime.now()
# print(date_.year)
# print(date_.time())

# mydate = dt.datetime(2025, 1, 1, 12, 00, 00)
# print(mydate)

# print(date_.strftime("%a %B, %Y. %H:%M:%S %p"))
# %a	Weekday, short version	Wed	

# %A	Weekday, full version	Wednesday	

# %w	Weekday as a number 0-6, 0 is Sunday	3	

# %d	Day of month 01-31	31	

# %b	Month name, short version	Dec	

# %B	Month name, full version	December	

# %m	Month as a number 01-12	12	

# %y	Year, short version, without century	18	

# %Y	Year, full version	2018	

# %H	Hour 00-23	17	

# %I	Hour 00-12	05	

# %p	AM/PM	PM	

# %M	Minute 00-59	41	

# %S	Second 00-59	08	

# %f	Microsecond 000000-999999	548513	

# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	

# %U	Week number of year, Sunday as the first day of week, 00-53	52	

# %W	Week number of year, Monday as the first day of week, 00-53	52	

# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	

# %C	Century	20	

# %x	Local version of date	12/31/18	

# %X	Local version of time	17:41:00
# 	
# # %%	A % character	%	

# %G	ISO 8601 year	2018	

# %u	ISO 8601 weekday (1-7)	1	

# %V	ISO 8601 weeknumber (01-53)	01

import pygame

print('Alarm..'.center(100))


hour = input('Hour: ').strip()
minute = input('Minute: ').strip()
second = input('Second: ').strip()
am_pm = input('AM/PM: ').strip().upper()

pygame.init()
pygame.mixer.music.load(r"C:\Users\Hp\Music\SQI.mp3")




while True: 
    date_now = dt.datetime.now()

    if date_now.strftime('%H') == hour and date_now.strftime('%M') == minute and date_now.strftime('%S') == second and date_now.strftime('%p') == am_pm:
        
        print('Alarm is ringing..'.center(100))
        pygame.mixer.music.play()
        pygame.time.wait(10000)
        pygame.mixer.music.stop()



    
