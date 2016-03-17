#!/usr/bin/env python
#coding=utf-8
sum=0

def isPrime(N):
	i=1
	num=0
	while i<=N:
		if N%i==0:
			num=num+1
		i=i+1
	
	if num==2:
		return 1
	else:
		return 0
		

for r in range(2,1000):
	if isPrime(r)==1:
		sum=sum+r
print sum