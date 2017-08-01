import time

with open('today.txt', 'rt') as input:
	today_string = input.read()

fmt = '%Y-%m-%d\n'
print( time.strptime(today_string, fmt) )

