# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#

def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        for i in range(item):
            if descending == False:
                if data[i][index]>data[i+1][index]:
                    temp = data[i]
                    data[i]=data[i+1]
                    data[i+1]=temp
            else:
                if data[i][index]<data[i+1][index]:
                    temp = data[i]
                    data[i]=data[i+1]
                    data[i+1]=temp
    
    #data.sort(key=lambda t: t[index], reverse=descending)


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(1,len(data)):

        position = item
        currentValue = data[item]
        if descending == True:
            while position > 0 and data[position-1][index]<currentValue[index]:
                data[position]=data[position-1]
                position=position-1
        else:
            while position>0 and data[position-1][index]>currentValue[index]:
                data[position]=data[position-1]
                position=position-1
        
        data[position]=currentValue


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        maxposition=0
        for i in range(1,item+1):
            if descending == False:
                if data[i][index]>data[maxposition][index]:
                    maxposition=i
            else:
                if data[i][index]<data[maxposition][index]:
                    maxposition=i
        temp=data[item]
        data[item]=data[maxposition]
        data[maxposition]=temp

def quick_sort_helper(data, first, last, index, descending):
    
    def partition(data, first, last):
        pivot=data[first][index]
        leftmark=first+1
        rightmark=last
        done = False
        while not done:
            if descending==False:
                while leftmark<=rightmark and data[leftmark][index]<=pivot:
                    leftmark=leftmark+1
                
                while rightmark>=leftmark and data[rightmark][index]>=pivot:
                    rightmark=rightmark-1
            elif descending== True:
                while leftmark<=rightmark and data[leftmark][index]>=pivot:
                    leftmark=leftmark+1
                
                while rightmark>=leftmark and data[rightmark][index]>=pivot:
                    rightmark=rightmark-1

            if rightmark<leftmark:
                done = True
            
            else:
                temp=data[rightmark]
                data[rightmark]=data[leftmark]
                data[leftmark]=temp

        temp = data[first]
        data[first] = data[rightmark]
        data[rightmark] = temp

        return rightmark

    if first<last:
        splitpoint=partition(data,first,last)
        quick_sort_helper(data,first,splitpoint-1, index, descending)
        quick_sort_helper(data,splitpoint+1,last, index, descending)
    
    


def quick_sort(data, index, descending=False):
    '''Sorts using the quick sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    #data.sort(key=lambda t: t[index], reverse=descending)
    quick_sort_helper(data,0, len(data)-1, index, descending)


def python_sort(data, index, descending=False):
    '''Sorts using the native Python sort algorithm (Timsort)'''
    # LEAVE this function as is - it will allow you to see your sorts against the python one
    data.sort(key=lambda t: t[index], reverse=descending)


# data = [
#     ( 'homer', 'simpson', 50 ),
#     ( 'luke', 'skywalker', 87 ),
#     ( 'bilbo', 'baggins', 111 ),
#     ( 'frodo', 'baggins', 103 ),
#     ( 'leia', 'skywalker', 67 ),
# ]

# quick_sort(data,2, True)
# print(data)