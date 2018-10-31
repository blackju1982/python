#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.

#Justin Blackford



from time import time
from random import *

#builder from class
def build(alist, size):
  for count in range(0, size):
    alist.append( randint(0, 1000000) )

#bubble sort and timer from class
def bubble_sort(alist):
    for outer in range(0, len(alist)-1 ):
        for inner in range(0, len(alist)-2 ):
            if ( alist[inner] > alist[inner+1] ):
                (alist[inner], alist[inner+1]) = ((alist[inner+1], alist[inner]))

def time_one_run_bubble_sort(size):
  l = []
  build(l, size)
  start_time = time()
  bubble_sort(l)
  end_time = time()
  return end_time - start_time

def bubbleCount(alist):
	counter = 0
	for outer in range(0, len(alist)-1 ):
		for inner in range(0, len(alist)-2 ):
			counter += 1
			if ( alist[inner] > alist[inner+1] ):
				counter += 2
				(alist[inner], alist[inner+1]) = ((alist[inner+1], alist[inner]))
	return counter

def countBubbleRun(size):
  l = []
  build(l, size)
  return bubbleCount(l)

#insertion sort and timer
def insertSort(alist):
	for n in range(1, len(alist)):

		currentValue = alist[n]
		position = n

		while position > 0 and alist[position - 1] > currentValue:
				alist[position] = alist[position - 1]
				position = position - 1

		alist[position] = currentValue

def timeInsertsort(size):
    l = []
    build(l, size)
    start_time = time()
    insertSort(l)
    end_time = time()
    return end_time - start_time

def  insertCount(alist):
	counter = 0
	for n in range(1, len(alist)):
		counter += 1
		currentValue = alist[n]
		position = n

		while position > 0 and alist[position - 1] > currentValue:
				counter += 1
				alist[position] = alist[position - 1]
				position = position - 1

		alist[position] = currentValue

	return counter

def countInsertRun(size):
  l = []
  build(l, size)
  return insertCount(l)

#main

#Text output for testing
# for count in range(0, 1000, 10):
#     timer_bubble = time_one_run_bubble_sort(count)
#     timerInsert = timeInsertsort(count)

#     print (str(count) + ", Bubble Sort Time: " + str(timer_bubble) + ", Times accessed: " + str(countBubbleRun(count)) +
#     " Insertion Sort Time: " + str(timerInsert) + ", Times accessed: " + str(countInsertRun(count)))

#Formatting for csv file
for count in range(0, 1000, 10):
    timer_bubble = time_one_run_bubble_sort(count)
    timerInsert = timeInsertsort(count)

    print (str(count) + ", " + str(timer_bubble) + ", " + str(countBubbleRun(count)) + ", " + str(timerInsert) + ", " + str(countInsertRun(count)))