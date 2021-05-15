import random
import re
from datetime import datetime

def add_num():
	print('Addition of 2 digit nos. (10 questions)')
	start_time=datetime.now()
	i=count=0
	max_ques=10
	while i<max_ques:
		i+=1
		a=random.randint(2,99)
		b=random.randint(2,99)
		ans=a+b
		print(f'Question No.{i}')
		res=input(f'{a} + {b} = ').strip()
		if not re.match('^[0-9]+$', res):
			print('Invalid input')
		else:
			if ans == int(res):
				print('Correct !!')
				count+=1
			else:
				print('Wrong !!')
				print(f'Answer is {ans}')
	end_time=datetime.now()
	print(f'Result: Correct = {count}, Wrong = {max_ques-count}')
	calc_time(start_time,end_time)


def subtract_num():
	print('Subtraction of 2 digit nos. (10 questions)')
	start_time=datetime.now()
	i=count=0
	max_ques=10
	while i<max_ques:
		i+=1
		a=random.randint(2,99)
		b=random.randint(2,99)
		if a < b:
			a, b = b, a
		ans=a-b
		# print(f'a is {a}, b is {b}, ans is {ans}')
		print(f'Question No.{i}')
		res=input(f'{a} - {b} = ').strip()
		if not re.match('^[0-9]+$', res):
			print('Invalid input')
		else:
			if ans == int(res):
				print('Correct !!')
				count+=1
			else:
				print('Wrong !!')
				print(f'Answer is {ans}')
	end_time=datetime.now()
	print(f'Result: Correct = {count}, Wrong = {max_ques-count}')
	calc_time(start_time,end_time)


def multiply_num():
	print('Subtraction of 2 digit nos. (10 questions)')
	start_time=datetime.now()
	i=count=0
	max_ques=20
	while i<max_ques:
		i+=1
		a=random.randint(2,19)
		b=random.randint(2,9)
		ans=a*b
		print(f'Question No.{i}')
		res=input(f'{a} * {b} = ').strip()
		if not re.match('^[0-9]+$', res):
			print('Invalid input')
		else:
			if ans == int(res):
				print('Correct !!')
				count+=1
			else:
				print('Wrong !!')
				print(f'Answer is {ans}')
	end_time=datetime.now()
	print(f'Result: Correct = {count}, Wrong = {max_ques-count}')
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
	if opt_sel not in set(('1','2','3','4')):
		print(f'Invalid option - {opt_sel}')
		continue
	else:
		if opt_sel == '1':
			add_num()
		elif opt_sel == '2':
			subtract_num()
		elif opt_sel == '3':
			multiply_num()
		elif opt_sel =='4':
			break
