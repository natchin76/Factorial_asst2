import fact
import time
n=input('Enter the integer')
st_time=time.time()  
f=fact.f(n)
end_time=time.time()
print(f)
print("time to run the function",end_time-st_time)
