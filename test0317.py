#!/usr/bin/env python
#coding=utf-8


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
		
print isPrime(2)


