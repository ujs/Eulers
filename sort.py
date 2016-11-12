

    
def selection_sort(L):
    '''Selection Sort using inbuilt min() function'''
    for i in range(0, len(L)-1):
        min_val = L[i]
        least_of_rest = min(L[i+1:])
        remaining_min_index = L.index(min(L[i+1:]))       
        if min_val > least_of_rest:
          temp = L[i]
          L[i] = L[remaining_min_index]
          L[remaining_min_index] = temp           
        else: continue
    return L
    

def selectionSort(L):
    '''Selection Sort'''
    for i in range(0,len(L)):
        min_index = i
        min_value= L[i]
        j = i + 1
        for j in range(i+1,len(L)):
            if min_value > L[j]:
                min_index = j
                min_value= L[j]
        temp = L[i]
        L[i] = L[min_index]
        L[min_index] = temp
        
    return L

def bubble_sort(L):
    '''Bubble sorting list, L'''
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(L)-1):
            if L[i]>L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
            else: continue
            swapped = True
    return L

### The following two functions handle merge sort together.

L = [5,3,6,2,32,16,8,12]

def merge(left,right):
    i = 0
    j = 0
    merged_ans = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_ans.append(left[i])
            i += 1
        else:
            merged_ans.append(right[j])
            j += 1
    while i < len(left):
        merged_ans.append(left[i])
        i += 1
    while i < len(right):
        merged_ans.append(right[i])
        i += 1
    return merged_ans

def sort(L):
    if len(L) == 1 : return L
    else:
        mid = int(len(L)/2)
        left_side = sort(L[:mid])
        right_side = sort(L[mid:])
        final_ans = merge(left_side,right_side)
        return final_ans
            


    
