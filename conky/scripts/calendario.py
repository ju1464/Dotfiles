#!/usr/bin/python
import time, calendar, re

localtime = time.localtime(time.time())
calendar.setfirstweekday(calendar.MONDAY)
cal = calendar.month(localtime[0], localtime[1])

parts = cal.split('\n')
cal = '${color lightblue}${alignc}${offset -13}' + '\n'.join(parts)

regex = '(?<= )%s(?= )|(?<=\n)%s(?= )|(?<= )%s(?=\n)' % (localtime[2], localtime[2], localtime[2])
replace = '${color red}%s${color lightblue}' % localtime[2]
newCal = re.sub(regex, replace, cal)
print newCal
