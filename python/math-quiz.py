import random
from datetime import datetime

def add_num():
	print('Addition of 2 digit nos. (10 questions)')
	start_time=datetime.now()
	i=count=0
	while i<10:
		i+=1
		a=random.randint(2,99)
		b=random.randint(2,99)
		ans=a+b
		print(f'Question No.{i}')
		res=int(input(f'{a} + {b} = '))
		if ans == res:
			print('Correct !!')
			count+=1
		else:
			print('Wrong !!')
			print(f'Answer is {ans}')
	end_time=datetime.now()
	print(f'Result: Correct = {count}, Wrong = {10-count}')
	calc_time(start_time,end_time)


def calc_time(start_time,end_time):
	diff_time=end_time-start_time
	h=int(diff_time.seconds/3600)
	m=int(diff_time.seconds/60)
	s=int(diff_time.seconds%60)
	print(f'Total Time : {h} hours {m} minutes {s} seconds')


print('Hello, Welcome to Math Quiz')
while True:
	print('1. Addition   2. Subtraction   3. Multiplication   4. Quit')
	opt_sel=input('Select your option: ')
	if opt_sel == '':
		print('Please select an option !')
		continue
	opt_sel=int(opt_sel)
	if opt_sel not in range(1,5):
		print(f'Invalid option - {opt_sel}')
	else:
		if opt_sel == 1:
			add_num()
		elif opt_sel == 2:
			pass
		elif opt_sel == 3:
			pass
		elif opt_sel ==4:
			break
