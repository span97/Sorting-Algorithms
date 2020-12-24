"""
2208-CSE-5311-002-DSGN & ANLY ALGORITHMS
Project 1 - sorting algorithms 
Name : Sai Spandana Gali
ID : 1001831591

"""

import time
import random

#Create an array 

def create_an_array():
    array=[]
    choice = input("\nDo you want to enter the input? Type Y for yes and N for no : ")
    if(choice=="Y" or choice=="y"):
        n =int(input("\nEnter the size of the input : "))
        for i in range(0,n):

            element=int(input("\nEnter the number you want to add to your array : "))
            array.append(element)
        return array
    if(choice=="N" or choice=="n"):
        n =int(input("\nEnter the size of the input : "))
        start_range=int(input("\nEnter the start of the range : "))
        end_range= int(input("\nEnter the end of the range : "))
        for i in range(0,n):
            element=random.randint(start_range,end_range)
            array.append(element)
        return array

    

#BUBBLE SORT

def bubbleSort(array):
    iteration=0
    step=len(array)
    
    
    while iteration<=step:
        for i in range(0,len(array)-1):
            
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        iteration+=1
        
    return array
        

    
#INSERTION SORT
    
def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j = i-1
        while(j>=0 and key<array[j]):
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array





# SELECTION SORT 

def SelectionSort(array):
    for i in range(0,len(array)):
        minimum=i
        for j in range(minimum+1,len(array)):
            
            if(array[j]<=array[minimum]):
                minimum=j
                
        
        array[i],array[minimum]=array[minimum],array[i]
    return array


    
    
# MERGE SORT   

def merge_sort(array):
    if(len(array)==1):
        return array
    a1=array[0:len(array)//2]
    a2=array[len(array)//2:]
    
    a1=merge_sort(a1)
    a2=merge_sort(a2)
    return merge(a1,a2)

  
def merge(arrayA,arrayB):
    arrayC=[]
    while(len(arrayA) and len(arrayB)!=0):
        if(arrayA[0]>arrayB[0]):
            arrayC.append(arrayB[0])
            arrayB.pop(0)
        else:
            arrayC.append(arrayA[0])
            arrayA.pop(0)
            
    while (len(arrayA)!=0):
        arrayC.append(arrayA[0])
        arrayA.pop(0)
    while (len(arrayB)!=0):
        arrayC.append(arrayB[0])
        arrayB.pop(0)
    return(arrayC)




#QUICK SORT :

def quick_sort(array,low,high):
    if(low < high):
        pi = partition(array,low,high)
        
        quick_sort(array,low,pi -1) 
        quick_sort(array,pi+1,high)
    return array
                
                
def partition(array,low,high):
    pivot=array[high]
    
    i=low-1 
    
    for j in range(low,high):
        
        if(array[j]<=pivot):
            i+=1;
            array[i],array[j]=array[j],array[i]
            
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)




#QUICK SORT 3 MEDIAN :

def swapping(array,c,low,high):
    
    array[c],array[high]=array[high],array[c]
    return array
    
    
def choose_median(array,low,middle,high):
 
    if(array[low]<=array[middle] and array[middle]<=array[high] ):
        return middle
    if(array[high]<=array[middle] and array[middle]<=array[low]):
        return middle
    if(array[low]<=array[high] and array[high]<=array[middle]):
        return high
    if(array[middle]<=array[high]and array[high]<=array[low]):
        return high
    if(array[low]<=array[middle] and array[high]<=array[middle]):
        return low
    return low



def quickSort_3Median(array,low,high):
    if(low < high):
        pi = partition(array,low,high)
        
        quick_sort(array,low,pi -1) 
        quick_sort(array,pi+1,high)
    return array
                
                
def partition_3Median(array,low,high):
    pivot=array[high]
    
    i=low-1 
    
    for j in range(low,high):
        
        if(array[j]<=pivot):
            i+=1;
            array[i],array[j]=array[j],array[i]
            
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)





# Heap Sort :

def heapify(array,n,i):
    maximum= i 
    left = i*2 +1
    right = i*2 +2
    if (left <n and array[left]>array[maximum]):
        maximum = left
    if (right <n and array[right]>array[maximum]):
        maximum = right
        
    if maximum != i:
        array[maximum],array[i]=array[i],array[maximum]
        heapify(array,n,maximum)

        
def build_heap(array,n):
    for i in range(n//2-1,-1,-1):
        heapify(array,n,i)
    
def heap_sort(array,n):
    
    build_heap(array,n)
    
    for i in range(n-1,0,-1):
        array[i],array[0]= array[0],array[i]
        heapify(array,i,0)
        
    return array    
        




array=create_an_array()

print("\nYour array : ",array)

#BUBBLE SORT OUTPUT
start_time_bs = time.time()
bs=bubbleSort(array)
end_time_bs = time.time()
runtime_bs=end_time_bs-start_time_bs

print("\nAfter Bubble Sort Algorithm : ",bs)
print("The runtime for bubble sort is : ",'{:.10f}'.format(runtime_bs))



# INSERTION SORT OUTPUT 
start_time_is = time.time()
IS=insertionSort(array)
end_time_is = time.time()
runtime_is=end_time_is-start_time_is

print("\nAfter Insertion Sort Algorithm : ",IS)
print("The runtime for Insertion sort is : ",'{:.10f}'.format(runtime_is))


# SELECTION SORT OUTPUT

start_time_ss = time.time()
ss=SelectionSort(array)
end_time_ss = time.time()
runtime_ss=end_time_ss-start_time_ss


print("\nAfter Selection Sort Algorithm : ",ss)
print("The runtime for Selection sort is : ",'{:.10f}'.format(runtime_ss))





#MERGE SORT OUTPUT
start_time_ms = time.time()
ms=merge_sort(array)
end_time_ms = time.time()
runtime_ms=end_time_ms-start_time_ms


print("\nAfter Merge Sort Algorithm : ",ms)
print("The runtime for merge sort is : ",'{:.10f}'.format(runtime_ms))



#QUICK SORT OUTPUT
start_time_qs = time.time()
qs=quick_sort(array,0,len(array)-1)
end_time_qs = time.time()
runtime_qs=end_time_qs-start_time_qs

print("\nAfter Quick Sort Algorithm : ",qs)
print("The runtime for quick sort is : ",'{:.10f}'.format(runtime_qs))



#QUICK SORT MEDIAN OF 3 OUTPUT
start_time_qs_3 = time.time()
pivot=choose_median(array,0,len(array)//2,len(array)-1)
array_median=swapping(array,pivot,0,len(array)-1)
qs_3med = quickSort_3Median(array_median,0,len(array_median)-1)
end_time_qs_3 = time.time()
runtime_qs_3=end_time_qs_3-start_time_qs_3


print("\nAfter Quick Sort Algorithm 3 Median : ",qs_3med)
print("The runtime for quick sort 3 median is : ",'{:.10f}'.format(runtime_qs_3))


#HEAP SORT OUTPUT 
start_time_Heap = time.time()
hs = heap_sort(array,len(array))
end_time_Heap = time.time()

runtime_Heap=end_time_Heap-start_time_Heap

print("\nAfter Heap sort Alogrithm : ",hs)
print("The runtime for Heap Sort  : ",'{:.10f}'.format(runtime_Heap))



