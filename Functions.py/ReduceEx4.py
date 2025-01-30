import functools

#ReduceEx4.py
oldsal=list([float(sal) for sal in input("Enter salaries:").split() if float(sal) in range(0,1001)])
print(oldsal)
sal0_500=list(filter(lambda sal: 0<=sal<=500,oldsal))
hikesal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
hiketotsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal0_500)
print("-"*50)
print("Salaries ranges 0 -500\tHike Salaries ranges 0 -500")
print("-"*50)
for sal,hike in zip(sal0_500,hikesal0_500):
    print("\t{}\t\t\t\t\t{}".format(sal,hike))
print("-"*50)
print(" Total:{}\t\t\t\t{}".format(totsal0_500,hiketotsal0_500))
sal501_1000=list(filter(lambda sal:501<=sal<=1000,oldsal))
hikesal501_1000=list(map(lambda sal:sal+sal*20/100,sal501_1000))
print("-"*50)
print("Salaries ranges 501 -1000\tHike Salaries ranges 501 -1000")
print("-"*50)
for sal,hike in zip(sal501_1000,hikesal501_1000):
    print("\t{}\t\t\t\t\t{}".format(sal,hike))
print("-"*50)
totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
tothikesal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
print(" Total:{}\t\t\t\t{}".format(totsal501_1000,tothikesal501_1000))
print("-"*50)
print("Grand Totals:{}\t\t\t{}".format(totsal0_500+totsal501_1000,hiketotsal0_500+tothikesal501_1000))
print("*"*50)













