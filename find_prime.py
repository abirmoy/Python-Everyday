import time
lower = 0
upper = 100000

tic = time.time()
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
           else:
               print(num)
       
print('Time:', time.process_time())
toc = time.time()

print(toc-tic)