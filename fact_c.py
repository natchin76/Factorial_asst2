from ctypes import *
import time
libpy = CDLL("./libpy.so")    #load .so file into object file
n=input('Enter the integer')
st_time=time.time()
f=libpy.fact(n)
end_time=time.time()
print(f)
print("time to run the function",end_time-st_time)
