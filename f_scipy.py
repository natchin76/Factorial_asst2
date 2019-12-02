from scipy.special import factorial as f
import time
n=input('Enter the integer')
if (n<0):
	print('Input error. Enter a positive integer')
else:
	st_time=time.time()  
	f=f(n)
	end_time=time.time()
	print(f)
	print("time to run the function",end_time-st_time)
