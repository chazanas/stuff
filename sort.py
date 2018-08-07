import numpy as np 
import datetime as dt
import pandas as pd
from copy import deepcopy

quick = []
merge = []
heap = []
insert = []
n = 1000
times = 1000

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def switch(l, a, b):
	value_b = l[b]
	l[b] = l[a]
	l[a] = value_b


for i in range(times):
	numbers = np.random.randint(0,2 *n,size=n)
	numbers = np.sort(numbers)
	mask1 = np.random.rand(n) > .95
	mask1 = np.where(mask1)[0]
	mask2 = np.random.rand(n) > .95
	mask2 = np.where(mask2)[0]
	if mask1.shape[0] > mask2.shape[0]:
		mask1 = mask1[:mask2.shape[0]]
	else:
		mask2 = mask2[:mask1.shape[0]]
	for i in range(mask1.shape[0]):
		switch(numbers, mask1[i], mask2[i])



	numbers_list = numbers.tolist()
	list_copy = deepcopy(numbers_list)

	first = dt.datetime.now()
	np.sort(numbers)
	second = dt.datetime.now()
	quick.append((second - first).microseconds)
	third = dt.datetime.now()
	np.sort(numbers, kind='mergesort')
	forth = dt.datetime.now()
	merge.append((forth - third).microseconds)
	fifth = dt.datetime.now()
	np.sort(numbers, kind='heapsort')
	sixth = dt.datetime.now()
	heap.append((sixth - fifth).microseconds)
	seventh = dt.datetime.now()
	insertionSort(numbers_list)
	eighth = dt.datetime.now()
	insert.append((eighth - seventh).microseconds)
	


sorts = [quick, merge, heap, insert]
sorts_mean = np.array(list(map(np.mean, sorts)))
sorts_std = np.array(list(map(np.std, sorts)))
sorts = pd.DataFrame({
	'mean' : sorts_mean,
	'std' : sorts_std
	}, index=[
		'Quicksort',
		'Mergesort',
		'Heapsort',
		'Insertionsort',
	])
print(sorts.sort_values(['mean', 'std']))




